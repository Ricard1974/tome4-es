#!/usr/bin/env python3
"""
Traduce las cadenas del engine (keybinds, UI) al español.
Son cadenas repetitivas y fáciles de traducir.

Uso: python3 scripts/translate_engine.py
"""

import re
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
ENGINE_FILE = TRANS_DIR / "engine.lua"

# Diccionario de traducciones para keybinds y UI
TRANSLATIONS = {
    # Keybinds - actions
    "Go to next/previous level": "Ir al siguiente/nivel anterior",
    "Levelup window": "Ventana de subida de nivel",
    "Use talents": "Usar talentos",
    "Show quests": "Mostrar misiones",
    "Rest for a while": "Descansar un rato",
    "Save game": "Guardar partida",
    "Quit game": "Salir del juego",
    "Tactical display on/off": "Pantalla táctica activar/desactivar",
    "Look around": "Inspeccionar",
    "Center the view on the player": "Centrar vista en el jugador",
    "Toggle minimap": "Activar/desactivar minimapa",
    "Show game calendar": "Mostrar calendario del juego",
    "Show character sheet": "Mostrar ficha del personaje",
    "Switch graphical modes": "Cambiar modos gráficos",
    "Accept action": "Aceptar acción",
    "Exit menu": "Salir del menú",
    # Chat
    "Talk to people": "Hablar con la gente",
    "Display chat log": "Mostrar registro de chat",
    "Cycle chat channels": "Cambiar canales de chat",
    # Debug
    "Show Lua console": "Mostrar consola Lua",
    "Debug Mode": "Modo depuración",
    # Hotkeys (1-12)
    "Hotkey 1": "Tecla rápida 1",
    "Hotkey 2": "Tecla rápida 2",
    "Hotkey 3": "Tecla rápida 3",
    "Hotkey 4": "Tecla rápida 4",
    "Hotkey 5": "Tecla rápida 5",
    "Hotkey 6": "Tecla rápida 6",
    "Hotkey 7": "Tecla rápida 7",
    "Hotkey 8": "Tecla rápida 8",
    "Hotkey 9": "Tecla rápida 9",
    "Hotkey 10": "Tecla rápida 10",
    "Hotkey 11": "Tecla rápida 11",
    "Hotkey 12": "Tecla rápida 12",
    "Secondary Hotkey 1": "Tecla rápida secundaria 1",
    "Secondary Hotkey 2": "Tecla rápida secundaria 2",
    "Secondary Hotkey 3": "Tecla rápida secundaria 3",
    "Secondary Hotkey 4": "Tecla rápida secundaria 4",
    "Secondary Hotkey 5": "Tecla rápida secundaria 5",
    "Secondary Hotkey 6": "Tecla rápida secundaria 6",
    "Secondary Hotkey 7": "Tecla rápida secundaria 7",
    "Secondary Hotkey 8": "Tecla rápida secundaria 8",
    "Secondary Hotkey 9": "Tecla rápida secundaria 9",
    "Secondary Hotkey 10": "Tecla rápida secundaria 10",
    "Secondary Hotkey 11": "Tecla rápida secundaria 11",
    "Secondary Hotkey 12": "Tecla rápida secundaria 12",
    "Third Hotkey 1": "Tecla rápida terciaria 1",
    "Third Hotkey 2": "Tecla rápida terciaria 2",
    "Third Hotkey 3": "Tecla rápida terciaria 3",
    "Third Hotkey 4": "Tecla rápida terciaria 4",
    "Third Hotkey 5": "Tecla rápida terciaria 5",
    "Third Hotkey 6": "Tecla rápida terciaria 6",
    "Third Hotkey 7": "Tecla rápida terciaria 7",
    "Third Hotkey 8": "Tecla rápida terciaria 8",
    "Third Hotkey 9": "Tecla rápida terciaria 9",
    "Third Hotkey 10": "Tecla rápida terciaria 10",
    "Third Hotkey 11": "Tecla rápida terciaria 11",
    "Third Hotkey 12": "Tecla rápida terciaria 12",
    "Fourth Hotkey 1": "Tecla rápida cuaternaria 1",
    "Fourth Hotkey 2": "Tecla rápida cuaternaria 2",
    "Fourth Hotkey 3": "Tecla rápida cuaternaria 3",
    "Fourth Hotkey 4": "Tecla rápida cuaternaria 4",
    "Fourth Hotkey 5": "Tecla rápida cuaternaria 5",
    "Fourth Hotkey 6": "Tecla rápida cuaternaria 6",
    "Fourth Hotkey 7": "Tecla rápida cuaternaria 7",
    "Fourth Hotkey 8": "Tecla rápida cuaternaria 8",
    "Fourth Hotkey 9": "Tecla rápida cuaternaria 9",
    "Fourth Hotkey 10": "Tecla rápida cuaternaria 10",
    "Fourth Hotkey 11": "Tecla rápida cuaternaria 11",
    "Fourth Hotkey 12": "Tecla rápida cuaternaria 12",
    "Fifth Hotkey 1": "Tecla rápida quinaria 1",
    "Fifth Hotkey 2": "Tecla rápida quinaria 2",
    "Fifth Hotkey 3": "Tecla rápida quinaria 3",
    "Fifth Hotkey 4": "Tecla rápida quinaria 4",
    "Fifth Hotkey 5": "Tecla rápida quinaria 5",
    "Fifth Hotkey 6": "Tecla rápida quinaria 6",
    "Fifth Hotkey 7": "Tecla rápida quinaria 7",
    "Fifth Hotkey 8": "Tecla rápida quinaria 8",
    "Fifth Hotkey 9": "Tecla rápida quinaria 9",
    "Fifth Hotkey 10": "Tecla rápida quinaria 10",
    "Fifth Hotkey 11": "Tecla rápida quinaria 11",
    "Fifth Hotkey 12": "Tecla rápida quinaria 12",
    # Diálogos UI
    "Ok": "Aceptar",
    "Cancel": "Cancelar",
    "Yes": "Sí",
    "No": "No",
    "Are you sure?": "¿Estás seguro?",
    "Please confirm": "Por favor, confirma",
    "Close": "Cerrar",
    "Save": "Guardar",
    "Load": "Cargar",
    "Delete": "Eliminar",
    "Rename": "Renombrar",
    "Copy": "Copiar",
    "Paste": "Pegar",
    "Select": "Seleccionar",
    "Deselect": "Deseleccionar",
    "Select all": "Seleccionar todo",
    "Clear": "Limpiar",
    "Undo": "Deshacer",
    "Redo": "Rehacer",
    "Search": "Buscar",
    "Filter": "Filtrar",
    "Sort by": "Ordenar por",
    "Ascending": "Ascendente",
    "Descending": "Descendente",
    # UI general
    "Inventory": "Inventario",
    "Character": "Personaje",
    "Abilities": "Habilidades",
    "Talents": "Talentos",
    "Spells": "Hechizos",
    "Sustains": "Sostenidos",
    "Effects": "Efectos",
    "Quests": "Misiones",
    "Map": "Mapa",
    "Log": "Registro",
    "Options": "Opciones",
    "Help": "Ayuda",
    "Back": "Atrás",
    "Next": "Siguiente",
    "Previous": "Anterior",
    "Continue": "Continuar",
    "Exit": "Salir",
    "Main Menu": "Menú principal",
    "New Game": "Nueva partida",
    "Load Game": "Cargar partida",
    "Save Game": "Guardar partida",
    "Multiplayer": "Multijugador",
    "Credits": "Créditos",
    "Quit": "Salir",
}


def translate_file():
    """Traduce las cadenas del engine usando el diccionario."""
    with open(ENGINE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for original, translation in TRANSLATIONS.items():
        # Buscar t("original", "original", ...) y reemplazar
        # Usamos una expresión regular que busca el patrón exacto
        old = f't("{original}", "{original}",'
        new = f't("{original}", "{translation}",'
        if old in content:
            content = content.replace(old, new)
            count += 1
        else:
            # Intentar con escape de caracteres especiales
            escaped_old = old.replace("'", "\\'")
            if escaped_old != old:
                content = content.replace(escaped_old, new)
                count += 1

    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✓ Traducidas {count} cadenas en engine.lua")
    return count


def main():
    print("=" * 50)
    print("  Traduciendo engine.lua (keybinds y UI)...")
    print("=" * 50)

    if not ENGINE_FILE.exists():
        print(f"Error: {ENGINE_FILE} no encontrado")
        return

    count = translate_file()
    print(f"\n  Total: {count}/{len(TRANSLATIONS)} cadenas traducidas")
    print()


if __name__ == "__main__":
    main()
