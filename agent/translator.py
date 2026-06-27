"""
Traductor para ToME4-es usando LibreTranslate (Docker local).
API REST en http://localhost:5000

Mejoras v2:
- Placeholders robustos §PHN§ (protege @vars@, <tags>, [[refs]], {{lua}})
- POST_PROCESS: correcciones post-traducción (usted→tú, términos de juego)
"""

import re
import json
import urllib.request
import urllib.parse


# ---------------------------------------------------------------------------
# Placeholder helpers
# ---------------------------------------------------------------------------


def _save_ph(m, ph_map, prefix="PH"):
    """Guarda un match en ph_map y devuelve el placeholder §prefix<N>§."""
    idx = len(ph_map)
    key = f"\u00a7{prefix}{idx}\u00a7"  # § = U+00A7, LT lo respeta
    ph_map[key] = m.group(0)
    return key


def protect_patterns(text):
    """
    Protege patrones especiales que LibreTranslate mutilaría.
    Retorna (texto_limpio, ph_map) donde ph_map {placeholder: original}.
    """
    ph_map = {}

    # 1) Proteger @variables@ (ej: @Source@, @Target@, @himher@)
    text = re.sub(r"@(\w+)@", lambda m: _save_ph(m, ph_map, "AT"), text)

    # 2) Proteger #Source#, #Target# (Capitalized = game vars, NO traducir)
    text = re.sub(r"(#[A-Z][a-z]+#)", lambda m: _save_ph(m, ph_map, "GV"), text)

    # 3) Proteger códigos de color (ej: #GOLD#, #LIGHT_GREEN#, #ffff00#)
    #    Incluye _ para tags compuestas como #LIGHT_GREEN#
    text = re.sub(r"(#[A-Z_]+#)", lambda m: _save_ph(m, ph_map, "CL"), text)
    text = re.sub(r"(#[a-fA-F0-9]{6}#)", lambda m: _save_ph(m, ph_map, "CH"), text)

    # 4) Proteger <etiquetas> (ej: <color>, <bold>, <i>)
    text = re.sub(r"<[^>]+>", lambda m: _save_ph(m, ph_map, "TG"), text)

    # 5) Proteger [[referencias]] (ej: [[wiki:...]], [[talent:...]])
    text = re.sub(r"\[\[[^\]]*\]\]", lambda m: _save_ph(m, ph_map, "DB"), text)

    # 6) Proteger {{expresiones lua}} (ej: {{x+1}})
    text = re.sub(
        r"\{\{.*?\}\}", lambda m: _save_ph(m, ph_map, "LU"), text, flags=re.DOTALL
    )

    # 7) Proteger %d, %s, %f (format specifiers) - mejora sobre ffNff
    text = re.sub(r"%[0-9+.\-]*[sdf]", lambda m: _save_ph(m, ph_map, "FS"), text)

    return text, ph_map


def restore_placeholders(text, ph_map):
    """
    Restaura todos los placeholders en el texto traducido.
    Además, limpia espacios extra que LibreTranslate añade alrededor
    de los placeholders al restaurarlos.
    """
    for ph, orig in ph_map.items():
        # LT a veces se come el § o lo duplica
        text = text.replace(ph, orig)
        # Intentar variantes si LT modificó el placeholder
        bare_key = ph.replace("\u00a7", "")
        if bare_key in text:
            text = text.replace(bare_key, orig)

    # Limpiar espacios extra alrededor de placeholders restaurados
    # Caso: "  %s" → " %s" (doble espacio antes)
    text = re.sub(r"  (%[0-9+.\-]*[sdf])", r" \1", text)
    # Caso: " %s  " → " %s " (doble espacio después)
    text = re.sub(r"(%[0-9+.\-]*[sdf])  ", r"\1 ", text)

    return text


def apply_post_process(text):
    """Aplica las correcciones post-traducción desde terms.POST_PROCESS."""
    try:
        from terms import POST_PROCESS

        for pattern, replacement in POST_PROCESS:
            try:
                if callable(replacement):
                    text = re.sub(pattern, replacement, text)
                else:
                    text = re.sub(pattern, replacement, text)
            except Exception as e:
                print(f"[POST_PROCESS] Error con patrón {pattern!r}: {e}")
    except ImportError:
        pass  # Si no hay POST_PROCESS, continuar sin cambios
    except Exception as e:
        print(f"[POST_PROCESS] Error general: {e}")
    return text


