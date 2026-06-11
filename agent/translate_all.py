#!/usr/bin/env python3
"""
Agente de traduccion ligero para ToME4-es.
Sin descargas, basado en diccionario + reglas linguisticas.

Uso:
  python3 agent/translate_all.py              # Traduce todo
  python3 agent/translate_all.py --dry-run    # Simulacion
  python3 agent/translate_all.py --talents    # Solo talentos
"""

import re
import sys
from pathlib import Path

# Añadir agent al path
sys.path.insert(0, str(Path(__file__).parent))

from translator import LightTranslator
from terms import NO_TRANSLATE, FORCED_TERMS

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"


def get_untranslated_talent_names():
    """Extrae todos los nombres de talentos sin traducir."""
    items = []
    for f in sorted((TRANS_DIR / "mod-tome-split" / "data" / "talents").rglob("*.lua")):
        with open(f, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r't\("([^"]+)",\s*"\1",\s*"talent name"\)', line)
                if m:
                    items.append((f, m.group(1)))
    return items


def get_untranslated_objects():
    """Extrae nombres de objetos sin traducir."""
    items = []
    for f in sorted(
        (TRANS_DIR / "mod-tome-split" / "data" / "general" / "objects").rglob("*.lua")
    ):
        with open(f, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r't\("([^"]+)",\s*"\1",\s*"entity name"\)', line)
                if m:
                    items.append((f, m.group(1)))
    return items


def translate_items(items, translator, title, dry_run=False):
    """Traduce una lista de items."""
    unique_texts = list(set(text for _, text in items))
    print(f"\n=== {title}: {len(items)} sin traducir ({len(unique_texts)} unicos) ===")

    if dry_run:
        # Solo mostrar ejemplo
        for t in sorted(unique_texts)[:10]:
            trans = translator.translate(t)
            if trans != t:
                print(f"  {t[:40]:40} -> {trans}")
        if len(unique_texts) > 10:
            print(f"  ... y {len(unique_texts) - 10} mas")
        return 0

    trans_map = {}
    for text in unique_texts:
        trans = translator.translate(text)
        if trans and trans != text:
            trans_map[text] = trans

    changes = 0
    files_modified = set()

    for fpath, text in items:
        if text not in trans_map:
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        trans = trans_map[text]
        old = f't("{text}", "{text}",'
        new = f't("{text}", "{trans}",'

        if old in content:
            content = content.replace(old, new)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            changes += 1
            files_modified.add(fpath)

    print(f"  Archivos: {len(files_modified)}, Traducciones: {changes}")
    return changes


def main():
    dry_run = "--dry-run" in sys.argv
    only_talents = "--talents" in sys.argv or "-t" in sys.argv
    only_objects = "--objects" in sys.argv or "-o" in sys.argv

    mode = "[SIMULACION]" if dry_run else ""
    print(f"AGENTE DE TRADUCCION ToME4-es {mode}")

    translator = LightTranslator()
    total = 0

    if not only_objects:
        items = get_untranslated_talent_names()
        total += translate_items(items, translator, "Talentos", dry_run)

    if not only_talents:
        items = get_untranslated_objects()
        total += translate_items(items, translator, "Objetos", dry_run)

    print(f"\nTotal: {total} traducciones")
    if not dry_run:
        print("\nSiguiente paso:")
        print("  python3 scripts/build_addon.py --package")


if __name__ == "__main__":
    main()
