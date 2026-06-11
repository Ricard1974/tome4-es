#!/usr/bin/env python3
"""Traduce TODOS los nombres de talentos y objetos."""

import re
from pathlib import Path

BASE = Path(__file__).parent.parent
TALENTS = BASE / "translations" / "es" / "mod-tome-split" / "data" / "talents"
OBJECTS = (
    BASE / "translations" / "es" / "mod-tome-split" / "data" / "general" / "objects"
)

# =============================================================================
# DICCIONARIO DE TALENTOS
# =============================================================================
TALENT_DICT = {
    # === Spells / Fire ===
    "Flame": "Llama",
    "Flameshock": "Descarga ígnea",
    "Fireflash": "Destello ígneo",
    "Inferno": "Infierno",
    "Burning Wake": "Estela ardiente",
    "Blastwave": "Onda expansiva",
    "Cleansing Flames": "Llamas purificadoras",
    "Wildfire": "Fuego salvaje",
    # === Spells / Ice ===
    "Freeze": "Congelar",
    "Ice Shards": "Fragmentos de hielo",
    "Ice Storm": "Tormenta de hielo",
    "Ice Armour": "Armadura de hielo",
    "Frozen Feet": "Pies congelados",
    "Glacial Vapour": "Vapor glacial",
    "Tidal Wave": "Ola gigante",
    "Flame of the Cold": "Llama del frío",
    # === Spells / Lightning ===
    "Lightning": "Relámpago",
    "Chain Lightning": "Cadena de relámpagos",
    "Feather Wind": "Viento de plumas",
    "Thunderstorm": "Tormenta eléctrica",
    "Hurricane": "Huracán",
    "Shock": "Descarga",
    # === Spells / Arcane ===
    "Manathrust": "Empuje de maná",
    "Arcane Power": "Poder arcano",
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
    "Teleport": "Teletransporte",
    "Phase Door": "Puerta dimensional",
    "Illuminate": "Iluminar",
    "Shatter": "Hacer añicos",
    "Stone": "Piedra",
    "Stone Wall": "Muro de piedra",
    "Earthquake": "Terremoto",
    "Pulverizing Auger": "Barrena pulverizadora",
    "Disintegrate": "Desintegrar",
    "Meteor": "Meteoro",
    "Temporal Shield": "Escudo temporal",
    # === Spells / Conveyance ===
    "Prophecy": "Profecía",
    "Prophecy of Ruin": "Profecía de ruina",
    "Prophecy of Treason": "Profecía de traición",
    "Prophecy of Madness": "Profecía de locura",
    # === Techniques / Combat ===
    "Rush": "Embestida",
    "Charge": "Carga",
    "Stun": "Aturdimiento",
    "Stunning Blow": "Golpe aturdidor",
    "Knockback": "Derribo",
    "Death Blow": "Golpe mortal",
    "Cripple": "Lisiar",
    "Maim": "Mutilar",
    "Hemorrhage": "Hemorragia",
    "Shattering Blow": "Golpe demoledor",
    "Shattering Impact": "Impacto demoledor",
    # === Techniques / Berserker ===
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
    "War Cry": "Grito de guerra",
    "Battle Cry": "Grito de batalla",
    "Savage Rush": "Embestida salvaje",
    # === Techniques / Rogue ===
    "Stealth": "Sigilo",
    "Hide in Plain Sight": "Ocultarse a plena vista",
    "Shadowstrike": "Golpe sombrío",
    "Backstab": "Apuñalar por la espalda",
    "Dual Strike": "Golpe dual",
    "Flurry": "Ráfaga",
    "Whirlwind": "Torbellino",
    "Sweep": "Barrido",
    "Knife Mastery": "Maestría en cuchillos",
    "Poison": "Veneno",
    "Apply Poison": "Aplicar veneno",
    "Virulent Disease": "Enfermedad virulenta",
    "Crippling Poison": "Veneno paralizante",
    # === Techniques / Archery ===
    "Shoot": "Disparar",
    "Aimed Shot": "Disparo apuntado",
    "Volley": "Lluvia de flechas",
    "Pin Down": "Inmovilizar",
    "Scatter Shot": "Disparo disperso",
    "Snipe": "Francotiro",
    "Explosive Shot": "Disparo explosivo",
    "Arrow Stitching": "Lluvia de flechas",
    "Barrage": "Barraje",
    # === Techniques / Shield ===
    "Shield Slam": "Golpe de escudo",
    "Shield Pummel": "Golpiza de escudo",
    "Bastion": "Baluarte",
    "Repulsion": "Repulsión",
    "Assault": "Asalto",
    "Block": "Bloquear",
    "Overpower": "Aplastar",
    # === Wild Gifts / Summoning ===
    "Summon": "Invocar",
    "War Hound": "Sabueso de guerra",
    "Minotaur": "Minotauro",
    "Stone Golem": "Gólem de piedra",
    "Fire Drake": "Dragón de fuego",
    "Ritch": "Ritch",
    "Jelly": "Babosa",
    "Spider": "Araña",
    "Turtle": "Tortuga",
    "Shade": "Sombra",
    "Rage": "Ira",
    "Detonate": "Detonar",
    # === Psionic / Mind ===
    "Mindlash": "Latigazo mental",
    "Mindwave": "Onda mental",
    "Mind Blast": "Explosión mental",
    "Mind Control": "Control mental",
    "Telekinetic": "Telequinético",
    "Telekinesis": "Telequinesis",
    "Psychic": "Psíquico",
    "Brain": "Cerebro",
    "Thought": "Pensamiento",
    "Dream": "Sueño",
    "Dreaming": "Soñar",
    "Dreamscape": "Paisaje onírico",
    "Distortion": "Distorsión",
    # === Cursed ===
    "Gloom": "Penumbra",
    "Fear": "Miedo",
    "Paranoia": "Paranoia",
    "Despair": "Desesperación",
    "Madness": "Locura",
    "Predator": "Depredador",
    "Stalk": "Acechar",
    "Savage": "Salvaje",
    "Torment": "Tormento",
    # === Celestial / Sun ===
    "Sun Ray": "Rayo solar",
    "Searing Light": "Luz abrasadora",
    "Healing Light": "Luz curativa",
    "Providence": "Providencia",
    "Bathe in Light": "Bañarse en luz",
    "Weapon of Light": "Arma de luz",
    "Weapon of Wrath": "Arma de ira",
    "Righteous": "Justo",
    "Chant": "Cántico",
    "Barrier": "Barrera",
    "Glyph": "Glifo",
    # === Corruptions ===
    "Blood": "Sangre",
    "Drain": "Drenar",
    "Soul Rot": "Podredumbre del alma",
    "Burning Sacrifice": "Sacrificio ardiente",
    "Dark Portal": "Portal oscuro",
    "Fearscape": "Páramo del miedo",
    "Abyssal Shield": "Escudo abismal",
    "Demon": "Demonio",
    # === Chronomancy ===
    "Timeless": "Intemporal",
    "Slow": "Ralentizar",
    "Haste": "Celeridad",
    "Speed": "Velocidad",
    "Cease to Exist": "Dejar de existir",
    "Age of Dusk": "Edad del ocaso",
    "Age of Twilight": "Edad del crepúsculo",
    "Stasis": "Estasis",
    "Energy": "Energía",
    # === Misc / Racial ===
    "Survival": "Supervivencia",
    "Devour": "Devorar",
    "Assimilate": "Asimilar",
    "Friendship": "Amistad",
    "Breed": "Reproducir",
}

