#!/usr/bin/env python3
"""
Contador de progreso de traducción para ToME4-es.
Analiza los archivos generados por Translation Toolbox y muestra estadísticas.

Uso: python3 scripts/count_translations.py [--detallado]
"""

import re
import sys
from pathlib import Path

# Ruta a los archivos de traducción
TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"


def analyze_file(filepath):
    """Analiza un archivo de traducción y devuelve estadísticas."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Contar secciones
    sections = re.findall(r'^section\s+"([^"]+)"', content, re.MULTILINE)

    # Contar entradas t() - pueden estar dentro o fuera de bloques --[==[
    re.findall(r't\(("[^"]*"\s*,\s*"[^"]*"\s*,\s*"[^"]*")\)', content)

    # Strings traducidos: fuera de bloques --[==[, o dentro de bloques marcados como "translated"
    translated = 0
    untranslated = 0

    # Dividir por secciones
    section_blocks = re.split(r"^-{48}", content, flags=re.MULTILINE)

    for block in section_blocks:
        if not block.strip():
            continue

        # Detectar si es "new text" o "translated text"

        # Encontrar todas las t() en este bloque
        t_calls = re.findall(r't\(("[^"]*"\s*,\s*"[^"]*"\s*,\s*"[^"]*")\)', block)

        for t_call in t_calls:
            # Extraer original y traducción
            match = re.match(r'"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"', t_call)
            if match:
                original = match.group(1)
                translated_text = match.group(2)

                # Si el texto traducido es diferente del original, está traducido
                if original != translated_text:
                    translated += 1
                else:
                    untranslated += 1
            else:
                untranslated += 1

    total = translated + untranslated
    pct = (translated / total * 100) if total > 0 else 0

    return {
        "file": filepath.name,
        "sections": len(sections),
        "total": total,
        "translated": translated,
        "untranslated": untranslated,
        "percentage": pct,
    }


def format_size(size):
    """Formatea tamaño de archivo."""
    for unit in ["B", "KB", "MB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def main():
    verbose = "--detallado" in sys.argv or "-v" in sys.argv

    if not TRANS_DIR.exists():
        print(f"Error: No se encuentra el directorio {TRANS_DIR}")
        print("Ejecuta primero la Translation Toolbox en el juego.")
        sys.exit(1)

    lua_files = sorted(TRANS_DIR.glob("*.lua"))
    if not lua_files:
        print(f"No se encontraron archivos .lua en {TRANS_DIR}")
        sys.exit(1)

    stats = []
    for fpath in lua_files:
        if fpath.name in ("_t_append.lua", "_not_merged.lua", "i18n.log"):
            continue
        stats.append(analyze_file(fpath))

    # Totales
    total_sections = sum(s["sections"] for s in stats)
    total_strings = sum(s["total"] for s in stats)
    total_translated = sum(s["translated"] for s in stats)
    total_untranslated = sum(s["untranslated"] for s in stats)
    total_pct = (total_translated / total_strings * 100) if total_strings > 0 else 0

    # Mostrar resultados
    print("=" * 65)
    print("  📊 PROGRESO DE TRADUCCIÓN — ToME4-es")
    print("=" * 65)
    print()

    # Tabla por archivo
    print(
        f"  {'Archivo':<25} {'Secciones':<10} {'Total':<8} {'Trad.':<8} {'Pend.':<8} {'%':<8}"
    )
    print(f"  {'-' * 25} {'-' * 10} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 8}")
    for s in stats:
        pct_str = f"{s['percentage']:.1f}%" if s["total"] > 0 else "-"
        print(
            f"  {s['file']:<25} {s['sections']:<10} {s['total']:<8} {s['translated']:<8} {s['untranslated']:<8} {pct_str:<8}"
        )

    print(f"  {'-' * 25} {'-' * 10} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 8}")
    print(
        f"  {'TOTAL':<25} {total_sections:<10} {total_strings:<8} {total_translated:<8} {total_untranslated:<8} {total_pct:.1f}%"
    )
    print()

    # Barra de progreso
    bar_width = 50
    filled = int(bar_width * total_pct / 100)
    bar = "█" * filled + "░" * (bar_width - filled)
    print(f"  [{bar}] {total_pct:.1f}%")
    print()

    # Detallado
    if verbose:
        print("  📋 DETALLE POR ARCHIVO:")
        print()
        for s in stats:
            if s["total"] > 0:
                print(f"    📄 {s['file']}")
                print(f"       Secciones: {s['sections']}")
                print(f"       Cadenas:   {s['total']}")
                print(f"       Traducidas: {s['translated']} ({s['percentage']:.1f}%)")
                print(f"       Pendientes: {s['untranslated']}")
                print()

    # Consejos
    print("  💡 CONSEJOS:")
    print("     Para traducir, edita los archivos en translations/es/")
    print("     Cambia el segundo parámetro de t() por la traducción:")
    print('       t("original", "TRADUCCIÓN", "tipo")')
    print()
    print("     Luego usa 'Rearrange translation files' en el juego")
    print("     para actualizar los archivos en ~/.t-engine/4.0/tome/user-i18n/es/")
    print()


if __name__ == "__main__":
    main()
