#!/usr/bin/env python3
"""
Re-traduce cadenas sin traducir (original==translation) que contienen spanglish.
Usa el pipeline mejorado con POST_PROCESS.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent / "agent"))
from translator import LibreTranslator

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"

# Patrones de spanglish comunes
SPANGLISH_RE = re.compile(
    r"\b(Strength|Dexterity|Constitution|Willpower|Cunning|"
    r"damage|melee|stamina|chance|weapon|armour|armor|ranged)\b"
)


def main():
    dry_run = "--dry-run" in sys.argv
    translator = LibreTranslator()

    print("=" * 60)
    print(f"  FIX UNTRANSLATED SPANGLISH{' (SIMULACION)' if dry_run else ''}")
    print("=" * 60)

    # 1) Encontrar todas las cadenas sin traducir con spanglish
    pending = []
    seen = set()

    for fpath in sorted(SPLIT_DIR.rglob("*.lua")):
        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        for m in re.finditer(r't\("([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\)', content):
            original, translation, type_ = m.group(1), m.group(2), m.group(3)

            if original != translation:
                continue
            if len(original) < 8:
                continue
            if not SPANGLISH_RE.search(original):
                continue
            if original in seen:
                continue
            seen.add(original)
            pending.append((fpath, original, type_))

    print(f"\n  Cadenas sin traducir con spanglish: {len(pending)}")
    if not pending:
        print("  ¡Nada que hacer!")
        return

    if dry_run:
        for fpath, orig, type_ in pending[:5]:
            rel = fpath.relative_to(SPLIT_DIR)
            print(f"    {rel}: {orig[:60]}")
        print(f"\n  Total: {len(pending)}")
        return

    # 2) Traducir textos únicos
    translations = {}
    for i, (fpath, original, type_) in enumerate(pending):
        trans = translator.translate(original)
        if trans and trans != original:
            translations[original] = trans
        if (i + 1) % 25 == 0:
            print(f"    Progreso: {i + 1}/{len(pending)}")

    print(f"\n  Traducciones generadas: {len(translations)}")

    # 3) Aplicar
    changes = 0
    file_changes = defaultdict(int)

    for fpath, original, type_ in pending:
        if original not in translations:
            continue
        trans = translations[original]

        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        old_pattern = f't("{original}", "{original}", "{type_}")'
        new_pattern = f't("{original}", "{trans}", "{type_}")'

        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            file_changes[fpath] += 1
            changes += 1

    print(f"\n  📊 Correcciones aplicadas: {changes}")
    print(f"  Archivos modificados: {len(file_changes)}")
    for fpath, count in sorted(file_changes.items(), key=lambda x: -x[1])[:10]:
        rel = fpath.relative_to(SPLIT_DIR)
        print(f"    {rel}: {count}")

    print(
        "\n  💡 Siguiente: scripts/batch_fix_post.py + scripts/build_addon.py --package"
    )


if __name__ == "__main__":
    main()
