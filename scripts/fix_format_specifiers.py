#!/usr/bin/env python3
"""
Corrige format specifiers rotos en traducciones.

Cuando el número o tipo de %d/%s/%f difiere entre original y traducción,
revierte la traducción al original inglés para evitar crashes en el juego.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"


def get_specifiers(text):
    """Extrae format specifiers en orden: [(spec, type), ...]"""
    specs = []
    for m in re.finditer(r"(?<!%)%[0-9+.\-]*([dsf])", text):
        specs.append((m.group(0), m.group(1)))
    return specs


def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print(f"  CORRECTOR DE FORMAT SPECIFIERS{' (SIMULACION)' if dry_run else ''}")
    print("=" * 60)

    total_fixed = 0
    total_files = 0
    file_fixes = defaultdict(list)

    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        with open(fpath, encoding="utf-8") as f:
            content = f.read()
            original_content = content

        for m in re.finditer(r't\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', content):
            full = m.group(0)
            original = m.group(1)
            translation = m.group(2)
            type_ = m.group(3)

            # Extraer format specifiers
            orig_specs = get_specifiers(original)
            trans_specs = get_specifiers(translation)

            # Verificar que coincidan número y tipo
            if len(orig_specs) != len(trans_specs):
                # Diferente número: revertir a inglés
                old_pattern = f't("{original}", "{translation}", "{type_}")'
                new_pattern = f't("{original}", "{original}", "{type_}")'
                if old_pattern in content:
                    content = content.replace(old_pattern, new_pattern)
                    file_fixes[fpath].append(
                        (original[:40], translation[:40], "count_mismatch")
                    )
                continue

            # Verificar tipos en el mismo orden
            for i, ((o_spec, o_type), (t_spec, t_type)) in enumerate(
                zip(orig_specs, trans_specs)
            ):
                if o_type != t_type:
                    old_pattern = f't("{original}", "{translation}", "{type_}")'
                    new_pattern = f't("{original}", "{original}", "{type_}")'
                    if old_pattern in content:
                        content = content.replace(old_pattern, new_pattern)
                        file_fixes[fpath].append(
                            (
                                original[:40],
                                translation[:40],
                                f"type_mismatch:{o_type}->{t_type}",
                            )
                        )
                    break

        if content != original_content and not dry_run:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    for fpath, fixes in sorted(file_fixes.items()):
        rel = fpath.relative_to(SPLIT_DIR)
        print(f"  {'[SIM]' if dry_run else '  ✓'} {rel}: {len(fixes)} revertidas")
        total_fixed += len(fixes)
        total_files += 1

    print(
        f"\n  📊 TOTAL: {total_files} archivos, {total_fixed} cadenas revertidas a inglés"
    )

    if dry_run:
        print("\n  💡 Ejecuta sin --dry-run para aplicar")

    return total_fixed


if __name__ == "__main__":
    main()
