#!/usr/bin/env python3
"""
Script para construir el addon de traducción tome-spanish.
Convierte los archivos de Translation Toolbox a formato addon.

Uso:
  python3 scripts/build_addon.py              # Construye el addon
  python3 scripts/build_addon.py --package     # Además genera .teaa
"""

import os
import re
import shutil
import zipfile
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
TRANS_DIR = PROJECT_DIR / "translations" / "es"
ADDON_DIR = PROJECT_DIR / "tome-spanish"
LOCALE_DIR = ADDON_DIR / "data" / "locales"
ENGINE_LOCALE_DIR = LOCALE_DIR / "engine"

# Mapeo de archivos fuente a archivos destino en el addon
FILE_MAP = {
    "engine.lua": ENGINE_LOCALE_DIR / "es.lua",
    "mod-tome.lua": LOCALE_DIR / "es.lua",
    "mod-boot.lua": LOCALE_DIR / "es.lua",  # Se mergea con mod-tome
    "tome-addon-dev.lua": LOCALE_DIR / "es.lua",
    "tome-items-vault.lua": LOCALE_DIR / "es.lua",
    "tome-remote-designer.lua": LOCALE_DIR / "es.lua",
    "mod-example.lua": None,  # Ignorar
    "mod-example_realtime.lua": None,  # Ignorar
}


def extract_t_calls(content):
    """
    Extrae todas las llamadas t() del contenido.
    Busca t("original", "traducción", "tipo") dentro y fuera de bloques.
    """
    t_calls = []
    # Buscar todas las llamadas t()
    pattern = r't\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)'
    for match in re.finditer(pattern, content):
        original, translation, type_ = match.group(1), match.group(2), match.group(3)
        t_calls.append((original, translation, type_))
    return t_calls


def lua_escape(s):
    """Escapa una cadena para usarla entre comillas dobles en Lua."""

    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\n", "\\n")
    s = s.replace("\t", "\\t")
    return s


def convert_file(src_path, dest_path, mode="a"):
    """
    Convierte un archivo de Translation Toolbox al formato de locale del addon.
    """
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    t_calls = extract_t_calls(content)

    if not t_calls:
        return 0

    with open(dest_path, mode, encoding="utf-8") as f:
        for original, translation, type_ in t_calls:
            escaped_original = lua_escape(original)
            escaped_translation = lua_escape(translation)
            f.write(f't("{escaped_original}", "{escaped_translation}", "{type_}")\n')

    return len(t_calls)


def clean_directory(dir_path):
    """Limpia un directorio sin borrar .gitkeep ni init.lua."""
    if not dir_path.exists():
        return
    for item in dir_path.iterdir():
        if item.name in (".gitkeep", "init.lua"):
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)


def build_addon():
    """Construye el addon desde los archivos de traducción."""
    print("=" * 60)
    print("  Construyendo addon tome-spanish...")
    print("=" * 60)

    # Si existen archivos divididos, mergear primero
    split_dir = TRANS_DIR / "mod-tome-split"
    if split_dir.exists():
        merge_script = Path(__file__).parent / "merge_sections.py"
        if merge_script.exists():
            print("  📂 Detectados archivos divididos, mergeando...")
            import subprocess

            result = subprocess.run(
                [sys.executable, str(merge_script)], capture_output=True, text=True
            )
            if result.returncode == 0:
                # Extraer número de secciones del output
                for line in result.stdout.split("\n"):
                    if "Merge completado" in line:
                        print(f"     {line.strip()}")
            else:
                print(f"  ⚠ Error en merge: {result.stderr}")

    # Crear directorios
    LOCALE_DIR.mkdir(parents=True, exist_ok=True)
    ENGINE_LOCALE_DIR.mkdir(parents=True, exist_ok=True)

    # Limpiar archivos de locale anteriores
    for f in LOCALE_DIR.glob("*.lua"):
        if f.name != ".gitkeep":
            f.unlink()
    for f in ENGINE_LOCALE_DIR.glob("*.lua"):
        if f.name != ".gitkeep":
            f.unlink()

    # Archivos a mergear en el locale principal
    engine_locale_files = ["engine.lua"]

    # Procesar engine primero, luego main
    total_calls = 0

    # 1. Engine locale
    engine_file = ENGINE_LOCALE_DIR / "es.lua"
    with open(engine_file, "w", encoding="utf-8") as f:
        f.write('locale "es"\n\n')

    for src_name in engine_locale_files:
        src_path = TRANS_DIR / src_name
        if src_path.exists():
            count = convert_file(str(src_path), str(engine_file), "a")
            print(f"  ✓ {src_name}: {count} cadenas -> engine/es.lua")
            total_calls += count

    # 2. Main locale
    main_file = LOCALE_DIR / "es.lua"
    with open(main_file, "w", encoding="utf-8") as f:
        f.write('locale "es"\n\n')

    for src_name in sorted(os.listdir(TRANS_DIR)):
        if not src_name.endswith(".lua"):
            continue
        if src_name in ("_t_append.lua", "_not_merged.lua", "i18n.log", "engine.lua"):
            continue
        if src_name in engine_locale_files:
            continue

        src_path = TRANS_DIR / src_name
        count = convert_file(str(src_path), str(main_file), "a")
        if count > 0:
            print(f"  ✓ {src_name}: {count} cadenas -> locales/es.lua")
            total_calls += count

    print(f"\n  Total: {total_calls} cadenas procesadas")
    print(f"\n  Addon listo en: {ADDON_DIR}")
    print()
    return total_calls


def package_addon():
    """Empaqueta el addon como .teaa (zip)."""
    output_path = PROJECT_DIR / "tome-spanish.teaa"

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(ADDON_DIR):
            # Excluir .gitkeep y scripts/
            dirs[:] = [d for d in dirs if d != "scripts"]
            for file in files:
                if file == ".gitkeep":
                    continue
                file_path = Path(root) / file
                arcname = str(file_path.relative_to(ADDON_DIR))
                zf.write(file_path, arcname)

    print(f"  📦 Addon empaquetado: {output_path}")
    print(f"     Tamaño: {output_path.stat().st_size / 1024:.1f} KB")


def main():
    build_addon()

    if "--package" in sys.argv:
        package_addon()


if __name__ == "__main__":
    main()
