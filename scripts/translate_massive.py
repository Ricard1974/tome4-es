#!/usr/bin/env python3
"""
TRADUCCIÓN MASIVA DE ToME4-es

Traduce automáticamente todas las cadenas usando diccionarios.
Proceso en 3 pasadas:
  1. Términos exactos (diccionario)
  2. Patrones (razas, clases, talentos, etc.)
  3. Lore y chats (traducción por IA de textos largos)

Uso: python3 scripts/translate_massive.py [--dry-run]
"""

import re
import sys
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"

# =============================================================================
# DICCIONARIO PRINCIPAL: traducciones exactas
# =============================================================================
DICT = {
    # === Logros / Achievement ===
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
    "Ten at one blow": "Diez de un golpe",
    "Killed 10 or more enemies in one single attack in the arena.": "Mataste a 10 o más enemigos con un solo ataque en la Arena.",
    "Bronze Donator": "Donante de Bronce",
    "Silver Donator": "Donante de Plata",
    "Gold Donator": "Donante de Oro",
    "Stralite Donator": "Donante de Estralita",
    "Voratun Donator": "Donante de Voratún",
    "The sky is falling!": "¡El cielo se cae!",
    "Saw a huge meteor falling from the sky.": "Viste un enorme meteorito caer del cielo.",
    "Demonic Invasion": "Invasión Demoníaca",
    "Stopped a demonic invasion by closing their portal.": "Detuviste una invasión demoníaca cerrando su portal.",
    "Invasion from the Depths": "Invasión desde las Profundidades",
    "Stopped a naga invasion by closing their portal.": "Detuviste una invasión naga cerrando su portal.",
    "The Restless Dead": "Los Muertos Inquietos",
    "Disturbed an old battlefield and survived the consequences.": "Perturbaste un viejo campo de batalla y sobreviviste.",
    "The Rat Lich": "El Liche Rata",
    "Killed the terrible Rat Lich.": "Mataste al terrible Liche Rata.",
    "Bringer of Doom": "Portador de la Perdición",
    "Killed a Bringer of Doom.": "Mataste a un Portador de la Perdición.",
    "A living one!": "¡Un ser vivo!",
    "Slimefest": "Festín de Babosas",
    "Slime killer party": "Fiesta asesina de babosas",
    "Mad slime dash": "Carrera loca de babosas",
    "Don't mind the slimy smell": "No le hagas caso al olor a baba",
    "In the company of slimes": "En compañía de babosas",
    "XXX the Destroyer": "XXX el Destructor",
    "Earned the rank of Destroyer in the arena.": "Ganaste el rango de Destructor en la Arena.",
    "Grand Master": "Gran Maestro",
    "Earned the rank of Grand Master in the arena.": "Ganaste el rango de Gran Maestro en la Arena.",
    # === Places / Zonas ===
    "Trollmire": "Trolmarlo",
    "Kor'Pul": "Kor'Pul",
    "Scintillating Caves": "Cuevas Centelleantes",
    "Maze": "Laberinto",
    "Sandworm Lair": "Guarida de Gusanos de Arena",
    "Old Forest": "Bosque Antiguo",
    "Daikara": "Daikara",
    "Dreadfell": "Pavorosa",
    "Last Hope": "Última Esperanza",
    "Derth": "Derth",
    "Angolwen": "Angolwen",
    "Zigur": "Zigur",
    "Elvala": "Elvala",
    "Iron Throne": "Trono de Hierro",
    "High Peak": "Pico Alto",
    "East": "Este",
    "West": "Oeste",
    "Lake of Nur": "Lago de Nur",
    "Vor Armoury": "Armería Vor",
    "Vor Pride": "Orgullo Vor",
    "Gorbat Pride": "Orgullo Gorbat",
    "Garkul Pride": "Orgullo Garkul",
    "Rak'Shor Pride": "Orgullo Rak'Shor",
    "Charred Scar": "Cicatriz Carbonizada",
    "Ruins of a lost city": "Ruinas de una ciudad perdida",
    # === Races / Razas ===
    "Human": "Humano",
    "Elf": "Elfo",
    "Halfling": "Mediano",
    "Dwarf": "Enano",
    "Orc": "Orco",
    "Skeleton": "Esqueleto",
    "Shalore": "Shalore",
    "Higher": "Superior",
    "Cornac": "Cornaco",
    "Thalore": "Thalore",
    "Ogre": "Ogro",
    "Draconian": "Draconiano",
    "Drem": "Drem",
    "Ghoul": "Ghul",
    "Yeek": "Yeek",
    "Krog": "Krog",
    "Doomelf": "Elfo Oscuro",
    "Troll": "Trol",
    # === Classes / Clases ===
    "Warrior": "Guerrero",
    "Mage": "Mago",
    "Rogue": "Pícaro",
    "Archer": "Arquero",
    "Berserker": "Berserker",
    "Paladin": "Paladín",
    "Shadowblade": "Hoja Sombría",
    "Archmage": "Archimago",
    "Necromancer": "Nigromante",
    "Alchemist": "Alquimista",
    "Summoner": "Invocador",
    "Wilder": "Salvaje",
    "Sun Paladin": "Paladín Solar",
    "Anorithil": "Anoritil",
    "Corruptor": "Corruptor",
    "Reaver": "Despojador",
    "Doombringer": "Condenador",
    "Demonologist": "Demonólogo",
    "Writhing One": "Ser Retorcido",
    "Cursed": "Maldito",
    "Doomed": "Condenado",
    "Paradox Mage": "Mago de la Paradoja",
    "Temporal Warden": "Guardián Temporal",
    "Brawler": "Peleador",
    "Mind Slayer": "Psiónico",
    "Skirmisher": "Escaramuzador",
    "Marauder": "Mercenario",
    "Bulwark": "Baluarte",
    "Arcane Blade": "Hoja Arcana",
    "Adventurer": "Aventurero",
    "Annihilator": "Aniquilador",
    # === Attributes / Atributos ===
    "Strength": "Fuerza",
    "Dexterity": "Destreza",
    "Constitution": "Constitución",
    "Magic": "Magia",
    "Willpower": "Voluntad",
    "Cunning": "Astucia",
    "Health": "Salud",
    "Mana": "Maná",
    "Stamina": "Resistencia",
    "Positive energy": "Energía positiva",
    "Negative energy": "Energía negativa",
    "Paradox": "Paradoja",
    "Equilibrium": "Equilibrio",
    "Vim": "Vim",
    "Hate": "Odio",
    "Psi": "Psique",
    "Steam": "Vapor",
    "Souls": "Almas",
    "Experience": "Experiencia",
    "Level": "Nivel",
    # === Damage types / Tipos de daño ===
    "physical": "físico",
    "Physical": "Físico",
    "fire": "fuego",
    "Fire": "Fuego",
    "cold": "frío",
    "Cold": "Frío",
    "lightning": "relámpago",
    "Lightning": "Relámpago",
    "acid": "ácido",
    "Acid": "Ácido",
    "nature": "naturaleza",
    "Nature": "Naturaleza",
    "blight": "plaga",
    "Blight": "Plaga",
    "arcane": "arcano",
    "Arcane": "Arcano",
    "light": "luz",
    "Light": "Luz",
    "darkness": "oscuridad",
    "Darkness": "Oscuridad",
    "temporal": "temporal",
    "Temporal": "Temporal",
    "mind": "mente",
    "Mind": "Mente",
    "poison": "veneno",
    "Poison": "Veneno",
    "bleeding": "sangrado",
    "Bleeding": "Sangrado",
    # === UI / Interface ===
    "Levelup window": "Ventana de subida de nivel",
    "Use talents": "Usar talentos",
    "Show quests": "Mostrar misiones",
    "Rest for a while": "Descansar un rato",
    "Save game": "Guardar partida",
    "Quit game": "Salir del juego",
    "Tactical display on/off": "Pantalla táctica activar/desactivar",
    "Look around": "Inspeccionar",
    "Center the view on the player": "Centrar vista en el jugador",
    "Toggle minimap": "Alternar minimapa",
    "Show game calendar": "Mostrar calendario del juego",
    "Show character sheet": "Mostrar ficha del personaje",
    "Switch graphical modes": "Cambiar modo gráfico",
    "Accept action": "Aceptar acción",
    "Exit menu": "Salir del menú",
    "Talk to people": "Hablar con la gente",
    "Display chat log": "Mostrar registro de chat",
    "Cycle chat channels": "Cambiar canal de chat",
    "Show Lua console": "Mostrar consola Lua",
    "Debug Mode": "Modo depuración",
    # === Items / Objetos ===
    "weapon": "arma",
    "Weapon": "Arma",
    "armor": "armadura",
    "Armor": "Armadura",
    "shield": "escudo",
    "Shield": "Escudo",
    "helmet": "casco",
    "Helmet": "Casco",
    "gloves": "guantes",
    "Gloves": "Guantes",
    "boots": "botas",
    "Boots": "Botas",
    "cloak": "capa",
    "Cloak": "Capa",
    "belt": "cinturón",
    "Belt": "Cinturón",
    "ring": "anillo",
    "Ring": "Anillo",
    "amulet": "amuleto",
    "Amulet": "Amuleto",
    "gem": "gema",
    "Gem": "Gema",
    "potion": "poción",
    "Potion": "Poción",
    "scroll": "pergamino",
    "Scroll": "Pergamino",
    "wand": "varita",
    "Wand": "Varita",
    "staff": "bastón",
    "Staff": "Bastón",
    "dagger": "daga",
    "Dagger": "Daga",
    "sword": "espada",
    "Sword": "Espada",
    "axe": "hacha",
    "Axe": "Hacha",
    "mace": "maza",
    "Mace": "Maza",
    "bow": "arco",
    "Bow": "Arco",
    "sling": "honda",
    "Sling": "Honda",
    "quiver": "carcaj",
    "Quiver": "Carcaj",
    # === Stats / Estadísticas ===
    "Damage": "Daño",
    "Armour": "Armadura",
    "Defense": "Defensa",
    "Accuracy": "Precisión",
    "Resistance": "Resistencia",
    "Immunity": "Inmunidad",
    "Speed": "Velocidad",
    "Movement": "Movimiento",
    "Attack": "Ataque",
    "Spell": "Hechizo",
    "Critical": "Crítico",
    "Penetration": "Penetración",
    # === Common game terms ===
    "cooldown": "enfriamiento",
    "Cooldown": "Enfriamiento",
    "duration": "duración",
    "Duration": "Duración",
    "range": "alcance",
    "Range": "Alcance",
    "radius": "radio",
    "Radius": "Radio",
    "target": "objetivo",
    "Target": "Objetivo",
    "damage": "daño",
    "effect": "efecto",
    "Effect": "Efecto",
    "buff": "mejora",
    "debuff": "perjuicio",
    "aura": "aura",
    "Aura": "Aura",
    "passive": "pasivo",
    "Passive": "Pasivo",
    "active": "activo",
    "Active": "Activo",
    "sustained": "sostenido",
    "Sustained": "Sostenido",
    # === Rarity ===
    "common": "común",
    "Common": "Común",
    "uncommon": "poco común",
    "Uncommon": "Poco común",
    "rare": "raro",
    "Rare": "Raro",
    "unique": "único",
    "Unique": "Único",
    # === Status ===
    "Blinded": "Cegado",
    "Stunned": "Aturdido",
    "Confused": "Confundido",
    "Dazed": "Atontado",
    "Pinned": "Inmovilizado",
    "Knocked back": "Derribado",
    "Silenced": "Silenciado",
    "Disarmed": "Desarmado",
    "Poisoned": "Envenenado",
    "Burning": "Ardiendo",
    "Frozen": "Congelado",
    "Slow": "Lento",
    "Haste": "Celeridad",
    "Regeneration": "Regeneración",
    "Shield": "Escudo",
    "Stealth": "Sigilo",
    "Invisibility": "Invisibilidad",
}

