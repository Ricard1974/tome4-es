#!/usr/bin/env python3
"""
TRADUCCIÓN SEGURA para ToME4-es
SOLO usa el diccionario de frases completas (PHRASES) que son traducciones verificadas.
NO hace traducción palabra por palabra.

Esto garantiza que todas las traducciones sean correctas.
Las cadenas que no están en el diccionario quedan sin traducir.

Uso: python3 scripts/translate_safe.py
"""

import re
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"

# =============================================================================
# DICCIONARIO DE FRASES COMPLETAS (TRADUCCIONES VERIFICADAS)
# =============================================================================
PHRASES = {
    # === Hotkeys / Keybinds ===
    "Go to next/previous level": "Ir al siguiente/nivel anterior",
    "Levelup window": "Ventana de subida de nivel",
    "Use talents": "Usar talentos",
    "Show quests": "Mostrar misiones",
    "Rest for a while": "Descansar un rato",
    "Save game": "Guardar partida",
    "Quit game": "Salir del juego",
    "Tactical display on/off": "Vista táctica act./desact.",
    "Look around": "Inspeccionar",
    "Center the view on the player": "Centrar vista en el jugador",
    "Toggle minimap": "Alternar minimapa",
    "Show game calendar": "Mostrar calendario",
    "Show character sheet": "Mostrar personaje",
    "Switch graphical modes": "Cambiar modo gráfico",
    "Accept action": "Aceptar",
    "Exit menu": "Salir del menú",
    "Talk to people": "Hablar",
    "Display chat log": "Ver chat",
    "Cycle chat channels": "Cambiar canal",
    "Show Lua console": "Consola Lua",
    "Debug Mode": "Modo depuración",
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
    # === Logros ===
    "The Arena": "La Arena",
    "Unlocked Arena mode.": "Modo Arena desbloqueado.",
    "Arena Battler 20": "Guerrero de Arena 20",
    "Got to wave 20 in the arena.": "Alcanzaste la oleada 20 en la Arena.",
    "Arena Battler 50": "Guerrero de Arena 50",
    "Got to wave 50 in the arena.": "Alcanzaste la oleada 50 en la Arena.",
    "Almost Master of Arena": "Casi Maestro de la Arena",
    "Became the new master of the arena in 30-wave mode.": "Te convertiste en el nuevo maestro de la Arena en modo 30 oleadas.",
    "Master of Arena": "Maestro de la Arena",
    "Became the new master of the arena in 60-wave mode.": "Te convertiste en el nuevo maestro de la Arena en modo 60 oleadas.",
    "XXX the Destroyer": "XXX el Destructor",
    "Earned the rank of Destroyer in the arena.": "Ganaste el rango de Destructor en la Arena.",
    "Grand Master": "Gran Maestro",
    "Earned the rank of Grand Master in the arena.": "Ganaste el rango de Gran Maestro en la Arena.",
    "Ten at one blow": "Diez de un golpe",
    "Killed 10 or more enemies in one single attack in the arena.": "Mataste a 10 o más enemigos con un solo ataque en la Arena.",
    "Bronze Donator": "Donante de Bronce",
    "Donated up to 5 euros to Tales of Maj'Eyal.": "Donaste hasta 5 euros a Tales of Maj'Eyal.",
    "Silver Donator": "Donante de Plata",
    "Donated at least 6 euros to Tales of Maj'Eyal.": "Donaste al menos 6 euros a Tales of Maj'Eyal.",
    "Gold Donator": "Donante de Oro",
    "Donated at least 16 euros to Tales of Maj'Eyal.": "Donaste al menos 16 euros a Tales of Maj'Eyal.",
    "Stralite Donator": "Donante de Estralita",
    "Donated at least 31 euros to Tales of Maj'Eyal.": "Donaste al menos 31 euros a Tales of Maj'Eyal.",
    "Voratun Donator": "Donante de Voratún",
    "Donated more than 60 euros to Tales of Maj'Eyal.": "Donaste más de 60 euros a Tales of Maj'Eyal.",
    "The sky is falling!": "¡El cielo se cae!",
    "Saw a huge meteor falling from the sky.": "Viste un enorme meteorito caer del cielo.",
    "Demonic Invasion": "Invasión Demoníaca",
    "Stopped a demonic invasion by closing their portal.": "Detuviste una invasión demoníaca cerrando su portal.",
    "Invasion from the Depths": "Invasión desde las Profundidades",
    "Stopped a naga invasion by closing their portal.": "Detuviste una invasión naga cerrando su portal.",
    "The Restless Dead": "Los Muertos Inquietos",
    "Disturbed an old battlefield and survived the consequences.": "Perturbaste un viejo campo de batalla y sobreviviste a las consecuencias.",
    "The Rat Lich": "El Liche Rata",
    "Killed the terrible Rat Lich.": "Mataste al terrible Liche Rata.",
    "Shasshhiy'Kaish": "Shasshhiy'Kaish",
    "Killed Shasshhiy'Kaish after letting her grow as powerful as possible.": "Mataste a Shasshhiy'Kaish tras dejarla crecer todo lo posible.",
    "Bringer of Doom": "Portador de la Perdición",
    "Killed a Bringer of Doom.": "Mataste a un Portador de la Perdición.",
    "A living one!": "¡Un ser vivo!",
    "Was teleported into Caldizar's Fortress, far into the void between the stars.": "Fuiste teletransportado a la Fortaleza de Caldizar, en el vacío entre las estrellas.",
    "Slimefest": "Festín de Babosas",
    "Have 100 walls on the sludgenest turn into hostile creatures.": "Consigue que 100 muros del nido de babosas se conviertan en criaturas hostiles.",
    "Slime killer party": "Fiesta Asesina de Babosas",
    "Have 200 walls on the sludgenest turn into hostile creatures.": "Consigue que 200 muros del nido de babosas se conviertan en criaturas hostiles.",
    "Mad slime dash": "Carrera Loca de Babosas",
    "Have 300 walls on the sludgenest turn into hostile creatures.": "Consigue que 300 muros del nido de babosas se conviertan en criaturas hostiles.",
    "Don't mind the slimy smell": "No le Hagas Caso al Olor a Baba",
    "Have 400 walls on the sludgenest turn into hostile creatures.": "Consigue que 400 muros del nido de babosas se conviertan en criaturas hostiles.",
    "In the company of slimes": "En Compañía de Babosas",
    "Have 500 walls on the sludgenest turn into hostile creatures.": "Consigue que 500 muros del nido de babosas se conviertan en criaturas hostiles.",
    "Infinite x10": "Infinito x10",
    "Got to level 10 of the infinite dungeon.": "Alcanzaste el nivel 10 de la mazmorra infinita.",
    "Infinite x20": "Infinito x20",
    "Got to level 20 of the infinite dungeon.": "Alcanzaste el nivel 20 de la mazmorra infinita.",
    "Infinite x30": "Infinito x30",
    "Got to level 30 of the infinite dungeon.": "Alcanzaste el nivel 30 de la mazmorra infinita.",
    "Infinite x40": "Infinito x40",
    "Got to level 40 of the infinite dungeon.": "Alcanzaste el nivel 40 de la mazmorra infinita.",
    "Infinite x50": "Infinito x50",
    "Got to level 50 of the infinite dungeon.": "Alcanzaste el nivel 50 de la mazmorra infinita.",
    "Infinite x60": "Infinito x60",
    "Got to level 60 of the infinite dungeon.": "Alcanzaste el nivel 60 de la mazmorra infinita.",
    "Infinite x70": "Infinito x70",
    "Got to level 70 of the infinite dungeon.": "Alcanzaste el nivel 70 de la mazmorra infinita.",
    "Infinite x80": "Infinito x80",
    "Got to level 80 of the infinite dungeon.": "Alcanzaste el nivel 80 de la mazmorra infinita.",
    "Infinite x90": "Infinito x90",
    "Got to level 90 of the infinite dungeon.": "Alcanzaste el nivel 90 de la mazmorra infinita.",
    "Infinite x100": "Infinito x100",
    "Got to level 100 of the infinite dungeon.": "Alcanzaste el nivel 100 de la mazmorra infinita.",
    "Infinite x150": "Infinito x150",
    "Got to level 150 of the infinite dungeon.": "Alcanzaste el nivel 150 de la mazmorra infinita.",
    "Infinite x200": "Infinito x200",
    "Got to level 200 of the infinite dungeon.": "Alcanzaste el nivel 200 de la mazmorra infinita.",
    "Infinite x300": "Infinito x300",
    "Got to level 300 of the infinite dungeon.": "Alcanzaste el nivel 300 de la mazmorra infinita.",
    "Infinite x400": "Infinito x400",
    "Got to level 400 of the infinite dungeon.": "Alcanzaste el nivel 400 de la mazmorra infinita.",
    "Infinite x500": "Infinito x500",
    "Got to level 500 of the infinite dungeon.": "Alcanzaste el nivel 500 de la mazmorra infinita.",
}


# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================
def translate_file(fpath):
    """Traduce SOLO las cadenas que están en PHRASES."""
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    lines = content.split("\n")
    new_lines = []

    for line in lines:
        # Buscar t("original", "original", "type") (sin traducir)
        match = re.match(
            r'^(\s*)t\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',
            line,
        )
        if match:
            indent = match.group(1)
            original = match.group(2)
            current_trans = match.group(3)
            type_ = match.group(4)

            # Solo traducir si original == current (aún sin traducir)
            if original != current_trans:
                new_lines.append(line)
                continue

            # Buscar en diccionario
            if original in PHRASES:
                translation = PHRASES[original]
                safe_trans = translation.replace('"', '\\"')
                new_line = f'{indent}t("{original}", "{safe_trans}", "{type_}")'
                new_lines.append(new_line)
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return count


def main():
    print("=" * 60)
    print("  TRADUCCIÓN SEGURA — ToME4-es")
    print("  Solo frases del diccionario verificado")
    print("=" * 60)

    files = sorted(TRANS_DIR.glob("*.lua"))
    total = 0

    for fpath in files:
        if fpath.name in (
            "_t_append.lua",
            "_not_merged.lua",
            "i18n.log",
            "copy_files.py",
        ):
            continue

        print(f"  📄 {fpath.name}...", end=" ")
        count = translate_file(str(fpath))
        print(f"✓ {count} cadenas traducidas")
        total += count

    print(f"\n  TOTAL: {total} cadenas traducidas")
    print()


if __name__ == "__main__":
    main()
