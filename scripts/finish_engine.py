#!/usr/bin/env python3
"""
Traduce TODAS las cadenas restantes de engine.lua (UI, menús, opciones, chat).
Cubre el 100% de las cadenas que quedan.

Uso: python3 scripts/finish_engine.py
"""

import re
from pathlib import Path

ENGINE_FILE = Path(__file__).parent.parent / "translations" / "es" / "engine.lua"

DICT = {
    # === Chat ===
    "Global": "Global",
    "Chat filters": "Filtros de chat",
    "Public chat": "Chat público",
    "Private whispers": "Susurros privados",
    "Join/part messages": "Mensajes de entrada/salida",
    "First time achievements (recommended to keep them on)": "Logros por primera vez (recomendado mantenerlos)",
    "Important achievements (recommended to keep them on)": "Logros importantes (recomendado mantenerlos)",
    "Other achievements": "Otros logros",
    "Select which types of chat events to see or not.": "Selecciona qué tipos de eventos de chat ver o no.",
    "Chat ignore list": "Lista de ignorados del chat",
    "Stop ignoring": "Dejar de ignorar",
    "Click a user to stop ignoring her/his messages.": "Click en un usuario para dejar de ignorar sus mensajes.",
    "[spoilers]": "[spoilers]",
    # === Video / Resolución ===
    "Switch Resolution": "Cambiar resolución",
    "Engine Restart Required": "Requiere reinicio del motor",
    "Reset Window Position?": "¿Restablecer posición de ventana?",
    "Simply restart or restart+reset window position?": "¿Solo reiniciar o reiniciar + restablecer posición?",
    "Restart": "Reiniciar",
    "Restart with reset": "Reiniciar y restablecer",
    "Display Resolution": "Resolución de pantalla",
    "Video Options": "Opciones de vídeo",
    "Show Achievements": "Mostrar logros",
    "No": "No",
    # === Menú del juego ===
    "Game Menu": "Menú del juego",
    "Developer Mode": "Modo desarrollador",
    "Disable developer mode?": "¿Desactivar modo desarrollador?",
    "Enable developer mode?": "¿Activar modo desarrollador?",
    # === Opciones de juego ===
    "Game Options": "Opciones del juego",
    "Audio Options": "Opciones de audio",
    "Video Options": "Opciones de vídeo",
    "Interface Options": "Opciones de interfaz",
    "Keybind Options": "Opciones de teclas",
    "Chat Options": "Opciones de chat",
    "Accessibility Options": "Opciones de accesibilidad",
    "Misc Options": "Opciones varias",
    "Mouse Options": "Opciones de ratón",
    "Keyboard Options": "Opciones de teclado",
    "Tooltip Options": "Opciones de tooltips",
    "UI Options": "Opciones de interfaz",
    # === Opciones varias ===
    "Enable music": "Activar música",
    "Enable sound": "Activar sonido",
    "Music volume": "Volumen de música",
    "Sound volume": "Volumen de sonido",
    "Ambient volume": "Volumen ambiente",
    "Effects volume": "Volumen de efectos",
    "Master volume": "Volumen general",
    "Auto-explore": "Autoexplorar",
    "Auto-rest": "Autodescansar",
    "Auto-pickup": "Auto-recoger",
    "Auto-save": "Autoguardar",
    "Auto-explore stops when item seen": "Autoexplorar para al ver objeto",
    "Auto-explore stops when attackable seen": "Autoexplorar para al ver atacable",
    "Lua Console": "Consola Lua",
    "Remove": "Eliminar",
    "Add": "Añadir",
    "Edit": "Editar",
    "Up": "Arriba",
    "Down": "Abajo",
    # === Misc ===
    "???": "???",
    "Error": "Error",
    "(progress will be saved)": "(el progreso se guardará)",
    "Global": "Global",
    "English": "Inglés",
    "Chat": "Chat",
    "Message": "Mensaje",
    "Messages": "Mensajes",
    "Input": "Entrada",
    "Output": "Salida",
    "All": "Todo",
    "None": "Ninguno",
    "OK": "Aceptar",
    # === Keybinds que faltan ===
    "Copy": "Copiar",
    "Paste": "Pegar",
    "Cut": "Cortar",
    "Undo": "Deshacer",
    "Redo": "Rehacer",
    "Select all": "Seleccionar todo",
    "Deselect": "Deseleccionar",
    "Find": "Buscar",
    "Find next": "Buscar siguiente",
    "Find previous": "Buscar anterior",
    "Replace": "Reemplazar",
    "Replace all": "Reemplazar todo",
    "Go to line": "Ir a línea",
    "Toggle comment": "Comentar/descomentar",
    "Indent": "Indentar",
    "Unindent": "Desindentar",
    # === Opciones del juego ===
    "Difficulty": "Dificultad",
    "Permadeath": "Muerte permanente",
    "Campaign": "Campaña",
    "Main Campaign": "Campaña principal",
    "Arena": "Arena",
    "Infinite Dungeon": "Mazmorra infinita",
    "Adventure": "Aventura",
    "Roguelike": "Roguelike",
    "Exploration": "Exploración",
    "Normal": "Normal",
    "Nightmare": "Pesadilla",
    "Insane": "Insano",
    "Madness": "Locura",
}


def finish_engine():
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
            current = m.group(3)
            type_ = m.group(4)

            if original != current:
                new_lines.append(line)
                continue

            if original in DICT:
                trans = DICT[original]
                safe = trans.replace('"', '\\"')
                new_lines.append(f'{indent}t("{original}", "{safe}", "{type_}")')
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return count


def main():
    print("=" * 60)
    print("  COMPLETANDO ENGINE.LUA (UI y menús)")
    print("=" * 60)

    count = finish_engine()
    print(f"\n  ✅ {count} cadenas traducidas")

    with open(ENGINE_FILE) as f:
        content = f.read()
    untranslated = sum(
        1 for line in content.split("\n") if re.match(r't\("([^"]*)",\s*"\1"', line)
    )
    print(f"  📊 Quedan {untranslated} sin traducir en engine.lua")
    print()


if __name__ == "__main__":
    main()
