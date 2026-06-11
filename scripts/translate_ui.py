#!/usr/bin/env python3
"""
Traduce engine.lua + todos los diálogos de UI visibles.
Cubre: engine, CharacterSheet, GameOptions, LevelupDialog,
UseTalents, DeathDialog, Birther, MapMenu, Donation.
"""

import re
from pathlib import Path

BASE = Path(__file__).parent.parent
TRANS_DIR = BASE / "translations" / "es"
SPLIT_DIR = TRANS_DIR / "mod-tome-split"

# =============================================================================
# ENGINE.LUA - Términos de interfaz
# =============================================================================
ENGINE = {
    " ???": " ???",
    " No": " No",
    " [spoilers]": " [spoilers]",
    " (progress will be saved)": " (el progreso se guardará)",
    "Exit Game": "Salir del juego",
    "Gesture": "Gesto",
    "Language Selection": "Selección de idioma",
    "Yours only": "Solo tuyos",
    "Everything": "Todo",
    "When": "Cuándo",
    "Who": "Quién",
    "Progress: ": "Progreso: ",
    "???": "???",
    "Enc.": "Peso",
    "Lua Error": "Error de Lua",
    "What happened?: ": "¿Qué pasó?: ",
    "Pickup": "Recoger",
    "Text": "Texto",
    "enabled": "activado",
    "disabled": "desactivado",
    "??": "??",
    "Normal": "Normal",
    "none": "ninguno",
    "all": "todos",
    "Show": "Mostrar",
    "Hide": "Ocultar",
    "Fullscreen": "Pantalla completa",
    "Windowed": "Ventana",
    "Borderless": "Sin bordes",
    "Default": "Por defecto",
    "Custom": "Personalizado",
    "On": "Sí",
    "Off": "No",
    "Auto": "Automático",
    "Manual": "Manual",
    "Enabled": "Activado",
    "Disabled": "Desactivado",
    "Low": "Bajo",
    "Medium": "Medio",
    "High": "Alto",
    "Ultra": "Ultra",
    "Accept": "Aceptar",
    "Reject": "Rechazar",
    "Confirm": "Confirmar",
    "Cancel": "Cancelar",
    "Close": "Cerrar",
    "Apply": "Aplicar",
    "Reset": "Reiniciar",
    "Restore": "Restaurar",
    "Undo": "Deshacer",
    "Redo": "Rehacer",
    "Copy to clipboard": "Copiar al portapapeles",
    "Search:": "Buscar:",
    "Open": "Abrir",
    "Save as...": "Guardar como...",
    "File": "Archivo",
    "Edit": "Editar",
    "Tools": "Herramientas",
    "Help": "Ayuda",
    "About": "Acerca de",
    "Settings": "Ajustes",
    "Properties": "Propiedades",
    "%s assigned to hotkey %s": "%s asignado a tecla %s",
    "Hotkey %s assigned": "Tecla %s asignada",
    "Achievements(%s/%s)": "Logros(%s/%s)",
    "Quest Log for %s": "Registro de misiones para %s",
}

# =============================================================================
# CHARACTER SHEET
# =============================================================================
CHAR_SHEET = {
    "[G]eneral": "[G]eneral",
    "#LIGHT_BLUE#Physical:": "#LIGHT_BLUE#Físico:",
    "#LIGHT_BLUE#Magical:": "#LIGHT_BLUE#Mágico:",
    "#LIGHT_BLUE#Mental:": "#LIGHT_BLUE#Mental:",
    "#LIGHT_BLUE#Damage Modifiers:": "#LIGHT_BLUE#Modificadores de daño:",
    "vs ": "vs ",
    "Heavy armor": "Armadura pesada",
    "Massive armor": "Armadura masiva",
    "Light armor": "Armadura ligera",
    "#LIGHT_BLUE#Saves:": "#LIGHT_BLUE#Salvaciones:",
    "Absolute": "Absoluto",
    "Speed Res": "Resistencia velocidad",
    "#LIGHT_BLUE#Flat resistances:": "#LIGHT_BLUE#Resistencias planas:",
    "#LIGHT_BLUE#Damage when hit:": "#LIGHT_BLUE#Daño al recibir:",
    "race/.*": "raza/.*",
    "Inscriptions": "Inscripciones",
    "Item_Talents": "Talentos de objeto",
    "Instant": "Instantáneo",
    "Activated": "Activado",
    "Sustained": "Sostenido",
    "Character dump complete": "Volcado completado",
    "Character Sheet": "Ficha del personaje",
    "Sex  : ": "Sexo: ",
    "big": "grande",
    "bigger": "más grande",
    "huge": "enorme",
    "massive": "masivo",
    "small": "pequeño",
    "tiny": "diminuto",
    "normal": "normal",
    "Sex": "Sexo",
    "Subtype": "Subtipo",
    "Rank": "Rango",
    "unique": "único",
    "boss": "jefe",
    "elite": "élite",
    "rare": "raro",
    "quest": "misión",
    "random": "aleatorio",
    "fixed": "fijo",
    "store": "tienda",
    "campaign": "campaña",
    "wilderness": "jungla",
    "dungeon": "mazmorra",
    "town": "ciudad",
}

