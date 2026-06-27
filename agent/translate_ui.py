"""
Traduce cadenas de UI/menús/ayuda que NO tienen format specs (%d, %s, %f).
Actualiza engine.lua, mod-boot.lua y los archivos split en mod-tome-split/.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from translator import LibreTranslator

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"
ENGINE_FILE = Path(__file__).parent.parent / "translations" / "es" / "engine.lua"
BOOT_FILE = Path(__file__).parent.parent / "translations" / "es" / "mod-boot.lua"

try:
    from terms import NO_TRANSLATE, FORCED_TERMS
except ImportError:
    NO_TRANSLATE = set()
    FORCED_TERMS = {}


def has_format_specs(text):
    return bool(re.search(r"(?<!%)%[0-9+.\-]*[dsf]", text))


def should_translate(text):
    text_stripped = text.strip()
    if len(text_stripped) <= 2:
        return False
    if re.match(r"^[.,!?;:\-\s\[\]()]+$", text_stripped):
        return False
    if text_stripped in FORCED_TERMS:
        return False
    if text_stripped in NO_TRANSLATE:
        return False
    if text_stripped.lower() in NO_TRANSLATE:
        return False
    if has_format_specs(text_stripped):
        return False
    return True


def translate_file(filepath, translator):
    rel = filepath.relative_to(filepath.parent.parent.parent)
    content = filepath.read_text(encoding="utf-8")
    new_content = content
    fixed = 0

    pattern = re.compile(r't\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)')

    for m in pattern.finditer(content):
        orig = m.group(1)
        trans = m.group(2)
        type_ = m.group(3)

        if orig != trans:
            continue
        if not should_translate(orig):
            continue

        result = translator.translate(orig)
        if result and result != orig:
            old = m.group(0)
            new = f't("{orig}", "{result}", "{type_}")'
            new_content = new_content.replace(old, new, 1)
            so = orig[:60].replace("\n", " ")
            sr = result[:60].replace("\n", " ")
            print(f'    "{so}" → "{sr}"')
            fixed += 1

    if fixed > 0:
        filepath.write_text(new_content, encoding="utf-8")
        print(f"    → [{rel}] {fixed} traducidas\n")
    return fixed


def translate_directory(dirpath, translator):
    total = 0
    for fpath in sorted(dirpath.rglob("*.lua")):
        total += translate_file(fpath, translator)
    return total


def main():
    print("Inicializando traductor...\n")
    translator = LibreTranslator()
    total = 0

    print("\n=== engine.lua ===")
    total += translate_file(ENGINE_FILE, translator)

    print("\n=== mod-boot.lua ===")
    total += translate_file(BOOT_FILE, translator)

    print("\n=== mod-tome-split/ ===")
    total += translate_directory(SPLIT_DIR, translator)

    print(f"\n{'=' * 50}")
    print(f"Total traducidas: {total}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