# =============================================================================
# DICCIONARIO DE OBJETOS
# =============================================================================
OBJECT_DICT = {
    # Entity types
    "weapon": "arma",
    "armor": "armadura",
    "armour": "armadura",
    "potion": "poción",
    "scroll": "pergamino",
    "wand": "varita",
    "staff": "bastón",
    "gem": "gema",
    "ring": "anillo",
    "amulet": "amuleto",
    "belt": "cinturón",
    "cloak": "capa",
    "helm": "yelmo",
    "helmet": "casco",
    "gloves": "guantes",
    "boots": "botas",
    "tool": "herramienta",
    "digger": "excavadora",
    "ammo": "munición",
    "quiver": "carcaj",
    "light": "luz",
    "jewelry": "joyería",
    "money": "dinero",
    # Object types
    "iron": "hierro",
    "steel": "acero",
    "voratun": "voratún",
    "stralite": "estralita",
    "mithril": "mitril",
    "dragonbone": "dragón",
    "elven": "élfico",
    "reinforced": "reforzado",
    "hardened": "endurecido",
    "drakeskin": "dragón",
    "rough": "basto",
    "elm": "olmo",
    "ash": "fresno",
    "yew": "tejo",
}


def translate_file(filepath, dictionary):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    count = 0
    for orig, trans in sorted(dictionary.items(), key=lambda x: -len(x[0])):
        old = f't("{orig}", "{orig}",'
        new = f't("{orig}", "{trans}",'
        if old in content:
            content = content.replace(old, new)
            count += 1
    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO TALENTOS Y OBJETOS")
    print("=" * 60)
    total = 0

    # Talentos
    print("\n--- TALENTOS ---")
    talent_files = sorted(TALENTS.rglob("*.lua"))
    tf = 0
    for f in talent_files:
        c = translate_file(f, TALENT_DICT)
        if c > 0:
            rel = f.relative_to(TALENTS.parent.parent.parent)
            print(f"  {rel}: +{c}")
            tf += 1
            total += c
    print(f"  ({tf} archivos afectados)")

    # Objetos
    print("\n--- OBJETOS ---")
    object_files = sorted(OBJECTS.rglob("*.lua"))
    of = 0
    for f in object_files:
        c = translate_file(f, OBJECT_DICT)
        if c > 0:
            rel = f.relative_to(OBJECTS.parent.parent.parent)
            print(f"  {rel}: +{c}")
            of += 1
            total += c
    print(f"  ({of} archivos afectados)")

    print(f"\n  Total: {total} traducciones")


if __name__ == "__main__":
    main()
