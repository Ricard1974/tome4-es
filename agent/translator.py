"""
Traductor para ToME4-es usando LibreTranslate (Docker local).
API REST en http://localhost:5000
"""

import re
import json
import urllib.request
import urllib.parse


class LibreTranslator:
    """Traductor usando LibreTranslate via API REST."""

    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.cache = {}
        print(f"[AGENT] Usando LibreTranslate en {url}")

    def translate(self, text):
        """Traduce un texto usando LibreTranslate."""
        if not text or text.strip() == "":
            return text

        # Cache
        if text in self.cache:
            return self.cache[text]

        # Preservar placeholders
        ph_map = {}
        ph_counter = [0]

        def save_ph(m):
            ph_map[f"__PH{ph_counter[0]}__"] = m.group(0)
            ph_counter[0] += 1
            return f"__PH{ph_counter[0] - 1}__"

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

        # Restaurar placeholders
        for ph, orig in ph_map.items():
            result = result.replace(ph, orig)

        self.cache[text] = result
        return result


# Para pruebas
if __name__ == "__main__":
    t = LibreTranslator()
    tests = ["Arcane Combat", "Acid Breath", "Temporal Shield", "Flame"]
    for test in tests:
        print(f"  {test:30} -> {t.translate(test)}")
