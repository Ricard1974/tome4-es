#!/usr/bin/env python3
"""
Genera un diccionario masivo de términos del juego para ToME4-es.
Usa reglas lingüísticas para traducir nombres de objetos, entidades y términos.

Uso: python3 scripts/generate_dictionary.py
"""

# =============================================================================
# GENERADOR DE DICCIONARIO MASIVO
# =============================================================================


def generate_dictionary():
    """Genera un diccionario EN→ES con términos de juego."""
    d = {}

    # === Materiales + objeto ===
    materials = {
        "iron": "hierro",
        "steel": "acero",
        "silver": "plata",
        "gold": "oro",
        "mithril": "mitril",
        "voratun": "voratún",
        "stralite": "estralita",
        "bronze": "bronce",
        "copper": "cobre",
        "bone": "hueso",
        "leather": "cuero",
        "rough leather": "cuero basto",
        "hardened leather": "cuero endurecido",
        "drakeskin leather": "cuero de dragón",
        "woollen": "lana",
        "linen": "lino",
        "silk": "seda",
        "cloth": "tela",
        "velvet": "terciopelo",
        "elm": "olmo",
        "ash": "fresno",
        "yew": "tejo",
        "poplar": "álamo",
        "oak": "roble",
        "coral": "coral",
        "crystal": "cristal",
        "diamond": "diamante",
        "ruby": "rubí",
        "sapphire": "zafiro",
        "emerald": "esmeralda",
        "amethyst": "amatista",
        "quartz": "cuarzo",
        "opal": "ópalo",
        "jet": "azabache",
        "amber": "ámbar",
    }

    # === Tipos de objeto ===
    items = {
        "longsword": "espada larga",
        "shortsword": "espada corta",
        "greatsword": "espada bastarda",
        "bastard sword": "espada bastarda",
        "waraxe": "hacha de guerra",
        "battleaxe": "hacha de batalla",
        "great axe": "gran hacha",
        "hand axe": "hacha de mano",
        "mace": "maza",
        "warhammer": "martillo de guerra",
        "great mace": "gran maza",
        "dagger": "daga",
        "knife": "cuchillo",
        "whip": "látigo",
        "bow": "arco",
        "longbow": "arco largo",
        "shortbow": "arco corto",
        "sling": "honda",
        "staff": "bastón",
        "magestaff": "bastón de mago",
        "vilestaff": "bastón vil",
        "starstaff": "bastón estelar",
        "shield": "escudo",
        "buckler": "broquel",
        "helmet": "casco",
        "helm": "yelmo",
        "cap": "gorro",
        "hat": "sombrero",
        "gloves": "guantes",
        "gauntlets": "guanteletes",
        "boots": "botas",
        "shoes": "zapatos",
        "greaves": "grebas",
        "sandals": "sandalias",
        "cloak": "capa",
        "robe": "túnica",
        "vestment": "vestidura",
        "armour": "armadura",
        "mail armour": "cota de malla",
        "plate armour": "armadura de placas",
        "leather armour": "armadura de cuero",
        "belt": "cinturón",
        "sash": "fajín",
        "ring": "anillo",
        "amulet": "amuleto",
        "torque": "torque",
        "totem": "tótem",
        "spell": "hechizo",
        "orb": "orbe",
        "pearl": "perla",
        "potion": "poción",
        "elixir": "elixir",
        "scroll": "pergamino",
        "rune": "runa",
        "infusion": "infusión",
        "wand": "varita",
        "rod": "vara",
        "pickaxe": "pico",
        "digger": "excavadora",
        "arrow": "flecha",
        "arrows": "flechas",
        "shot": "proyectil",
        "shots": "proyectiles",
        "bolt": "virote",
        "bolts": "virotes",
        "quiver": "carcaj",
        "pouch": "saco",
        "bag": "bolsa",
        "satchel": "mochila",
        "lamp": "lámpara",
        "lantern": "linterna",
        "tool": "herramienta",
        "pick": "pico",
        "trap": "trampa",
        "trap component": "componente de trampa",
    }

    # Generar combinaciones material + objeto
    for mat_en, mat_es in materials.items():
        for item_en, item_es in items.items():
            key = f"{mat_en} {item_en}"
            val = f"{item_es} de {mat_es}"
            d[key] = val
            # Versión capitalizada
            if mat_en[0].isupper():
                d[key.title()] = val[0].upper() + val[1:]

    # === Razas ===
    races = {
        "humanoid": "humanoide",
        "human": "humano",
        "elf": "elfo",
        "dark elf": "elfo oscuro",
        "dwarf": "enano",
        "halfling": "mediano",
        "orc": "orco",
        "orc master": "maestro orco",
        "orc elite": "élite orca",
        "orc warrior": "guerrero orco",
        "orc beserker": "berserker orco",
        "troll": "trol",
        "ogre": "ogro",
        "giant": "gigante",
        "skeleton": "esqueleto",
        "ghoul": "ghul",
        "lich": "liche",
        "vampire": "vampiro",
        "zombie": "zombi",
        "demon": "demonio",
        "demonic": "demoníaco",
        "dragon": "dragón",
        "wyrm": "dragón",
        "wurm": "gusano",
        "spider": "araña",
        "snake": "serpiente",
        "wolf": "lobo",
        "warg": "huargo",
        "bear": "oso",
        "tiger": "tigre",
        "lion": "león",
        "panther": "pantera",
        "rat": "rata",
        "giant rat": "rata gigante",
        "bat": "murciélago",
        "fire imp": "diablillo de fuego",
        "golem": "gólem",
        "construct": "constructo",
        "elemental": "elemental",
        "golem": "gólem",
        "eye": "ojo",
        "floating eye": "ojo flotante",
        "gelatinous cube": "cubo gelatinoso",
        "slime": "babosa",
        "ooze": "limo",
        "wight": "espectro",
        "ghost": "fantasma",
        "shade": "sombra",
        "phantom": "fantasma",
        "will o' the wisp": "fuego fatuo",
        "crab": "cangrejo",
        "turtle": "tortuga",
        "bee": "abeja",
        "queen bee": "abeja reina",
        "ant": "hormiga",
        "giant ant": "hormiga gigante",
        "fly": "mosca",
        "mosquito": "mosquito",
        "wasp": "avispa",
        "scorpion": "escorpión",
    }

    for en, es in races.items():
        d[en] = es
        d[en.capitalize()] = es.capitalize()

    # === Adjetivos de objeto ===
    prefixes = {
        "flaming": "llameante",
        "freezing": "helado",
        "shocking": "electrificante",
        "acidic": "ácido",
        "venomous": "venenoso",
        "corrosive": "corrosivo",
        "flame": "llama",
        "frost": "escarcha",
        "storm": "tormenta",
        "thunder": "trueno",
        "wrathful": "iracundo",
        "vengeful": "vengativo",
        "mighty": "poderoso",
        "giant": "gigante",
        "guardian": "guardián",
        "sentry": "centinela",
        "warden": "vigilante",
        "protector": "protector",
        "impervious": "impenetrable",
        "invulnerable": "in vulnerable",
        "reinforced": "reforzado",
        "hardened": "endurecido",
        "thick": "grueso",
        "heavy": "pesado",
        "light": "ligero",
        "fine": "fino",
        "shimmering": "centelleante",
        "glowing": "brillante",
        "radiant": "radiante",
        "shining": "resplandeciente",
        "shadowy": "sombrío",
        "gloom": "penumbra",
        "darkness": "oscuridad",
        "eclipsed": "eclipsado",
        "corrupted": "corrupto",
        "tainted": "infecto",
        "defiled": "profanado",
        "unholy": "profano",
        "consecrated": "consagrado",
        "blessed": "bendito",
        "saintly": "santo",
        "divine": "divino",
        "ancient": "ancestral",
        "elven": "élfico",
        "dwarven": "enano",
        "orcish": "orco",
        "knight": "caballero",
        "royal": "real",
        "kingly": "regio",
        "lordly": "señorial",
        "sage": "sabio",
        "scholar": "erudito",
        "mystic": "místico",
        "occult": "oculto",
        "arcane": "arcano",
        "magical": "mágico",
        "elvenkind": "élfico",
        "draconic": "draconiano",
        "dragonbone": "de dragón",
    }

    for en, es in prefixes.items():
        d[en] = es
        d[en.capitalize()] = es.capitalize()

    # === Tipos de daño ===
    damage_types = {
        "physical": "físico",
        "fire": "fuego",
        "cold": "frío",
        "lightning": "relámpago",
        "acid": "ácido",
        "nature": "naturaleza",
        "blight": "plaga",
        "arcane": "arcano",
        "light": "luz",
        "darkness": "oscuridad",
        "temporal": "temporal",
        "mind": "mente",
        "poison": "veneno",
        "bleed": "sangrado",
        "disease": "enfermedad",
        "cut": "corte",
        "crushing": "aplastante",
        "piercing": "perforante",
        "slashing": "cortante",
        "fireburn": "quemadura",
        "cold ice": "hielo",
    }

    for en, es in damage_types.items():
        d[en] = es
        d[en.capitalize()] = es.capitalize()
        d[f"{en} damage"] = f"daño {es}"
        d[f"{en.capitalize()} damage"] = f"Daño {es.capitalize()}"

    return d


if __name__ == "__main__":
    d = generate_dictionary()
    print(f"Generated {len(d)} dictionary entries")
    # Mostrar algunos ejemplos
    examples = [
        "iron longsword",
        "steel plate armour",
        "rough leather boots",
        "elm magestaff",
        "voratun shield",
        "dragonbone bow",
        "ancient elven sword",
        "flaming iron dagger",
        "shimmering silk robe",
        "reinforced steel shield",
    ]
    for e in examples:
        print(f"  {e} -> {d.get(e, '?')}")