# =============================================================================
# GAME OPTIONS
# =============================================================================
GAME_OPTIONS = {
    "UI": "UI",
    "#GOLD##{bold}#Creatures movement speed#WHITE##{normal}#": "#GOLD##{bold}#Velocidad de criaturas#WHITE##{normal}#",
    "#GOLD##{bold}#Bold font for selected items#WHITE##{normal}#": "#GOLD##{bold}#Negrita para seleccionados#WHITE##{normal}#",
    "#GOLD##{bold}#Show key bindings in tooltips#WHITE##{normal}#": "#GOLD##{bold}#Teclas en tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Show quests in tooltips#WHITE##{normal}#": "#GOLD##{bold}#Misiones en tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Display floating text for damage/healing#WHITE##{normal}#": "#GOLD##{bold}#Texto flotante daño/cura#WHITE##{normal}#",
    "#GOLD##{bold}#Size of tooltip background#WHITE##{normal}#": "#GOLD##{bold}#Fondo de tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Options tree auto collapse#WHITE##{normal}#": "#GOLD##{bold}#Auto-colapsar opciones#WHITE##{normal}#",
    "#GOLD##{bold}#Combat log format#WHITE##{normal}#": "#GOLD##{bold}#Formato registro combate#WHITE##{normal}#",
    "#GOLD##{bold}#Count of each monster in telepathy#WHITE##{normal}#": "#GOLD##{bold}#Conteo monstruos telepatía#WHITE##{normal}#",
    "#GOLD##{bold}#Auto accept rename#WHITE##{normal}#": "#GOLD##{bold}#Auto-aceptar renombrar#WHITE##{normal}#",
    "#GOLD##{bold}#Difficulty based auto-explore#WHITE##{normal}#": "#GOLD##{bold}#Autoexplorar por dificultad#WHITE##{normal}#",
    "#GOLD##{bold}#Auto use insignias of learning#WHITE##{normal}#": "#GOLD##{bold}#Auto-usar insignias#WHITE##{normal}#",
    "#GOLD##{bold}#Auto use items on levelup#WHITE##{normal}#": "#GOLD##{bold}#Auto-usar al subir nivel#WHITE##{normal}#",
    "#GOLD##{bold}#Always show chat#WHITE##{normal}#": "#GOLD##{bold}#Mostrar chat siempre#WHITE##{normal}#",
    "#GOLD##{bold}#Show donators only#WHITE##{normal}#": "#GOLD##{bold}#Solo donantes#WHITE##{normal}#",
    "#GOLD##{bold}#Chat timestamp#WHITE##{normal}#": "#GOLD##{bold}#Marca de tiempo#WHITE##{normal}#",
    "#GOLD##{bold}#Display mode for chat tabs#WHITE##{normal}#": "#GOLD##{bold}#Pestañas de chat#WHITE##{normal}#",
    "#GOLD##{bold}#Small screen layout#WHITE##{normal}#": "#GOLD##{bold}#Pantalla pequeña#WHITE##{normal}#",
    "#GOLD##{bold}#Auto hide unused hotkeys#WHITE##{normal}#": "#GOLD##{bold}#Ocultar teclas no usadas#WHITE##{normal}#",
    "#GOLD##{bold}#Auto hide hotkey page buttons#WHITE##{normal}#": "#GOLD##{bold}#Ocultar páginas teclas#WHITE##{normal}#",
    "#GOLD##{bold}#Tactical map style#WHITE##{normal}#": "#GOLD##{bold}#Mapa táctico#WHITE##{normal}#",
    "#GOLD##{bold}#Display mouse information#WHITE##{normal}#": "#GOLD##{bold}#Información ratón#WHITE##{normal}#",
    "#GOLD##{bold}#Display tooltip at mouse position#WHITE##{normal}#": "#GOLD##{bold}#Tooltip en ratón#WHITE##{normal}#",
    "#GOLD##{bold}#Tactical map display#WHITE##{normal}#": "#GOLD##{bold}#Mapa táctico#WHITE##{normal}#",
}

