"""
Traductor para ToME4-es usando LibreTranslate (Docker local).
API REST en http://localhost:5000
"""

import re
import json
import urllib.request
import urllib.parse


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
            f"[AGENT] Usando LibreTranslate en {url} (+{len(self.forced)} terminos forzados)"
        )

    def translate(self, text):
        """Traduce un texto usando diccionario + LibreTranslate."""
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

        # Para frases compuestas: traducir palabra por palabra si falla
        words = text.split()
        if len(words) > 1:
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

        # Preservar placeholders: reemplazar %s, %d, %f con marcadores ffNff
        ph_map = {}

        def save_ph(m):
            idx = len(ph_map)
            ph_map[f"ff{idx}ff"] = m.group(0)
            return f"ff{idx}ff"

        text_clean = re.sub(r"%[0-9.]*[sdf]", save_ph, text)

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

        # Restaurar placeholders: buscar ffNff y reemplazar con el original
        for ph, orig in ph_map.items():
            result = result.replace(ph, orig)

        # Si aun hay PH0, PH1, __PH0__ (de version anterior del traductor), arreglarlos
        # buscando en el texto original que placeholders hay y restaurandolos
        orig_phs = re.findall(r"%\d*\.?\d*[sdfd]", text)
        for i, ph in enumerate(orig_phs):
            for variant in [f"__PH{i}__", f"PH{i}", f" PH{i} ", f"  PH{i}  "]:
                if variant in result:
                    result = result.replace(variant, ph)

        self.cache[text] = result
        return result


# Para pruebas
if __name__ == "__main__":
    t = LibreTranslator()
    tests = ["Arcane Combat", "Acid Breath", "Temporal Shield", "Flame"]
    for test in tests:
        print(f"  {test:30} -> {t.translate(test)}")
