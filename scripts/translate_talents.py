#!/usr/bin/env python3
"""
FASE 3: Traduce nombres de talentos (data/talents/*).
Prioriza los nombres de talentos y mensajes de activación.

Uso: python3 scripts/translate_talents.py
"""

import re
from pathlib import Path

TALENTS_DIR = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "data"
    / "talents"
)

# =============================================================================
# DICCIONARIO DE TALENTOS
# =============================================================================
DICT = {
    # === Técnicas de combate ===
    "Thick Skin": "Piel gruesa",
    "Heavy Armour Training": "Entrenamiento en armadura pesada",
    "Light Armour Training": "Entrenamiento en armadura ligera",
    "Combat Accuracy": "Precisión de combate",
    "Weapons Mastery": "Maestría en armas",
    "Dagger Mastery": "Maestría en dagas",
    "Exotic Weapons Mastery": "Maestría en armas exóticas",
    "Combat Training": "Entrenamiento de combate",
    "Combat Techniques": "Técnicas de combate",
    "Combat Veteran": "Veterano de combate",
    "Weapon Combat": "Combate armado",
    "Archery": "Arquería",
    "Archery Training": "Entrenamiento en arquería",
    "Throwing Knives": "Cuchillos arrojadizos",
    "Dual Weapons": "Armas dobles",
    "Dual Weapon Training": "Entrenamiento en armas dobles",
    "Two-Handed Weapons": "Armas a dos manos",
    "Two-Handed Assault": "Asalto a dos manos",
    "Weaponshield": "Escudo-armado",
    "Shield Training": "Entrenamiento en escudo",
    "Shield Assault": "Asalto con escudo",
    "Shield Defense": "Defensa con escudo",
    "Shield Offense": "Ofensiva con escudo",
    "Shield Slam": "Golpe de escudo",
    "Shield Pummel": "Golpiza de escudo",
    "Bastion": "Baluarte",
    "Repulsion": "Repulsión",
    "Assault": "Asalto",
    "Rush": "Embestida",
    "Charge": "Carga",
    "Stun": "Aturdimiento",
    "Stunning Blow": "Golpe aturdidor",
    "Knockback": "Derribo",
    "Death Blow": "Golpe mortal",
    "Cripple": "Lisiar",
    "Maim": "Mutilar",
    "Hemorrhage": "Hemorragia",
    "Berserker": "Berserker",
    "Berserker Rage": "Ira del berserker",
    "Fearless": "Imparcial",
    "Rampage": "Rabia",
    "Murder": "Asesinato",
    "Bloodbath": "Baño de sangre",
    "Blood Thirst": "Sed de sangre",
    "Blood Frenzy": "Frenesí de sangre",
    "Relentless Fury": "Furia implacable",
    "Unstoppable": "Imparable",
    "Surge": "Surge",
    "Stealth": "Sigilo",
    "Hide in Plain Sight": "Ocultarse a plena vista",
    "Shadowstrike": "Golpe sombrío",
    "Backstab": "Apuñalar por la espalda",
    # === Hechizos ===
    "Flame": "Llama",
    "Flameshock": "Descarga ígnea",
    "Fireflash": "Destello ígneo",
    "Inferno": "Infierno",
    "Manathrust": "Empuje de maná",
    "Arcane Reconstruction": "Reconstrucción arcana",
    "Arcane Shield": "Escudo arcano",
    "Shielding": "Escudo protector",
    "Aegis": "Égida",
    "Arcane Vortex": "Vórtice arcano",
    "Disruption Shield": "Escudo de disrupción",
    "Metaflow": "Metaflujo",
    "Spellcraft": "Arte de hechizar",
    "Quicken Spells": "Acelerar hechizos",
    "Essence of Speed": "Esencia de velocidad",
    "Freeze": "Congelar",
    "Ice Shards": "Fragmentos de hielo",
    "Ice Storm": "Tormenta de hielo",
    "Ice Armour": "Armadura de hielo",
    "Frozen Feet": "Pies congelados",
    "Glacial Vapour": "Vapor glacial",
    "Tidal Wave": "Ola gigante",
    "Lightning": "Relámpago",
    "Chain Lightning": "Cadena de relámpagos",
    "Feather Wind": "Viento de plumas",
    "Thunderstorm": "Tormenta eléctrica",
    "Hurricane": "Huracán",
    "Shock": "Descarga",
    "Arcane Power": "Poder arcano",
    "Teleport": "Teletransporte",
    "Phase Door": "Puerta dimensional",
    "Telekinetic": "Telequinético",
    "Illuminate": "Iluminar",
    "Shatter": "Hacer añicos",
    "Stone": "Piedra",
    "Stone Wall": "Muro de piedra",
    "Earthquake": "Terremoto",
    "Meteor": "Meteoro",
    "Pulverizing Auger": "Barrena pulverizadora",
    "Disintegrate": "Desintegrar",
    # === Nigromancia ===
    "Necromancy": "Nigromancia",
    "Animus": "Ánimus",
    "Soul": "Alma",
    "Souls": "Almas",
    "Haunt": "Acechar",
    "Ghost": "Fantasma",
    "Phantasm": "Fantasmal",
    "Will o' the Wisp": "Fuego fatuo",
    "Darkness": "Oscuridad",
    "Nightfall": "Anochecer",
    "Invoke Darkness": "Invocar oscuridad",
    "Circle of Death": "Círculo de muerte",
    "Crepuscule": "Crepúsculo",
    "Blight": "Plaga",
    "Bone": "Hueso",
    "Bone Shield": "Escudo de hueso",
    "Bone Spear": "Lanza de hueso",
    "Bone Armour": "Armadura de hueso",
    "Bone Nova": "Nova de hueso",
    "Bone Grab": "Garra de hueso",
    "Undead": "No-muerto",
    "Lichform": "Forma de liche",
    "Lich": "Liche",
    "Ghoul": "Ghul",
    "Ghoul Rot": "Podredumbre de ghul",
    # === Invocación ===
    "Summoning": "Invocación",
    "Summon": "Invocar",
    "War Hound": "Sabueso de guerra",
    "Jelly": "Babosa",
    "Minotaur": "Minotauro",
    "Stone Golem": "Gólem de piedra",
    "Spider": "Araña",
    "Ritch": "Ritch",
    "Turtle": "Tortuga",
    "Fire Drake": "Dragón de fuego",
    "Shade": "Sombra",
    "Jelly Spread": "Extensión de babosa",
    "Mitotic Split": "División mitótica",
    # === Psiónico ===
    "Mindpower": "Poder mental",
    "Mindlash": "Latigazo mental",
    "Mindwave": "Onda mental",
    "Mind Blast": "Explosión mental",
    "Mental": "Mental",
    "Psionic": "Psiónico",
    "Telekinesis": "Telequinesis",
    "Mind Control": "Control mental",
    "Psychic": "Psíquico",
    "Brain": "Cerebro",
    "Thought": "Pensamiento",
    "Dream": "Sueño",
    "Dreaming": "Soñar",
    # === Cólera / Maldición ===
    "Cursed": "Maldito",
    "Cursed Aura": "Aura maldita",
    "Gloom": "Penumbra",
    "Fear": "Miedo",
    "Paranoia": "Paranoia",
    "Despair": "Desesperación",
    "Madness": "Locura",
    "Predator": "Depredador",
    "Stalk": "Acechar",
    # === Prodigios ===
    "Prodigy": "Prodigio",
    "Prodigies": "Prodigios",
    "Flexible Combat": "Combate flexible",
    "Adept": "Experto",
    "Arcane Might": "Poder arcano",
    "Corrupted Shell": "Coraza corrupta",
    "Draconic Will": "Voluntad draconiana",
    "Eternal Guard": "Guardia eterna",
    "Eye of the Tiger": "Ojo del tigre",
    "Giant Leap": "Salto gigante",
    "I Can Feel": "Puedo sentir",
    "Meteor Crash": "Impacto de meteoro",
    "Mighty :": "Poderoso:",
    "Never Stop Running": "Nunca pares de correr",
    "Pain Enhancement System": "Sistema de mejora del dolor",
    "PES": "SMP",
    "Poisonous Spores": "Esporas venenosas",
    "Spine of the World": "Espina dorsal del mundo",
    "Superpower": "Superpoder",
    "Windtouched Speed": "Velocidad del viento",
    "Worldly Knowledge": "Conocimiento mundano",
    "Writhing Mass": "Masa retorcida",
    # === Paladín solar ===
    "Sun Paladin": "Paladín solar",
    "Celestial": "Celestial",
    "Sun": "Sol",
    "Solar": "Solar",
    "Light": "Luz",
    "Holy": "Sagrado",
    "Divine": "Divino",
    "Sunray": "Rayo solar",
    "Searing Light": "Luz abrasadora",
    "Healing Light": "Luz curativa",
    "Providence": "Providencia",
    "Bathe in Light": "Bañarse en luz",
    "Chant": "Cántico",
    "Chants": "Cánticos",
    "Glyph": "Glifo",
    "Glyphs": "Glifos",
    "Barrier": "Barrera",
    "Weapon of Light": "Arma de luz",
    "Weapon of Wrath": "Arma de ira",
    "Righteous": "Justo",
    # === Corrupción ===
    "Corruption": "Corrupción",
    "Corruptor": "Corruptor",
    "Demon": "Demonio",
    "Demonic": "Demoníaco",
    "Blood": "Sangre",
    "Vim": "Vim",
    "Drain": "Drenar",
    "Soul Rot": "Podredumbre del alma",
    "Burning Sacrifice": "Sacrificio ardiente",
    "Dark Portal": "Portal oscuro",
    "Fearscape": "Páramo del miedo",
    "Abyssal Shield": "Escudo abismal",
    # === Cronomancia ===
    "Chronomancy": "Cronomancia",
    "Paradox": "Paradoja",
    "Temporal": "Temporal",
    "Time": "Tiempo",
    "Timeless": "Intemporal",
    "Slow": "Ralentizar",
    "Haste": "Celeridad",
    "Speed": "Velocidad",
    "Cease to Exist": "Dejar de existir",
    "Age of Dusk": "Edad del ocaso",
    "Age of Twilight": "Edad del crepúsculo",
    # === Misc / varios ===
    "Survival": "Supervivencia",
    "Devour": "Devorar",
    "Saving": "Guardar",
    "Assimilate": "Asimilar",
    "Friendship": "Amistad",
    "Breed": "Reproducir",
    "Distortion": "Distorsión",
    "Bellows": "Soplidos",
    "Fire Breath": "Aliento de fuego",
    "Ice Breath": "Aliento de hielo",
    "Lightning Breath": "Aliento de relámpago",
    "Sand Breath": "Aliento de arena",
    "Corrosive Breath": "Aliento corrosivo",
    "Venom Breath": "Aliento venenoso",
    "Swallow": "Tragar",
    "@source@ oozes over the ground!!": "¡@source@ se extiende sobre el suelo!",
    "@Source@ summons a War Hound!": "¡@Source@ invoca un Sabueso de guerra!",
    "You cannot summon; you are suppressed!": "¡No puedes invocar; estás reprimido!",
    "Not enough space to summon!": "¡No hay suficiente espacio para invocar!",
    "%s (wild summon)": "%s (invocación salvaje)",
    "@Source@ summons a Jelly!": "¡@Source@ invoca una Babosa!",
    "A strange blob on the dungeon floor.": "Una extraña masa en el suelo de la mazmorra.",
    "@Source@ summons a Minotaur!": "¡@Source@ invoca un Minotauro!",
    "It is a cross between a human and a bull.": "Es un cruce entre humano y toro.",
    "@Source@ summons a Stone Golem!": "¡@Source@ invoca un Gólem de piedra!",
    "It is a massive animated statue.": "Es una estatua animada masiva.",
    "You cannot use your %s anymore.": "Ya no puedes usar tu %s.",
    "(Note that brawlers will be unable to perform many of their talents in massive armour.)": "(Los peleadores no podrán usar muchos talentos con armadura pesada.)",
    "(Note that wearing mail or plate armour will interfere with stealth.)": "(Usar armadura de malla o placas interfiere con el sigilo.)",
    "Increases the accuracy of unarmed, melee and ranged weapons by %d.": "Aumenta la precisión de armas cuerpo a cuerpo y a distancia en %d.",
    "Increases weapon damage by %d%% and physical power by 30 when using swords, axes or maces.": "Aumenta el daño de armas en %d%% y el poder físico en 30 al usar espadas, hachas o mazas.",
    "Increases weapon damage by %d%% and physical power by 30 when using daggers.": "Aumenta el daño de armas en %d%% y el poder físico en 30 al usar dagas.",
    "Increases weapon damage by %d%% and physical power by 30 when using exotic weapons.": "Aumenta el daño de armas en %d%% y el poder físico en 30 al usar armas exóticas.",
    "Your skin becomes more resilient to damage. Increases resistance to all damage by %0.1f%%.": "Tu piel se vuelve más resistente. Aumenta la resistencia a todo daño en %0.1f%%.",
}


def translate_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
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

    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return count


def main():
    print("=" * 60)
    print("  FASE 3: talents/* (nombres de talentos)")
    print("=" * 60)

    talent_files = sorted(TALENTS_DIR.rglob("*.lua"))
    total = 0
    files_affected = 0

    for fpath in talent_files:
        count = translate_file(fpath)
        if count > 0:
            print(f"  ✅ {fpath.relative_to(TALENTS_DIR.parent.parent)}: +{count}")
            total += count
            files_affected += 1

    print(f"\n  📊 Total: {total} traducciones en {files_affected} archivos")
    print()


if __name__ == "__main__":
    main()
