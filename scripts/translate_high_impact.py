#!/usr/bin/env python3
"""
Traduce birth/ (razas+clases), npcs/ y achievements/.
Son secciones de ALTO IMPACTO con términos muy repetitivos.

Uso: python3 scripts/translate_high_impact.py
"""

import re
from pathlib import Path

BASE = Path(__file__).parent.parent / "translations" / "es" / "mod-tome-split"

# =============================================================================
# DICCIONARIO COMPLETO
# =============================================================================
DICT = {
    # === RAZAS ===
    "Dwarf": "Enano",
    "Dwarves": "Enanos",
    "Human": "Humano",
    "Humans": "Humanos",
    "Elf": "Elfo",
    "Elves": "Elfos",
    "Halfling": "Mediano",
    "Halflings": "Medianos",
    "Shalore": "Shalore",
    "Higher": "Superior",
    "Cornac": "Cornaco",
    "Thalore": "Thalore",
    "Ogre": "Ogro",
    "Ogres": "Ogros",
    "Draconian": "Draconiano",
    "Drem": "Drem",
    "Ghoul": "Ghul",
    "Yeek": "Yeek",
    "Krog": "Krog",
    "Doomelf": "Duendeldo",
    "Troll": "Trol",
    "Skeleton": "Esqueleto",
    "Undead": "No-muerto",
    "Undeads": "No-muertos",
    # === CLASES ===
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
    "Wanderer": "Vagabundo",
    # === Descripciones de razas ===
    "Skin": "Piel",
    "Hairs": "Pelo",
    "Hair": "Pelo",
    "Beard": "Barba",
    "Facial features": "Rasgos faciales",
    "Special": "Especial",
    "Dark Hair": "Pelo oscuro",
    "Blond Hair": "Pelo rubio",
    "Redhead Hair": "Pelo pelirrojo",
    "Dark Beard": "Barba oscura",
    "Blond Beard": "Barba rubia",
    "Redhead Beard": "Barba pelirroja",
    "Dark Mustache": "Bigote oscuro",
    "Blond Mustache": "Bigote rubio",
    "Redhead Mustache": "Bigote pelirrojo",
    "Dark Sideburns": "Patillas oscuras",
    "Blond Sideburns": "Patillas rubias",
    "Redhead Sideburns": "Patillas pelirrojas",
    "Dark Donut": "Donut oscuro",
    "Blond Donut": "Donut rubio",
    "Redhead Donut": "Donut pelirrojo",
    "Dark Flip": "Flip oscuro",
    "Blond Flip": "Flip rubio",
    "Redhead Flip": "Flip pelirrojo",
    # === Atributos ===
    "#GOLD#Stat modifiers:": "#GOLD#Modificadores de atributos:",
    "#GOLD#Life per level:#LIGHT_BLUE#": "#GOLD#Vida por nivel:#LIGHT_BLUE#",
    "#GOLD#Experience penalty:#LIGHT_BLUE#": "#GOLD#Penalización de exp:#LIGHT_BLUE#",
    "Their most important stats are:": "Sus atributos más importantes son:",
    "Strength": "Fuerza",
    "Dexterity": "Destreza",
    "Constitution": "Constitución",
    "Magic": "Magia",
    "Willpower": "Voluntad",
    "Cunning": "Astucia",
    # === NPCs: tipos ===
    "animal": "animal",
    "canine": "canino",
    "wolf": "lobo",
    "great wolf": "lobo grande",
    "dire wolf": "lobo terrible",
    "white wolf": "lobo blanco",
    "warg": "huargo",
    "fox": "zorro",
    "giant": "gigante",
    "humanoid": "humanoide",
    "skeleton": "esqueleto",
    "skeletal": "esquelético",
    "troll": "trol",
    "rat": "rata",
    "giant rat": "rata gigante",
    "snake": "serpiente",
    "spider": "araña",
    "dragon": "dragón",
    "demon": "demonio",
    "demonic": "demoníaco",
    "elemental": "elemental",
    "golem": "gólem",
    "construct": "constructo",
    "ooze": "limo",
    "slime": "babosa",
    "bat": "murciélago",
    "bear": "oso",
    "turtle": "tortuga",
    "crab": "cangrejo",
    "insect": "insecto",
    "plant": "planta",
    "tree": "árbol",
    "eye": "ojo",
    "ghost": "fantasma",
    "lich": "liche",
    "vampire": "vampiro",
    "zombie": "zombi",
    "ghoul": "ghul",
    "wight": "espectro",
    "shade": "sombra",
    "will o' the wisp": "fuego fatuo",
    # === NPC: descripciones ===
    "Lean, mean, and shaggy, it stares at you with hungry eyes.": "Magro, hirsuto y fiero, te mira con ojos hambrientos.",
    "Larger than a normal wolf, it prowls and snaps at you.": "Más grande que un lobo normal, merodea y te gruñe.",
    "Easily as big as a horse, this wolf menaces you with its claws and fangs.": "Grande como un caballo, este lobo te amenaza con sus garras y colmillos.",
    "It is a large wolf with eyes full of cunning.": "Es un lobo grande con ojos llenos de astucia.",
    "The quick brown fox jumps over the lazy dog.": "El rápido zorro marrón salta sobre el perro perezoso.",
    "It is a large wolf with eyes full of cunning, thrice the size of a normal warg.": "Es un lobo grande con ojos astutos, triple de tamaño que un huargo normal.",
    # === NPC: nombres ===
    "Rungof the Warg Titan": "Rungof el Titán Huargo",
    # === Achievements ===
    # (muchos ya traducidos en la primera pasada)
    "Homecoming": "Regreso a casa",
    "Destroyer of the universe": "Destructor del universo",
    "Destroyer of the world": "Destructor del mundo",
    "Harvest festival": "Festival de la cosecha",
    "Back to basics": "Volver a lo básico",
    "Catch that mage!": "¡Atrapa a ese mago!",
    "Tales of Maj'Eyal": "Tales of Maj'Eyal",
    "Hunting contest": "Concurso de caza",
    "Half-blood": "Mestizo",
    "Through the void": "A través del vacío",
    "The beast within": "La bestia interior",
    "Killing spree": "Espiral asesina",
    "Impossible death": "Muerte imposible",
    "Templar": "Templario",
    "Suicide mission": "Misión suicida",
    "Luck of the little folk": "Suerte del pueblo pequeño",
    "Rare (not so)": "Raro (no tanto)",
    "Partially sorted": "Parcialmente ordenado",
    "Sorted": "Ordenado",
    "Tactical": "Táctico",
    "Fast as lightning": "Rápido como un relámpago",
    "Can you hear me?": "¿Puedes oírme?",
    "Ignorance is bliss": "La ignorancia es felicidad",
    "Having a blast": "Pásatelo bomba",
    "Sliders": "Deslizantes",
    "Logistical nightmare": "Pesadilla logística",
    "Do not do it!": "¡No lo hagas!",
    "Fearsome": "Temible",
    "Speedy": "Veloz",
    "Tremendous": "Tremendo",
    "Do more!": "¡Haz más!",
    "Not so simple": "No tan simple",
    "Saving the world": "Salvando el mundo",
    "The Dragon's Hoard": "El Tesoro del Dragón",
    "Riddles of the night": "Acertijos de la noche",
    "The Earth Spawn": "El Engendro de la Tierra",
    "More triangles": "Más triángulos",
    "A weird danger": "Un peligro extraño",
    "Sword of the Long Years": "Espada de los Largos Años",
    "Triumph of the Weak": "Triunfo del Débil",
    "Deal with the orcs": "Trato con los orcos",
    "Suicide Squad": "Escuadrón Suicida",
    "No way? No way!": "¿De ninguna manera? ¡De ninguna manera!",
    "What a shame": "Qué vergüenza",
    "Burning day": "Día ardiente",
    "Brain freezel": "¡Congelación cerebral!",
    "Darkness Unlimited": "Oscuridad ilimitada",
    "Fall of the Guard": "Caída de la Guardia",
    "Echoes of the Past": "Ecos del Pasado",
    "Impossible Doom": "Perdición Imposible",
    "Destruction of the Krypt": "Destrucción del Krypt",
}