# ---------------------------------------------------------------------------
# Traductor principal
# ---------------------------------------------------------------------------


class LibreTranslator:
    """Traductor usando diccionario + LibreTranslate via API REST."""

    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.cache = {}
        # Cargar diccionario de términos forzados
        try:
            from terms import FORCED_TERMS, NO_TRANSLATE

            self.forced = FORCED_TERMS
            self.no_translate = NO_TRANSLATE
        except ImportError:
            self.forced = {}
            self.no_translate = set()
        print(
            f"[AGENT] Usando LibreTranslate en {url} "
            f"(+{len(self.forced)} terminos forzados, "
            f"+{len(self._count_post_process())} reglas post-process)"
        )

    def _count_post_process(self):
        try:
            from terms import POST_PROCESS

            return POST_PROCESS
        except (ImportError, AttributeError):
            return []

    def translate(self, text):
        """Traduce un texto usando diccionario + LibreTranslate + POST_PROCESS."""
        if not text or text.strip() == "":
            return text

        # Cache
        if text in self.cache:
            return self.cache[text]

        # Diccionario forzado primero
        if text in self.forced:
            self.cache[text] = self.forced[text]
            return self.forced[text]

        # No traducir (nombre propio sensible a mayusculas)
        if text in self.no_translate:
            self.cache[text] = text
            return text
        if text.lower() in self.no_translate:
            self.cache[text] = text
            return text

        # Para frases compuestas cortas: traducir palabra por palabra si es posible
        words = text.split()
        if len(words) > 1 and len(words) <= 8:
            translated_words = []
            all_dictionary = True
            for w in words:
                w_clean = w.strip(".,!?;:'\"")
                if w_clean in self.forced:
                    translated_words.append(self.forced[w_clean])
                elif (
                    w_clean in self.no_translate or w_clean.lower() in self.no_translate
                ):
                    translated_words.append(w_clean)
                else:
                    all_dictionary = False
                    break
            if all_dictionary:
                result = " ".join(translated_words)
                self.cache[text] = result
                return result

        # Proteger placeholders antes de enviar a LT
        text_clean, ph_map = protect_patterns(text)

        # Llamar a LibreTranslate
        try:
            data = urllib.parse.urlencode(
                {"q": text_clean, "source": "en", "target": "es"}
            ).encode()
            req = urllib.request.Request(
                f"{self.url}/translate",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read())["translatedText"]
        except Exception as e:
            print(f"[AGENT] Error en traduccion: {e}")
            self.cache[text] = text
            return text

        # Restaurar placeholders
        result = restore_placeholders(result, ph_map)

        # Aplicar POST_PROCESS (usted→tú, términos, etc.)
        result = apply_post_process(result)

        # Si el resultado es idéntico al original (o solo cambió casing), cachear igual
        self.cache[text] = result
        return result


# Para pruebas
if __name__ == "__main__":
    t = LibreTranslator()

    # Tests básicos
    tests = [
        "Arcane Combat",
        "Acid Breath",
        "Temporal Shield",
        "Flame",
        "You have a chance to deal 50% damage to your target.",
        "@Source@ hits @Target@ for 50 damage!",
        "You can use this talent once per turn.",
        "Increases your physical power by 10.",
        "Your willpower affects the duration.",
        "You are stunned for 3 turns.",
    ]

    print("\n=== PRUEBAS DE TRADUCCION ===")
    for test in tests:
        trans = t.translate(test)
        marker = " ✓" if trans != test else " ✗"
        if trans != test:
            print(f"  EN: {test}")
            print(f"  ES: {trans}{marker}")
            print()

    # Probar POST_PROCESS específicamente
    print("\n=== PRUEBAS POST_PROCESS (usted→tú) ===")
    usted_tests = [
        "You can use this talent",
        "You have a chance",
        "Your physical power",
        "You are affected by",
    ]
    for test in usted_tests:
        # Simular lo que LT devolvería con "usted"
        fake_lt = (
            test.replace("You", "Usted").replace("your", "su").replace("Your", "Su")
        )
        fake_lt = (
            fake_lt.replace("have", "tiene")
            .replace("use", "usa")
            .replace("are", "está")
        )
        fixed = apply_post_process(fake_lt)
        print(f"  ANTES: {fake_lt}")
        print(f"  DESP:  {fixed}")
        print()
