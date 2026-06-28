#!/usr/bin/env python3
"""
Merge: une los archivos de secciones divididos de vuelta a mod-tome.lua

Uso: python3 scripts/merge_sections.py

El script busca archivos en translations/es/mod-tome-split/ y los mergea
de vuelta a translations/es/mod-tome.lua, respetando el formato original
de Translation Toolbox.
"""

import re
from pathlib import Path
import sys

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
SPLIT_DIR = TRANS_DIR / "mod-tome-split"
OUTPUT_FILE = TRANS_DIR / "mod-tome.lua"
BACKUP_FILE = TRANS_DIR / "mod-tome.lua.bak"

# =============================================================================
# ORDEN DE LAS SECCIONES (por categoría)
# Secciones principales primero, luego alfabético
# =============================================================================
SECTION_ORDER = [
    # Archivos de módulo (init, load)
    "mod/init.lua",
    "mod/load.lua",
    "mod/mod.lua",
    # Birth (creación de personaje)
    "data/birth/",
    "data/birth/races/",
    "data/birth/classes/",
    # Recursos
    "data/resources.lua",
    "data/damage_types.lua",
    "data/ingredients.lua",
    # Talentos
    "data/talents/",
    "data/talents.lua",
    "data/timed_effects/",
    "data/timed_effects.lua",
    # General
    "data/general/",
    "data/general/npcs/",
    "data/general/objects/",
    "data/general/grids/",
    "data/general/events/",
    "data/general/traps/",
    "data/general/encounters/",
    "data/general/stores.lua",
    # Chats y diálogos
    "data/chats/",
    # Zonas
    "data/zones/",
    # Mapas
    "data/maps/",
    "data/maps/towns/",
    "data/maps/vaults/",
    "data/maps/wilderness.lua",
    "data/mapscripts/",
    # Clases del módulo
    "mod/class/",
    "mod/dialogs/",
    "mod/ai/",
    # Contenido del juego
    "data/achievements/",
    "data/quests/",
    "data/lore/",
    "data/texts/",
    # Misc
    "data/keybinds/",
    "data/factions.lua",
    "data/rooms/",
    "data/wda.lua",
    "data/calendar_allied.lua",
    "data/calendar_dwarf.lua",
]


def get_section_name(filepath):
    """Obtiene el nombre de sección a partir de la ruta del archivo."""
    rel = filepath.relative_to(SPLIT_DIR)
    return f"mod-tome/{rel}"


def sort_key(filepath):
    """Ordena los archivos según SECTION_ORDER."""
    rel = str(filepath.relative_to(SPLIT_DIR))

    for i, prefix in enumerate(SECTION_ORDER):
        if rel.startswith(prefix) or rel == prefix:
            return (i, rel)

    # Si no está en el orden definido, va al final ordenado alfabéticamente
    return (len(SECTION_ORDER), rel)


def merge_sections():
    """Mergea todos los archivos de secciones de vuelta a mod-tome.lua."""
    # Backup del archivo actual
    if OUTPUT_FILE.exists():
        import shutil

        shutil.copy2(OUTPUT_FILE, BACKUP_FILE)
        print(f"  📋 Backup: {BACKUP_FILE}")

    # Encontrar todos los archivos .lua
    files = sorted(SPLIT_DIR.rglob("*.lua"), key=sort_key)

    total_calls = 0
    sections = []

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extraer solo las líneas t()
        t_calls = re.findall(
            r't\((\"(?:[^"\\]|\\.)*\",\s*\"(?:[^"\\]|\\.)*\",\s*\"(?:[^"\\]|\\.)*\")\)',
            content,
        )
        if not t_calls:
            continue

        section_name = get_section_name(fpath)
        total_calls += len(t_calls)
        sections.append((section_name, t_calls))

    # Escribir el archivo mergeado
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, (section_name, t_calls) in enumerate(sections):
            if i > 0:
                f.write("\n")
            f.write("-" * 48 + "\n")
            f.write(f'-- section "{section_name}"')
            f.write("\n\n")
            f.write("-- new text\n")

            for t_call in t_calls:
                f.write(f"t({t_call})\n")

    return len(sections), total_calls


def main():
    print("=" * 60)
    print("  MERGE DE SECCIONES → mod-tome.lua")
    print("=" * 60)

    if not SPLIT_DIR.exists():
        print(f"  ERROR: {SPLIT_DIR} no encontrado")
        print("  Ejecuta primero: python3 scripts/split_sections.py")
        sys.exit(1)

    files = list(SPLIT_DIR.rglob("*.lua"))
    if not files:
        print(f"  ERROR: No hay archivos en {SPLIT_DIR}")
        sys.exit(1)

    print(f"  📁 {len(files)} archivos encontrados en {SPLIT_DIR}")

    sections, total = merge_sections()
    print(f"  ✅ Merge completado: {sections} secciones, {total} cadenas")
    print(f"  📄 {OUTPUT_FILE}")

    # Verificar que el número de cadenas es similar al original
    import subprocess

    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "count_translations.py")],
        capture_output=True,
        text=True,
    )
    print()
    print(result.stdout)
    print()


if __name__ == "__main__":
    main()
