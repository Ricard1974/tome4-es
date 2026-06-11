#!/usr/bin/env python3
"""
Extrae todas las cadenas únicas de los archivos de traducción.
Genera un archivo JSON con todas las cadenas para su traducción.

Uso: python3 scripts/extract_strings.py
"""

import re
import json
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
OUTPUT = Path(__file__).parent.parent / "translations" / "all_strings.json"


def extract_strings():
    """Extrae todas las cadenas únicas de todos los archivos."""
    all_strings = {}
    file_strings = {}

    for fpath in sorted(TRANS_DIR.glob("*.lua")):
        if fpath.name in (
            "_t_append.lua",
            "_not_merged.lua",
            "i18n.log",
            "copy_files.py",
        ):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Buscar t("original", "original|traduccion", "tipo")
        pattern = r't\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)'
        strings_in_file = []

        for match in re.finditer(pattern, content):
            original = match.group(1)
            current_trans = match.group(2)
            type_ = match.group(3)

            # Solo incluir si está sin traducir
            if original == current_trans:
                if original not in all_strings:
                    all_strings[original] = {
                        "original": original,
                        "translation": None,
                        "type": type_,
                        "files": [],
                    }
                if fpath.name not in all_strings[original]["files"]:
                    all_strings[original]["files"].append(fpath.name)

        file_strings[fpath.name] = len(strings_in_file)

    return all_strings, file_strings


def main():
    all_strings, file_strings = extract_strings()

    # Guardar como JSON
    output = {
        "total": len(all_strings),
        "strings": list(all_strings.values()),
        "by_file": file_strings,
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=1)

    print(f"  Total cadenas únicas: {len(all_strings)}")
    print(f"  Por archivo:")
    for fname, count in sorted(file_strings.items(), key=lambda x: -x[1]):
        print(f"    {fname}: {count}")
    print(f"\n  Guardado en: {OUTPUT}")
    print()


if __name__ == "__main__":
    main()