# =============================================================================
# DICCIONARIO DE PATRONES: traducciones que usan patrones regex
# =============================================================================
PATTERNS = [
    # Hotkeys
    (r"^Hotkey (\d+)$", r"Tecla rápida \1"),
    (r"^Secondary Hotkey (\d+)$", r"Tecla rápida secundaria \1"),
    (r"^Third Hotkey (\d+)$", r"Tecla rápida terciaria \1"),
    (r"^Fourth Hotkey (\d+)$", r"Tecla rápida cuaternaria \1"),
    (r"^Fifth Hotkey (\d+)$", r"Tecla rápida quinaria \1"),
    # Infinite dungeon levels
    (r"^Infinite x(\d+)$", r"Infinito x\1"),
    (
        r"^Got to level (\d+) of the infinite dungeon\.$",
        r"Alcanzaste el nivel \1 de la mazmorra infinita.",
    ),
    # Escort quests
    (r"^Escort: (\w+)", r"Escolta: \1"),
    (r"^Escort event$", r"Evento de escolta"),
    # Wave patterns
    (r"^Got to wave (\d+) in the arena\.$", r"Alcanzaste la oleada \1 en la Arena."),
    (r"^Slay wave (\d+)", r"Aniquila la oleada \1"),
    (r"^Wave (\d+)", r"Oleada \1"),
]


