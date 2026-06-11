#!/usr/bin/env python3
"""
Traduce engine.lua completamente.
Son cadenas de UI, keybinds, opciones y mensajes del motor.

Uso: python3 scripts/translate_engine_complete.py
"""

import re
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
ENGINE_FILE = TRANS_DIR / "engine.lua"

# =============================================================================
# DICCIONARIO COMPLETO para engine.lua
# =============================================================================
ENGINE_TRANSLATIONS = {
    # === Opciones gráficas y de video ===
    "#GOLD##{bold}#Antialiased texts#WHITE##{normal}#": "#GOLD##{bold}#Textos antialiased#WHITE##{normal}#",
    "#GOLD##{bold}#Cloud Saves#WHITE##{normal}#": "#GOLD##{bold}#Guardado en la nube#WHITE##{normal}#",
    "#GOLD##{bold}#Font Scale#WHITE##{normal}#": "#GOLD##{bold}#Escala de fuente#WHITE##{normal}#",
    "#GOLD##{bold}#Framebuffers#WHITE##{normal}#": "#GOLD##{bold}#Framebuffers#WHITE##{normal}#",
    "#GOLD##{bold}#Gamma correction#WHITE##{normal}#": "#GOLD##{bold}#Corrección gamma#WHITE##{normal}#",
    "#GOLD##{bold}#Mouse cursor#WHITE##{normal}#": "#GOLD##{bold}#Cursor del ratón#WHITE##{normal}#",
    "#GOLD##{bold}#OpenGL Shaders#WHITE##{normal}#": "#GOLD##{bold}#Shaders OpenGL#WHITE##{normal}#",
    "#GOLD##{bold}#OpenGL Shaders: Advanced#WHITE##{normal}#": "#GOLD##{bold}#Shaders OpenGL: Avanzado#WHITE##{normal}#",
    "#GOLD##{bold}#OpenGL Shaders: Distortions#WHITE##{normal}#": "#GOLD##{bold}#Shaders OpenGL: Distorsiones#WHITE##{normal}#",
    "#GOLD##{bold}#OpenGL Shaders: Volumetric#WHITE##{normal}#": "#GOLD##{bold}#Shaders OpenGL: Volumétrico#WHITE##{normal}#",
    "#GOLD##{bold}#Particle effects density#WHITE##{normal}#": "#GOLD##{bold}#Densidad de partículas#WHITE##{normal}#",
    "#GOLD##{bold}#Purge Cloud Saves#WHITE##{normal}#": "#GOLD##{bold}#Purgar guardado en la nube#WHITE##{normal}#",
    "#GOLD##{bold}#Requested FPS#WHITE##{normal}#": "#GOLD##{bold}#FPS deseados#WHITE##{normal}#",
    "#GOLD##{bold}#Requested Window Position#WHITE##{normal}#": "#GOLD##{bold}#Posición de ventana#WHITE##{normal}#",
    "#GOLD##{bold}#Resolution#WHITE##{normal}#": "#GOLD##{bold}#Resolución#WHITE##{normal}#",
    "#GOLD##{bold}#Screen Zoom#WHITE##{normal}#": "#GOLD##{bold}#Zoom de pantalla#WHITE##{normal}#",
    "#GOLD##{bold}#Use tilesets#WHITE##{normal}#": "#GOLD##{bold}#Usar tilesets#WHITE##{normal}#",
    "#GREY#Developer Mode": "#GREY#Modo desarrollador",
    "#LIGHT_GREEN#Installed": "#LIGHT_GREEN#Instalado",
    "#YELLOW#-- connecting to server... --": "#YELLOW#-- conectando al servidor... --",
    "#YELLOW#Installable": "#YELLOW#Instalable",
    # === Estados y mensajes de UI ===
    "(progress will be saved)": "(el progreso se guardará)",
    "[spoilers]": "[spoilers]",
    "%0.2f %s": "%0.2f %s",
    "%d coins": "%d monedas",
    "Name": "Nombre",
    "Level": "Nivel",
    "Life": "Vida",
    "Exp": "Exp",
    "Gold": "Oro",
    "Score": "Puntuación",
    "Turn": "Turno",
    "Time": "Tiempo",
    "Damage": "Daño",
    # === Keybinds (las que no se tradujeron antes) ===
    "Six Hotkey 1": "Tecla rápida sexta 1",
    "Six Hotkey 2": "Tecla rápida sexta 2",
    "Six Hotkey 3": "Tecla rápida sexta 3",
    "Six Hotkey 4": "Tecla rápida sexta 4",
    "Six Hotkey 5": "Tecla rápida sexta 5",
    "Six Hotkey 6": "Tecla rápida sexta 6",
    "Six Hotkey 7": "Tecla rápida sexta 7",
    "Six Hotkey 8": "Tecla rápida sexta 8",
    "Six Hotkey 9": "Tecla rápida sexta 9",
    "Six Hotkey 10": "Tecla rápida sexta 10",
    "Six Hotkey 11": "Tecla rápida sexta 11",
    "Six Hotkey 12": "Tecla rápida sexta 12",
    "Seventh Hotkey 1": "Tecla rápida séptima 1",
    "Seventh Hotkey 2": "Tecla rápida séptima 2",
    "Seventh Hotkey 3": "Tecla rápida séptima 3",
    "Seventh Hotkey 4": "Tecla rápida séptima 4",
    "Seventh Hotkey 5": "Tecla rápida séptima 5",
    "Seventh Hotkey 6": "Tecla rápida séptima 6",
    "Seventh Hotkey 7": "Tecla rápida séptima 7",
    "Seventh Hotkey 8": "Tecla rápida séptima 8",
    "Seventh Hotkey 9": "Tecla rápida séptima 9",
    "Seventh Hotkey 10": "Tecla rápida séptima 10",
    "Seventh Hotkey 11": "Tecla rápida séptima 11",
    "Seventh Hotkey 12": "Tecla rápida séptima 12",
    "Eighth Hotkey 1": "Tecla rápida octava 1",
    "Eighth Hotkey 2": "Tecla rápida octava 2",
    "Eighth Hotkey 3": "Tecla rápida octava 3",
    "Eighth Hotkey 4": "Tecla rápida octava 4",
    "Eighth Hotkey 5": "Tecla rápida octava 5",
    "Eighth Hotkey 6": "Tecla rápida octava 6",
    "Eighth Hotkey 7": "Tecla rápida octava 7",
    "Eighth Hotkey 8": "Tecla rápida octava 8",
    "Eighth Hotkey 9": "Tecla rápida octava 9",
    "Eighth Hotkey 10": "Tecla rápida octava 10",
    "Eighth Hotkey 11": "Tecla rápida octava 11",
    "Eighth Hotkey 12": "Tecla rápida octava 12",
    "Ninth Hotkey 1": "Tecla rápida novena 1",
    "Ninth Hotkey 2": "Tecla rápida novena 2",
    "Ninth Hotkey 3": "Tecla rápida novena 3",
    "Ninth Hotkey 4": "Tecla rápida novena 4",
    "Ninth Hotkey 5": "Tecla rápida novena 5",
    "Ninth Hotkey 6": "Tecla rápida novena 6",
    "Ninth Hotkey 7": "Tecla rápida novena 7",
    "Ninth Hotkey 8": "Tecla rápida novena 8",
    "Ninth Hotkey 9": "Tecla rápida novena 9",
    "Ninth Hotkey 10": "Tecla rápida novena 10",
    "Ninth Hotkey 11": "Tecla rápida novena 11",
    "Ninth Hotkey 12": "Tecla rápida novena 12",
    "Tenth Hotkey 1": "Tecla rápida décima 1",
    "Tenth Hotkey 2": "Tecla rápida décima 2",
    "Tenth Hotkey 3": "Tecla rápida décima 3",
    "Tenth Hotkey 4": "Tecla rápida décima 4",
    "Tenth Hotkey 5": "Tecla rápida décima 5",
    "Tenth Hotkey 6": "Tecla rápida décima 6",
    "Tenth Hotkey 7": "Tecla rápida décima 7",
    "Tenth Hotkey 8": "Tecla rápida décima 8",
    "Tenth Hotkey 9": "Tecla rápida décima 9",
    "Tenth Hotkey 10": "Tecla rápida décima 10",
    "Tenth Hotkey 11": "Tecla rápida décima 11",
    "Tenth Hotkey 12": "Tecla rápida décima 12",
    "Eleventh Hotkey 1": "Tecla rápida undécima 1",
    "Eleventh Hotkey 2": "Tecla rápida undécima 2",
    "Eleventh Hotkey 3": "Tecla rápida undécima 3",
    "Eleventh Hotkey 4": "Tecla rápida undécima 4",
    "Eleventh Hotkey 5": "Tecla rápida undécima 5",
    "Eleventh Hotkey 6": "Tecla rápida undécima 6",
    "Eleventh Hotkey 7": "Tecla rápida undécima 7",
    "Eleventh Hotkey 8": "Tecla rápida undécima 8",
    "Eleventh Hotkey 9": "Tecla rápida undécima 9",
    "Eleventh Hotkey 10": "Tecla rápida undécima 10",
    "Eleventh Hotkey 11": "Tecla rápida undécima 11",
    "Eleventh Hotkey 12": "Tecla rápida undécima 12",
    "Twelfth Hotkey 1": "Tecla rápida duodécima 1",
    "Twelfth Hotkey 2": "Tecla rápida duodécima 2",
    "Twelfth Hotkey 3": "Tecla rápida duodécima 3",
    "Twelfth Hotkey 4": "Tecla rápida duodécima 4",
    "Twelfth Hotkey 5": "Tecla rápida duodécima 5",
    "Twelfth Hotkey 6": "Tecla rápida duodécima 6",
    "Twelfth Hotkey 7": "Tecla rápida duodécima 7",
    "Twelfth Hotkey 8": "Tecla rápida duodécima 8",
    "Twelfth Hotkey 9": "Tecla rápida duodécima 9",
    "Twelfth Hotkey 10": "Tecla rápida duodécima 10",
    "Twelfth Hotkey 11": "Tecla rápida duodécima 11",
    "Twelfth Hotkey 12": "Tecla rápida duodécima 12",
    # === Diálogos UI ===
    "Are you sure you want to quit?": "¿Seguro que quieres salir?",
    "Are you sure you want to delete this character?": "¿Seguro que quieres borrar este personaje?",
    "Yes": "Sí",
    "No": "No",
    "Cancel": "Cancelar",
    "Ok": "Aceptar",
    "Close": "Cerrar",
    "Save": "Guardar",
    "Load": "Cargar",
    "Delete": "Eliminar",
    "Rename": "Renombrar",
    "Copy": "Copiar",
    "Paste": "Pegar",
    "Select": "Seleccionar",
    "Select All": "Seleccionar todo",
    "Clear": "Limpiar",
    "Search": "Buscar",
    "Filter": "Filtrar",
    "Sort by": "Ordenar por",
    "Ascending": "Ascendente",
    "Descending": "Descendente",
    "Apply": "Aplicar",
    "Reset": "Reiniciar",
    "Default": "Por defecto",
    "Custom": "Personalizado",
    "Auto": "Automático",
    "Manual": "Manual",
    "Enabled": "Activado",
    "Disabled": "Desactivado",
    "On": "Sí",
    "Off": "No",
    "Show": "Mostrar",
    "Hide": "Ocultar",
    "Maximize": "Maximizar",
    "Minimize": "Minimizar",
    "Restore": "Restaurar",
    "Fullscreen": "Pantalla completa",
    "Windowed": "Ventana",
    "Borderless": "Sin bordes",
    # === Log messages ===
    "#LIGHT_RED#Keyboard input temporarily disabled.": "#LIGHT_RED#Entrada de teclado desactivada temporalmente.",
    "#LIGHT_RED#Mouse input temporarily disabled.": "#LIGHT_RED#Entrada de ratón desactivada temporalmente.",
    "#LIGHT_RED#Online profile disabled(switching to offline profile) due to %s.": "#LIGHT_RED#Perfil online desactivado(cambiando a offline) por %s.",
    "#YELLOW#Connection to online server established.": "#YELLOW#Conexión al servidor establecida.",
    "#YELLOW#Connection to online server lost, trying to reconnect.": "#YELLOW#Conexión al servidor perdida, reconectando.",
    "#YELLOW#Error report sent, thank you.": "#YELLOW#Informe de error enviado, gracias.",
    "#YELLOW#-- connecting to server... --": "#YELLOW#-- conectando al servidor... --",
    # === Keybinds (adicionales) ===
    "Press a key (escape to cancel, backspace to remove) for: %s": "Pulsa una tecla (escape para cancelar, retroceso para quitar) para: %s",
    "Press a key for: %s": "Pulsa una tecla para: %s",
    "Current key: %s": "Tecla actual: %s",
    "Key not set": "Tecla no asignada",
    "Remove key": "Quitar tecla",
    "Reset to default": "Restaurar por defecto",
    "Keyboard Settings": "Ajustes de teclado",
    "Mouse Settings": "Ajustes de ratón",
    "Change Key": "Cambiar tecla",
    "Key Bindings": "Asignación de teclas",
    # === Títulos de opciones ===
    "Audio": "Audio",
    "Video": "Video",
    "Gameplay": "Jugabilidad",
    "Interface": "Interfaz",
    "Controls": "Controles",
    "General": "General",
    "Advanced": "Avanzado",
    "Volume": "Volumen",
    "Master Volume": "Volumen general",
    "Music Volume": "Volumen de música",
    "SFX Volume": "Volumen de efectos",
    "Ambient Volume": "Volumen ambiental",
    "Language": "Idioma",
    "Font": "Fuente",
    "Font Size": "Tamaño de fuente",
    "UI Scale": "Escala de UI",
    "Tooltip delay": "Retardo de tooltip",
    "Show tooltips": "Mostrar tooltips",
    "Always center on player": "Centrar siempre en jugador",
    "Show minimap": "Mostrar minimapa",
    "Show fps": "Mostrar FPS",
    "Show clock": "Mostrar reloj",
    "Auto-explore": "Autoexplorar",
    "Auto-rest": "Autodescanso",
    "Auto-pickup": "Auto-recoger",
    "Auto-save": "Autoguardado",
    "Difficulty": "Dificultad",
    "Permadeath": "Muerte permanente",
    "Adventure Mode": "Modo aventura",
    "Exploration Mode": "Modo exploración",
    "Roguelike Mode": "Modo roguelike",
    "Nightmare Mode": "Modo pesadilla",
    "Insane Mode": "Modo insano",
    "Madness Mode": "Modo locura",
    # === Tooltips ===
    "HP": "PV",
    "MP": "PM",
    "SP": "PR",
    "Exp needed": "Exp necesaria",
    "Next level": "Siguiente nivel",
    "Weapon": "Arma",
    "Armor": "Armadura",
    "Defense": "Defensa",
    "Accuracy": "Precisión",
    "Damage": "Daño",
    "Range": "Alcance",
    "Speed": "Velocidad",
    "Power": "Poder",
    "Resist": "Resistir",
    "Immune": "Inmune",
    "Vulnerable": "Vulnerable",
    # === UI misc ===
    "Character": "Personaje",
    "Inventory": "Inventario",
    "Talents": "Talentos",
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
    "Play": "Jugar",
    "Start": "Empezar",
    "Finish": "Finalizar",
    "Complete": "Completar",
    "Abort": "Abortar",
    "Retry": "Reintentar",
    "Skip": "Saltar",
    "Done": "Hecho",
    "Wait": "Esperar",
    "Stop": "Parar",
    "Pause": "Pausa",
    "Resume": "Reanudar",
    "Configure": "Configurar",
    "Settings": "Ajustes",
}