# =============================================================================
# LEVELUP DIALOG
# =============================================================================
LEVELUP = {
    "Do you accept changes?": "¿Aceptas los cambios?",
    "Impossible": "Imposible",
    "You cannot learn this talent(s): ": "No puedes aprender: ",
    "You have no stat points left!": "¡No tienes puntos de atributo!",
    "You cannot increase this stat further until next level!": "¡No puedes aumentar más hasta el siguiente nivel!",
    "Stat is at the maximum": "Atributo al máximo",
    "You cannot increase this stat further!": "¡No puedes aumentar más!",
    "You cannot take out more points!": "¡No puedes sacar más puntos!",
    "unknown": "desconocido",
    "not enough stat": "atributo insuficiente",
    "class": "clase",
    "generic": "genérico",
    "Not enough %s talent points": "Faltan puntos de talento %s",
    "You have no %s talent points left!": "¡No tienes puntos de talento %s!",
    "Cannot learn talent": "No se puede aprender",
    "Prerequisites not met!": "¡Requisitos no cumplidos!",
    "Already known": "Ya conocido",
    "You already fully know this talent!": "¡Ya conoces este talento!",
    "You do not know this talent!": "¡No conoces este talento!",
    "Impossible here": "Imposible aquí",
    "You cannot unlearn this talent!": "¡No puedes olvidar esto!",
    "You cannot unlearn this talent because of talent(s): ": "No puedes olvidar por culpa de: ",
    "You can only improve a category mastery once!": "¡Solo puedes mejorar una categoría una vez!",
    "Not enough talent category points": "Faltan puntos de categoría",
    "You have no category points left!": "¡No tienes puntos de categoría!",
    "Too low level": "Nivel muy bajo",
    "You cannot unlearn this category!": "¡No puedes olvidar esta categoría!",
}

# =============================================================================
# USE TALENTS
# =============================================================================
USE_TALENTS = {
    "Use Talent": "Usar talento",
    "Select a target": "Selecciona un objetivo",
    "Self": "Uno mismo",
    "Enemies": "Enemigos",
    "Friends": "Aliados",
    "All": "Todos",
    "Range: ": "Alcance: ",
    "Radius: ": "Radio: ",
    "Uses: ": "Usa: ",
    "Damage: ": "Daño: ",
    "Target": "Objetivo",
    "Target: %s": "Objetivo: %s",
    "No valid target!": "¡Sin objetivo válido!",
    "target": "objetivo",
}

# =============================================================================
# DEATH DIALOG
# =============================================================================
DEATH = {
    "You have died!": "¡Has muerto!",
    "Death": "Muerte",
    "Main Menu": "Menú principal",
    "Quit": "Salir",
}

# =============================================================================
# BIRTHER (Creación de personaje)
# =============================================================================
BIRTHER = {
    "Character Creation": "Creación de personaje",
    "Random!": "¡Aleatorio!",
    "Reroll": "Rehacer",
    "Refund": "Reembolsar",
    "Points left": "Puntos restantes",
    "Confirm and continue": "Confirmar y continuar",
    "Go back": "Volver atrás",
    "Your character": "Tu personaje",
    "Summary": "Resumen",
    "Equipment": "Equipo",
    "Description": "Descripción",
    "Confirm": "Confirmar",
    "Stats": "Atributos",
    "Talents": "Talentos",
    "Load premade": "Cargar prediseñado",
    "Custom tile": "Tile personalizado",
    "Customize": "Personalizar",
    "Extra Options": "Opciones extra",
    "Name: ": "Nombre: ",
    "Campaign: ": "Campaña: ",
    "Difficulty: ": "Dificultad: ",
    "Permadeath: ": "Muerte permanente: ",
}

# =============================================================================
# MAP MENU
# =============================================================================
MAP = {
    "Actions": "Acciones",
    "%s: Inventory": "%s: Inventario",
    "Change level": "Cambiar nivel",
    "Pickup item": "Recoger objeto",
    "Move to": "Mover a",
    "Control": "Controlar",
    "Give order": "Dar orden",
    "Target player": "Apuntar a jugador",
}


# =============================================================================
# FUNCIÓN DE TRADUCCIÓN
# =============================================================================
def translate_file(filepath, translations):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for orig, trans in sorted(translations.items(), key=lambda x: -len(x[0])):
        old = f't("{orig}", "{orig}",'
        new = f't("{orig}", "{trans}",'
        if old in content:
            content = content.replace(old, new)
            count += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO INTERFAZ Y DIÁLOGOS VISIBLES")
    print("=" * 60)

    total = 0

    # 1. Engine
    c = translate_file(TRANS_DIR / "engine.lua", ENGINE)
    print(f"  ✅ engine.lua: +{c}")
    total += c

    # 2. Diálogos
    dialogs = {
        "CharacterSheet.lua": CHAR_SHEET,
        "GameOptions.lua": GAME_OPTIONS,
        "LevelupDialog.lua": LEVELUP,
        "UseTalents.lua": USE_TALENTS,
        "DeathDialog.lua": DEATH,
        "Birther.lua": BIRTHER,
        "MapMenu.lua": MAP,
    }
    for fname, trans in dialogs.items():
        fpath = SPLIT_DIR / "mod" / "dialogs" / fname
        if fpath.exists():
            c = translate_file(fpath, trans)
            print(f"  ✅ {fname}: +{c}")
            total += c
        else:
            print(f"  ⚠ No encontrado: {fname}")

    print(f"\n  📊 Total: {total} traducciones")
    print()


if __name__ == "__main__":
    main()
