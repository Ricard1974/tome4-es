#!/usr/bin/env python3
"""
Fix spanglish en traducciones: reemplaza palabras inglesas
que se colaron en textos visibles al jugador.
"""

import re
from pathlib import Path

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"

# Patrones de spanglish -> español
# Solo palabras completas (rodeadas de espacios/puntuación)
# y solo en textos ya traducidos (orig != trans)
REPLACEMENTS = [
    # Efectos de estado
    (r"\bdaze\b", "aturdimiento"),
    (r"\bDaze\b", "Aturdimiento"),
    (r"\bstun\b", "aturdimiento"),
    (r"\bStun\b", "Aturdimiento"),
    (r"\bblind\b(?! block)", "ceguera"),
    (r"\bBlind\b(?! block)", "Ceguera"),
    (r"\bslow\b(?!ly)(?!ness)", "ralentización"),
    (r"\bSlow\b(?!ly)(?!ness)", "Ralentización"),
    (r"\bhaste\b", "celeridad"),
    (r"\bHaste\b", "Celeridad"),
    # Atributos
    (r"\bCunning\b(?!%)", "Astucia"),
    (r"\bDexterity\b", "Destreza"),
    (r"\bMagic\b(?! )", "Magia"),
    # Turn
    (r"(\d+) turn\b", r"\1 turnos"),
    (r"(\d+) turns\b", r"\1 turnos"),
    (r"turn \(", "turno ("),
    (r"turn\.", "turno."),
    (r"turn,", "turno,"),
    # Misc
    (r"\battack\b", "ataque"),
    (r"\bAttack\b", "Ataque"),
    (r"\bweapon\b", "arma"),
    (r"\bWeapon\b", "Arma"),
]

# Excepciones: strings que NO deben modificarse
EXCEPTIONS = [
    "Wave of Power",
    "Auto Attack",
]


def has_formatting(s):
    """Check if string has color tags or format specifiers."""
    return bool(re.search(r"#[A-Z_#{}]|%[0-9.]*[dfs]", s))


def process_file(fpath):
    """Apply spanglish fixes to a split file, only to translated strings."""
    content = fpath.read_text("utf-8")
    modified = False

    lines = content.split("\n")
    for i, line in enumerate(lines):
        # Match t("orig", "trans", "ctx")
        m = re.match(
            r'(.*?)t\(\s*("[^"]*")\s*,\s*("[^"]*")\s*,\s*("[^"]*")\s*\)(.*)', line
        )
        if not m:
            continue

        prefix = m.group(1)
        orig_str = m.group(2)
        trans_str = m.group(3)
        ctx_str = m.group(4)
        suffix = m.group(5)

        orig = orig_str[1:-1]
        trans = trans_str[1:-1]
        ctx = ctx_str[1:-1]

        if orig == trans and len(orig) > 2:
            continue

        # Skip if it's an exception
        if any(exc in trans for exc in EXCEPTIONS):
            continue

        # Apply replacements
        new_trans = trans
        for pattern, replacement in REPLACEMENTS:
            new_trans = re.sub(pattern, replacement, new_trans)

        if new_trans != trans:
            # Escape for Lua
            escaped = new_trans.replace("\\", "\\\\").replace('"', '\\"')
            new_line = f'{prefix}t({orig_str}, "{escaped}", {ctx_str}){suffix}'
            lines[i] = new_line
            modified = True

    if modified:
        fpath.write_text("\n".join(lines), "utf-8")
    return modified


def main():
    print("=" * 60)
    print("  FIX SPANGLISH")
    print("=" * 60)

    files = sorted(SPLIT_DIR.rglob("*.lua"))
    fixed = 0
    fixed_files = 0

    for fpath in files:
        if process_file(fpath):
            rel = fpath.relative_to(SPLIT_DIR)
            print(f"  ✏️  {rel}")
            fixed_files += 1
            # Count replacements approximately
            fixed += 1  # We'll get exact count from diff later

    print(f"\n  📊 {fixed_files} archivos modificados")
    print("  ✅ Hecho")


if __name__ == "__main__":
    main()
