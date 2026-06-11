#!/usr/bin/env python3
"""
Divide mod-tome.lua en archivos independientes por sección.
Cada sección se guarda en su propia ruta bajo translations/es/mod-tome-split/.

Uso: python3 scripts/split_sections.py
"""

import re
import os
from pathlib import Path
import sys

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
MOD_TOME_FILE = TRANS_DIR / "mod-tome.lua"
OUTPUT_DIR = TRANS_DIR / "mod-tome-split"


def split_mod_tome():
    """Divide mod-tome.lua en archivos por sección."""
    with open(MOD_TOME_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Dividir por el separador de secciones
    # Cada sección empieza con 48 guiones + section "ruta"
    blocks = re.split(r"^-{48}", content, flags=re.MULTILINE)

    sections_found = 0
    sections_ignored = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Buscar el nombre de la sección
        section_match = re.search(r'^section\s+"([^"]+)"', block, re.MULTILINE)
        if not section_match:
            continue

        section_path = section_match.group(1)

        # Solo procesar secciones de mod-tome
        if not section_path.startswith("mod-tome/"):
            continue

        # Quitar el prefijo "mod-tome/"
        rel_path = section_path[len("mod-tome/") :]

        # Construir la ruta del archivo de salida
        output_file = OUTPUT_DIR / rel_path

        # Extraer el contenido de la sección (todo después de la línea de section)
        section_content = block[section_match.end() :].strip()

        # Si solo tiene "-- new text" o "-- translated text" y "--[==[ ... ]--]==]", extraer t() calls
        # Buscar las t() calls reales
        t_calls = re.findall(r't\(("[^"]*",\s*"[^"]*",\s*"[^"]*")\)', section_content)

        if not t_calls:
            sections_ignored += 1
            continue

        # Crear directorio de salida
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Escribir el archivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"-- {section_path}\n")
            f.write(f"-- Total: {len(t_calls)} cadenas\n")
            f.write(
                f"-- Estado: {'✅ Traducido' if any('traducido' in block or 'translated' in block for block in [section_content]) else '⏳ Pendiente'}\n"
            )
            f.write(f"-- Ultima actualizacion: --\n")
            f.write(f"-- Traductor: --\n")
            f.write("\n")
            for t_call in t_calls:
                f.write(f"t({t_call})\n")
            f.write("\n")

        sections_found += 1

    return sections_found, sections_ignored


def create_category_files():
    """
    Opcional: crea archivos de categoría que agrupan secciones relacionadas.
    """
    categories = {
        "achievements": "data/achievements",
        "birth_races": "data/birth/races",
        "birth_classes": "data/birth/classes",
        "chats": "data/chats",
        "damage_types": "data/damage_types",
        "ingredients": "data/ingredients",
        "lore": "data/lore",
        "npcs": "data/general/npcs",
        "objects": "data/general/objects",
        "quests": "data/quests",
        "talents_spells": "data/talents/spells",
        "talents_techniques": "data/talents/techniques",
        "talents_psionic": "data/talents/psionic",
        "talents_gifts": "data/talents/gifts",
        "talents_chronomancy": "data/talents/chronomancy",
        "talents_cursed": "data/talents/cursed",
        "talents_celestial": "data/talents/celestial",
        "talents_corruptions": "data/talents/corruptions",
        "talents_cunning": "data/talents/cunning",
        "talents_uber": "data/talents/uber",
        "talents_misc": "data/talents/misc",
        "talents_undeads": "data/talents/undeads",
        "timed_effects_magical": "data/timed_effects/magical",
        "timed_effects_physical": "data/timed_effects/physical",
        "timed_effects_mental": "data/timed_effects/mental",
        "timed_effects_other": "data/timed_effects/other",
        "zones": "data/zones",
        "grids": "data/general/grids",
        "traps": "data/general/traps",
        "events": "data/general/events",
        "encounters": "data/general/encounters",
        "egos": "data/general/objects/egos",
        "random_artifacts": "data/general/objects/random-artifacts",
    }

    # Las categorías se crean automáticamente con la estructura de directorios
    return categories


def print_stats():
    """Muestra estadísticas de las secciones divididas."""
    total_files = 0
    total_strings = 0
    by_category = {}

    for fpath in sorted(OUTPUT_DIR.rglob("*.lua")):
        rel = fpath.relative_to(OUTPUT_DIR)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        t_count = len(re.findall(r"t\(", content))
        total_files += 1
        total_strings += t_count

        # Categorizar
        parts = str(rel).split("/")
        if len(parts) >= 2:
            cat = f"{parts[0]}/{parts[1]}"
        else:
            cat = parts[0]
        by_category[cat] = by_category.get(cat, 0) + t_count

    print(f"\n📊 ESTADÍSTICAS DEL SPLIT")
    print(f"   Archivos: {total_files}")
    print(f"   Cadenas:  {total_strings}")
    print()
    print("   Por categoría:")
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"     {cat:<45} {count:>5} cadenas")


def main():
    print("=" * 60)
    print("  DIVIDIENDO SECCIONES DE mod-tome.lua")
    print("=" * 60)

    if not MOD_TOME_FILE.exists():
        print(f"  ERROR: {MOD_TOME_FILE} no encontrado")
        sys.exit(1)

    # Crear directorio de salida
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Limpiar split anterior (opcional)
    import shutil

    for item in OUTPUT_DIR.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    sections, ignored = split_mod_tome()
    print(f"\n  ✅ {sections} secciones divididas en {OUTPUT_DIR}")
    print(f"  ⏩ {ignored} secciones vacías ignoradas")

    print_stats()
    print()


if __name__ == "__main__":
    main()
