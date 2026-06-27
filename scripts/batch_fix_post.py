#!/usr/bin/env python3
"""
Aplica POST_PROCESS a TODAS las traducciones existentes en los archivos split.
NO re-traduce, solo aplica correcciones regex (usted→tú, spanglish, etc.)
Es rápido porque no llama a LibreTranslate.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))
from terms import POST_PROCESS

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"

# Compilar todos los patrones POST_PROCESS una sola vez
COMPILED = []
for pattern, replacement in POST_PROCESS:
    try:
        if callable(replacement):
            compiled = re.compile(pattern)
            COMPILED.append((compiled, replacement))
        else:
            compiled = re.compile(pattern)
            COMPILED.append((compiled, replacement))
    except re.error as e:
        print(f"  [WARN] Patron invalido: {pattern[:50]}: {e}")


def apply_post_process_to_translation(text):
    """Aplica POST_PROCESS a un texto."""
    for compiled, replacement in COMPILED:
        if callable(replacement):
            text = compiled.sub(replacement, text)
        else:
            text = compiled.sub(replacement, text)
    return text


def process_file(filepath, dry_run=False):
    """Procesa un archivo split y aplica POST_PROCESS a todas las traducciones."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changes = 0

    def fix_translation(m):
        nonlocal changes
        full = m.group(0)
        original = m.group(1)
        translation = m.group(2)
        type_ = m.group(3)

        new_trans = apply_post_process_to_translation(translation)
        if new_trans != translation:
            changes += 1
            return f't("{original}", "{new_trans}", "{type_}")'
        return full

    new_content = re.sub(
        r't\("([^"]*)",\s*"([^"]*)",\s*"([^"]*)"\)',
        fix_translation,
        content,
    )

    if changes > 0 and not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return changes


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print(f"  BATCH FIX POST - Aplicando POST_PROCESS a traducciones existentes")
    print(f"  {len(COMPILED)} patrones compilados{' (SIMULACION)' if dry_run else ''}")
    print("=" * 60)

    total_changes = 0
    total_files = 0

    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        changes = process_file(fpath, dry_run)
        if changes > 0:
            rel_path = fpath.relative_to(SPLIT_DIR)
            print(f"  {'[SIM]' if dry_run else '  ✓'} {rel_path}: {changes} fixes")
            total_changes += changes
            total_files += 1

    print(f"\n  📊 TOTAL: {total_files} archivos, {total_changes} correcciones")
    if dry_run:
        print("\n  💡 Ejecuta sin --dry-run para aplicar")
    else:
        print("\n  💡 Siguiente: python3 scripts/build_addon.py --package")


if __name__ == "__main__":
    main()