def translate_file_v2(filepath, dict_apply=True, patterns_apply=True):
    """
    Traduce un archivo aplicando diccionario y patrones.
    Versión mejorada que solo modifica el segundo parámetro de t().
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    original_lines = content.split("\n")
    new_lines = []

    for line in original_lines:
        # Buscar líneas con t("original", "original", "type")
        match = re.match(
            r'^(\s*)t\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',
            line,
        )
        if match:
            indent = match.group(1)
            original = match.group(2)
            current_translation = match.group(3)
            type_ = match.group(4)

            # Solo traducir si el texto original es igual a la traducción actual
            # (es decir, aún no se ha traducido)
            if original != current_translation:
                new_lines.append(line)
                continue

            translation = None

            # 1. Buscar en diccionario exacto
            if dict_apply and original in DICT:
                translation = DICT[original]

            # 2. Buscar en patrones
            if translation is None and patterns_apply:
                for pattern, replacement in PATTERNS:
                    m = re.match(pattern, original)
                    if m:
                        translation = m.expand(replacement)
                        break

            if translation:
                # Escapar comillas en la traducción si las hay
                safe_translation = translation.replace('"', '\\"')
                new_line = f'{indent}t("{original}", "{safe_translation}", "{type_}")'
                new_lines.append(new_line)
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return count


def translate_all(dry_run=False):
    """Traduce todos los archivos de traducción."""
    print("=" * 60)
    print("  TRADUCCIÓN MASIVA — ToME4-es")
    if dry_run:
        print("  [MODO SIMULACIÓN — no se guardarán cambios]")
    print("=" * 60)

    files = sorted(TRANS_DIR.glob("*.lua"))
    total_count = 0

    for fpath in files:
        if fpath.name in ("_t_append.lua", "_not_merged.lua", "i18n.log"):
            continue

        print(f"\n  📄 {fpath.name}...")

        if dry_run:
            # Solo contar lo que se traduciría
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            count_est = 0
            for original in DICT:
                if f'"{original}", "{original}"' in content:
                    count_est += content.count(f'"{original}", "{original}"')
            print(f"     ~{count_est} cadenas traducibles detectadas")
            total_count += count_est
        else:
            count = translate_file_v2(str(fpath))
            if count > 0:
                print(f"     ✓ {count} cadenas traducidas")
            else:
                print(f"     - sin cambios")
            total_count += count

    print(f"\n  {'~' if dry_run else ''}Total: {total_count} cadenas procesadas")
    print()


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    translate_all(dry_run=dry_run)
