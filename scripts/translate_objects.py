#!/usr/bin/env python3
"""
FASE 4: Traduce objetos (data/general/objects/*).
~2.116 cadenas de nombres, descripciones y tipos de objetos.

Uso: python3 scripts/translate_objects.py
"""

import re
from pathlib import Path

OBJECTS_DIR = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "data"
    / "general"
    / "objects"
)

# =============================================================================
# DICCIONARIO DE TÉRMINOS DE OBJETOS
# =============================================================================
DICT = {
    # === Entity types ===
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
    "cap": "gorro",
    "gloves": "guantes",
    "gauntlets": "guanteletes",
    "boots": "botas",
    "shoes": "zapatos",
    "greaves": "grebas",
    "digger": "excavadora",
    "tool": "herramienta",
    "lore": "texto histórico",
    "gem": "gema",
    "light": "luz",
    "lites": "luces",
    "ammo": "munición",
    "quiver": "carcaj",
    # === Subtypes ===
    "waraxe": "hacha de guerra",
    "axe": "hacha",
    "sword": "espada",
    "greatsword": "espada bastarda",
    "mace": "maza",
    "morningstar": "estrella matutina",
    "knife": "cuchillo",
    "dagger": "daga",
    "trident": "tridente",
    "bow": "arco",
    "sling": "honda",
    "feet": "pies",
    "head": "cabeza",
    "hands": "manos",
    "belt": "cinturón",
    "jewelry": "joyería",
    # === Combat talents ===
    "axe": "hacha",
    "sword": "espada",
    "mace": "maza",
    # === Short names (material abbreviations) ===
    "iron": "hierro",
    "steel": "acero",
    "d.steel": "ac.dw",
    "dwarven-steel": "acero enano",
    "stralite": "estralita",
    "voratun": "voratún",
    "rough": "basto",
    "hardened": "endurecido",
    "drakeskin": "dragón",
    "elm": "olmo",
    "ash": "fresno",
    "yew": "tejo",
    "poplar": "álamo",
    "oak": "roble",
    "silk": "seda",
    "wool": "lana",
    "linen": "lino",
    "cloth": "tela",
    "copper": "cobre",
    "silver": "plata",
    "gold": "oro",
    "mithril": "mitril",
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
    "bone": "hueso",
    "reinforced": "reforzado",
    "spider": "araña",
    "wyrm": "dragón",
    "dragonbone": "dragón",
    "dragon": "dragón",
    # === Nombres de objetos compuestos ===
    "iron waraxe": "hacha de guerra de hierro",
    "steel waraxe": "hacha de guerra de acero",
    "dwarven-steel waraxe": "hacha de guerra de acero enano",
    "stralite waraxe": "hacha de guerra de estralita",
    "voratun waraxe": "hacha de guerra de voratún",
    "iron battleaxe": "hacha de batalla de hierro",
    "steel battleaxe": "hacha de batalla de acero",
    "iron greatsword": "espada bastarda de hierro",
    "steel greatsword": "espada bastarda de acero",
    "iron longsword": "espada larga de hierro",
    "steel longsword": "espada larga de acero",
    "iron mace": "maza de hierro",
    "steel mace": "maza de acero",
    "iron dagger": "daga de hierro",
    "steel dagger": "daga de acero",
    "elm magestaff": "bastón de mago de olmo",
    "elm vilestaff": "bastón vil de olmo",
    "elm starstaff": "bastón estelar de olmo",
    "elm longbow": "arco largo de olmo",
    "rough sling": "honda basta",
    "quiver of elm arrows": "carcaj de flechas de olmo",
    "pouch of iron shots": "saco de proyectiles de hierro",
    "pair of rough leather boots": "par de botas de cuero basto",
    "pair of hardened leather boots": "par de botas de cuero endurecido",
    "pair of drakeskin leather boots": "par de botas de cuero de dragón",
    "rough leather gloves": "guantes de cuero basto",
    "iron gauntlets": "guanteletes de hierro",
    "steel gauntlets": "guanteletes de acero",
    "linen cloak": "capa de lino",
    "woollen robe": "túnica de lana",
    "silk robe": "túnica de seda",
    "iron helm": "yelmo de hierro",
    "steel helm": "yelmo de acero",
    "rough leather cap": "gorro de cuero basto",
    "iron shield": "escudo de hierro",
    "steel shield": "escudo de acero",
    "iron mail armour": "cota de malla de hierro",
    "steel mail armour": "cota de malla de acero",
    "iron plate armour": "armadura de placas de hierro",
    "steel plate armour": "armadura de placas de acero",
    "iron pickaxe": "pico de hierro",
    "steel pickaxe": "pico de acero",
    "brass lantern": "linterna de latón",
    "alchemist's lamp": "lámpara de alquimista",
    # === Descripciones ===
    "One-handed war axes.": "Hachas de guerra de una mano.",
    "One-handed maces.": "Mazas de una mano.",
    "One-handed axes.": "Hachas de una mano.",
    "One-handed swords.": "Espadas de una mano.",
    "Two-handed axes.": "Hachas a dos manos.",
    "Two-handed maces.": "Mazas a dos manos.",
    "Two-handed swords.": "Espadas a dos manos.",
    "Two-handed tridents.": "Tridentes a dos manos.",
    "Bows to shoot arrows with.": "Arcos para disparar flechas.",
    "Slings to shoot bullets with.": "Hondas para disparar balas.",
    "Daggers and other small blades.": "Dagas y otras hojas pequeñas.",
    "A pair of boots made of leather.": "Un par de botas de cuero.",
    "Gloves are hand armours ; they take the hands slot.": "Los guantes son armadura para las manos.",
    "Gauntlets are hand armours ; they take the hands slot.": "Los guanteletes son armadura para las manos.",
    "A cloth armour to wear over your clothes.": "Una armadura de tela para llevar sobre la ropa.",
    "A cloak to wear over your equipment.": "Una capa para llevar sobre tu equipo.",
    "A helmet to wear on your head.": "Un casco para llevar en la cabeza.",
    "A cap to wear on your head.": "Un gorro para llevar en la cabeza.",
    "An amulet to wear around your neck.": "Un amuleto para llevar al cuello.",
    "A ring to wear on your finger.": "Un anillo para llevar en el dedo.",
    "Helms to protect your head.": "Yelmos para proteger tu cabeza.",
    "Belts to wear around your waist.": "Cinturones para llevar a la cintura.",
    "Leather boots to wear on your feet.": "Botas de cuero para llevar en los pies.",
    "Heavy boots to wear on your feet.": "Botas pesadas para los pies.",
    "Vests, shirts and other clothes to protect your body.": "Chalecos y camisas para proteger tu cuerpo.",
    "Light armours to protect your body.": "Armaduras ligeras para proteger tu cuerpo.",
    "Heavy armours to protect your body.": "Armaduras pesadas para proteger tu cuerpo.",
    "Lights to light up your surroundings.": "Luces para iluminar tu entorno.",
    "Jewelry to wear on your fingers and around your neck.": "Joyas para llevar en los dedos y el cuello.",
    "Digging tools.": "Herramientas de excavación.",
    "Potions and elixirs.": "Pociones y elixires.",
    "A pickaxe to dig with.": "Un pico para excavar.",
    "Magical potions can have wildly different effects, from healing to killing you -- beware! Most of them function better with a high Magic score.": "Las pociones mágicas pueden tener efectos muy diversos, desde curarte hasta matarte. La mayoría funcionan mejor con una puntuación de Magia alta.",
    "Staves are magical weapons.": "Los bastones son armas mágicas.",
    "Magical wands.": "Varitas mágicas.",
    "Magical scrolls.": "Pergaminos mágicos.",
    "Gems to socket into items.": "Gemas para engarzar en objetos.",
    # === Misc ===
    "potion": "poción",
    "weapon": "arma",
    "armor": "armadura",
    "feet": "pies",
    "hands": "manos",
    "head": "cabeza",
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
    print("  FASE 4: objetos (data/general/objects/*)")
    print("=" * 60)

    # Archivos de objetos y subdirectorios
    files = sorted(OBJECTS_DIR.rglob("*.lua"))
    total = 0
    affected = 0

    for fpath in files:
        count = translate_file(fpath)
        if count > 0:
            print(
                f"  ✅ {fpath.relative_to(OBJECTS_DIR.parent.parent.parent.parent)}: +{count}"
            )
            total += count
            affected += 1

    print(f"\n  📊 Total: {total} traducciones en {affected} archivos")
    print()


if __name__ == "__main__":
    main()