def translate_dir(dir_path):
    total = 0
    files_affected = 0
    for fpath in sorted(dir_path.rglob("*.lua")):
        count = 0
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

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

        if count > 0:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            rel = fpath.relative_to(BASE.parent.parent)
            print(f"  ✅ {rel}: +{count}")
            total += count
            files_affected += 1

    return total, files_affected


def main():
    print("=" * 60)
    print("  ALTO IMPACTO: birth + npcs + achievements")
    print("=" * 60)

    gran_total = 0

    # 1. Razas
    print("\n--- RAZAS ---")
    t, f = translate_dir(BASE / "data" / "birth" / "races")
    gran_total += t

    # 2. Clases
    print("\n--- CLASES ---")
    t, f = translate_dir(BASE / "data" / "birth" / "classes")
    gran_total += t

    # 3. Descriptores
    print("\n--- DESCRIPTORES ---")
    for f in (BASE / "data" / "birth").glob("*.lua"):
        if f.is_file():
            t = 0
            with open(f, "r", encoding="utf-8") as fh:
                content = fh.read()
            lines = content.split("\n")
            new_lines = []
            for line in lines:
                m = re.match(
                    r'^(\s*)t\("((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',
                    line,
                )
                if m and m.group(1) == m.group(2) and m.group(2) in DICT:
                    orig = m.group(2)
                    trans = DICT[orig]
                    safe = trans.replace('"', '\\"')
                    new_lines.append(
                        f'{m.group(1)}t("{orig}", "{safe}", "{m.group(4)}")'
                    )
                    t += 1
                else:
                    new_lines.append(line)
            if t > 0:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(new_lines))
                print(f"  ✅ {f.name}: +{t}")
                gran_total += t

    # 4. NPCs
    print("\n--- NPCS ---")
    t, f = translate_dir(BASE / "data" / "general" / "npcs")
    gran_total += t

    # 5. Achievements
    print("\n--- ACHIEVEMENTS ---")
    t, f = translate_dir(BASE / "data" / "achievements")
    gran_total += t

    print(f"\n{'=' * 60}")
    print(f"  TOTAL: {gran_total} traducciones")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
