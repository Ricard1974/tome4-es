#!/usr/bin/env python3
"""
Instala los archivos de locale español en los módulos del juego.
Esto hace que español esté disponible desde el primer arranque.

Uso: python3 scripts/install_locale.py /ruta/al/juego
"""

import shutil
import zipfile
import sys
import os
from pathlib import Path

GAME_DIR = (
    Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/t-engine4-linux64-1.7.6")
)
SOURCE_FILE = (
    Path(__file__).parent.parent / "tome-spanish" / "data" / "locales" / "es.lua"
)


def install_to_team(team_path, locale_name="es"):
    """Añade un archivo de locale a un .team (zip) manteniendo los archivos existentes."""
    temp_path = team_path.with_suffix(".tmp")

    # Leer archivo locale
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        locale_content = f.read()

    added = False
    with zipfile.ZipFile(team_path, "r") as zin:
        with zipfile.ZipFile(temp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                # Si ya existe el locale, lo actualizamos
                if item.filename == f"data/locales/{locale_name}.lua":
                    zout.writestr(item, locale_content)
                    added = True
                    print(f"  ✅ Actualizado: {team_path.name}/{item.filename}")
                else:
                    zout.writestr(item, zin.read(item.filename))

            # Si no existía, lo añadimos
            if not added:
                zout.writestr(f"data/locales/{locale_name}.lua", locale_content)
                print(f"  ✅ Añadido: {team_path.name}/data/locales/{locale_name}.lua")

    # Reemplazar original con el temporal
    shutil.move(temp_path, team_path)


def install_to_teae(teae_path, locale_name="es"):
    """Añade un archivo de locale a un .teae (engine zip)."""
    if not teae_path.exists():
        print(f"  ⚠ {teae_path} no encontrado")
        return

    temp_path = teae_path.with_suffix(".tmp")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        locale_content = f.read()

    added = False
    with zipfile.ZipFile(teae_path, "r") as zin:
        with zipfile.ZipFile(temp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == f"data/locales/engine/{locale_name}.lua":
                    zout.writestr(item, locale_content)
                    added = True
                    print(f"  ✅ Actualizado: {teae_path.name}/{item.filename}")
                elif item.filename == f"data/locales/{locale_name}.lua":
                    zout.writestr(item, locale_content)
                    added = True
                    print(f"  ✅ Actualizado: {teae_path.name}/{item.filename}")
                else:
                    zout.writestr(item, zin.read(item.filename))

            if not added:
                # Añadir al engine también
                zout.writestr(f"data/locales/engine/{locale_name}.lua", locale_content)
                print(
                    f"  ✅ Añadido: {teae_path.name}/data/locales/engine/{locale_name}.lua"
                )

    shutil.move(temp_path, teae_path)


def main():
    print("=" * 60)
    print("  Instalando locale español en módulos del juego")
    print("=" * 60)

    if not SOURCE_FILE.exists():
        print(f"  ERROR: {SOURCE_FILE} no encontrado")
        print("  Ejecuta primero: python3 scripts/build_addon.py")
        sys.exit(1)

    if not GAME_DIR.exists():
        print(f"  ERROR: {GAME_DIR} no encontrado")
        sys.exit(1)

    modules_dir = GAME_DIR / "game" / "modules"
    engines_dir = GAME_DIR / "game" / "engines"

    # Buscar módulos y engines
    teams = list(modules_dir.glob("*.team"))
    teaes = list(engines_dir.glob("*.teae"))

    print(f"\n  Módulos encontrados: {len(teams)}")
    for team in teams:
        print(f"    {team.name}")

    print(f"\n  Engines encontrados: {len(teaes)}")
    for teae in teaes:
        print(f"    {teae.name}")

    # Instalar en boot module (para que español aparezca en el menú principal)
    print("\n--- Instalando en boot module ---")
    boot_team = modules_dir / "boot-te4-1.7.6.team"
    if boot_team.exists():
        # Backup
        shutil.copy2(boot_team, boot_team.with_suffix(".team.bak"))
        install_to_team(boot_team, "es")
    else:
        print(f"  ⚠ {boot_team.name} no encontrado")

    # Instalar en tome module (el principal)
    print("\n--- Instalando en tome module ---")
    tome_teams = list(modules_dir.glob("tome-*.team"))
    if not tome_teams:
        # Buscar tome.team genérico
        tome_teams = list(modules_dir.glob("*.team"))
    for team in tome_teams:
        if "boot" not in team.name:
            shutil.copy2(team, team.with_suffix(".team.bak"))
            install_to_team(team, "es")

    # Instalar en engine (para traducciones del engine)
    print("\n--- Instalando en engine ---")
    for teae in teaes:
        shutil.copy2(teae, teae.with_suffix(".teae.bak"))
        install_to_teae(teae, "es")

    print(f"\n  ✅ Instalación completa")
    print(f"  Para restaurar los archivos originales, elimina los .bak")


if __name__ == "__main__":
    main()