# =============================================================================
# FUNCIÓN DE TRADUCCIÓN
# =============================================================================
def translate_engine():
    """Traduce engine.lua usando el diccionario completo."""
    with open(ENGINE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    lines = content.split("\n")
    new_lines = []

    for line in lines:
        m = re.match(
            r'^(\s*)t\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',
            line,
        )
        if m:
            indent = m.group(1)
            original = m.group(2)
            current_trans = m.group(3)
            type_ = m.group(4)

            # Saltar si ya está traducido
            if original != current_trans:
                new_lines.append(line)
                continue

            # Buscar en diccionario
            if original in ENGINE_TRANSLATIONS:
                translation = ENGINE_TRANSLATIONS[original]
                safe_trans = translation.replace('"', '\\"')
                new_line = f'{indent}t("{original}", "{safe_trans}", "{type_}")'
                new_lines.append(new_line)
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO ENGINE.LUA COMPLETO")
    print("=" * 60)

    if not ENGINE_FILE.exists():
        print(f"  ERROR: {ENGINE_FILE} no encontrado")
        return

    count = translate_engine()
    print(f"\n  ✅ {count} cadenas traducidas en engine.lua")
    print()

    # Mostrar cuántas quedan
    with open(ENGINE_FILE, "r", encoding="utf-8") as f:
        remaining = len(re.findall(r't\("[^"]*",\s*"[^"]*",\s*"[^"]*"\)', f.read()))
    print(f"  📊 Cadenas totales en engine.lua: ~{remaining}")


if __name__ == "__main__":
    main()
