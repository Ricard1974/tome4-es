#!/usr/bin/env python3
"""
Fix: Restaura format specifiers perdidos en traducciones de archivos split.
Para cada t() donde la traducción perdió %d, %s o %0.2f, los añade al final.
Esto evita errores de Lua (crash por mismatch de argumentos).
"""

import re
from pathlib import Path

SPLIT_DIR = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"

T_PATTERN = re.compile(
    r"t\(\s*"
    r'("[^"\\]*(?:\\.?[^"\\]*)*")'  # orig
    r"\s*,\s*"
    r'("[^"\\]*(?:\\.?[^"\\]*)*")'  # trans
    r"\s*,\s*"
    r'("[^"\\]*(?:\\.?[^"\\]*)*")'  # ctx
    r"\s*\)"
)


def fmt_specifiers(s):
    """Extrae especificadores de formato (%d, %s, %0.2f, etc.) de un string."""
    return re.findall(r"%[0-9.]*[dfs]", s)


def process_file(fpath):
    """Procesa un archivo .lua, arreglando format specifiers en t() calls."""
    original_content = fpath.read_text("utf-8")
    content = original_content
    fixes = 0

    for m in T_PATTERN.finditer(content):
        orig_str = m.group(1)
        trans_str = m.group(2)
        ctx_str = m.group(3)

        orig_raw = orig_str[1:-1]
        trans_raw = trans_str[1:-1]
        ctx_raw = ctx_str[1:-1]

        orig_fmt = fmt_specifiers(orig_raw)
        trans_fmt = fmt_specifiers(trans_raw)

        if len(orig_fmt) == len(trans_fmt):
            continue
        if len(orig_fmt) < len(trans_fmt):
            continue

        # Missing specifiers - append at end of translation
        missing = orig_fmt[len(trans_fmt) :]
        fixed_trans = trans_raw + "".join(" " + f for f in missing)

        # Escapar el string para Lua
        escaped = fixed_trans.replace("\\", "\\\\").replace('"', '\\"')

        old = content[m.start(2) : m.end(2)]
        new = f'"{escaped}"'
        content = content[: m.start(2)] + new + content[m.end(2) :]
        fixes += 1

    if fixes > 0:
        fpath.write_text(content, "utf-8")
    return fixes


def main():
    print("=" * 60)
    print("  FIX FORMAT SPECIFIERS (split files)")
    print("=" * 60)

    if not SPLIT_DIR.exists():
        print(f"  ERROR: {SPLIT_DIR} no encontrado")
        return

    files = sorted(SPLIT_DIR.rglob("*.lua"))
    total_fixes = 0
    fixed_files = 0

    for fpath in files:
        fixes = process_file(fpath)
        if fixes > 0:
            rel = fpath.relative_to(SPLIT_DIR)
            print(f"  ✏️  [{rel}] {fixes} specifiers restaurados")
            total_fixes += fixes
            fixed_files += 1

    print()
    print(
        f"  📊 {fixed_files} archivos modificados, {total_fixes} specifiers restaurados"
    )
    print(f"  ✅ Hecho")


if __name__ == "__main__":
    main()
