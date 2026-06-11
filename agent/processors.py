"""
Procesadores de archivos para traducción automática.
"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TRANS_DIR = BASE_DIR / "translations" / "es"


def get_untranslated_talent_names():
    """Extrae todos los nombres de talentos sin traducir."""
    untranslated = []
    for f in sorted((TRANS_DIR / "mod-tome-split" / "data" / "talents").rglob("*.lua")):
        with open(f, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r't\("([^"]+)",\s*"\1",\s*"talent name"\)', line)
                if m:
                    untranslated.append((f, m.group(1)))
    return untranslated


def process_talents(translator, dry_run=False):
    """Traduce TODOS los nombres de talentos sin traducir."""
    items = get_untranslated_talent_names()
    unique_texts = list(set(text for _, text in items))

    print(f"\n[AGENT] Talentos: {len(items)} sin traducir ({len(unique_texts)} únicos)")

    if dry_run:
        print("  (modo simulación - no se aplicarán cambios)")
        return 0, 0

    # Traducir textos únicos
    trans_map = {}
    for text in unique_texts:
        trans = translator.translate(text)
        if trans and trans != text:
            trans_map[text] = trans

    # Aplicar traducciones a los archivos
    changes = 0
    files_modified = set()

    for fpath, text in items:
        if text not in trans_map:
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        trans = trans_map[text]
        old = f't("{text}", "{text}", "talent name")'
        new = f't("{text}", "{trans}", "talent name")'

        if old in content:
            content = content.replace(old, new)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            changes += 1
            files_modified.add(fpath)

    print(f"  Archivos modificados: {len(files_modified)}")
    print(f"  Traducciones aplicadas: {changes}")
    return changes, len(files_modified)


def process_objects(translator, dry_run=False):
    """Traduce nombres de objetos sin traducir."""
    items = []
    for f in sorted(
        (TRANS_DIR / "mod-tome-split" / "data" / "general" / "objects").rglob("*.lua")
    ):
        with open(f, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r't\("([^"]+)",\s*"\1",\s*"entity name"\)', line)
                if m:
                    items.append((f, m.group(1)))

    unique_texts = list(set(text for _, text in items))
    print(f"\n[AGENT] Objetos: {len(items)} sin traducir ({len(unique_texts)} únicos)")

    if dry_run:
        return 0, 0

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
        old = f't("{text}", "{text}", "entity name")'
        new = f't("{text}", "{trans}", "entity name")'

        if old in content:
            content = content.replace(old, new)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            changes += 1
            files_modified.add(fpath)

    print(f"  Archivos modificados: {len(files_modified)}")
    print(f"  Traducciones aplicadas: {changes}")
    return changes, len(files_modified)


if __name__ == "__main__":
    # Test rápido
    items = get_untranslated_talent_names()
    print(f"Total talent names sin traducir: {len(items)}")
    print(f"Únicos: {len(set(t for _, t in items))}")
    for _, t in items[:20]:
        print(f"  {t}")
