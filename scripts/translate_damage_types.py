#!/usr/bin/env python3
"""
FASE 1: Traduce damage_types.lua (339 cadenas).
Tipos de daño, verbos de muerte y mensajes de combate.

Uso: python3 scripts/translate_damage_types.py
"""

import re
from pathlib import Path

DAMAGE_FILE = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "data"
    / "damage_types.lua"
)

# =============================================================================
# TRADUCCIONES COMPLETAS
# =============================================================================
DICT = {
    # === Tipos de daño (damage type) ===
    "cosmetic": "cosmético",
    "cosmeticed": "cosmetizado",
    "physical": "físico",
    "arcane": "arcano",
    "fire": "fuego",
    "cold": "frío",
    "lightning": "relámpago",
    "acid": "ácido",
    "nature": "naturaleza",
    "blight": "plaga",
    "light": "luz",
    "darkness": "oscuridad",
    "mind": "mente",
    "temporal": "temporal",
    "winter": "invierno",
    "temporal stun": "aturdimiento temporal",
    "lite": "luz",
    "illumination": "iluminación",
    "silence": "silencio",
    "arcane silence": "silencio arcano",
    "blindness": "ceguera",
    "blinding ink": "tinta cegadora",
    "bright light": "luz brillante",
    "fire burn": "quemadura de fuego",
    "stunning fire": "fuego aturdidor",
    "devouring flames": "llamas devoradoras",
    "shadowflame": "llama sombría",
    "stunning darkness": "oscuridad aturdidora",
    "flameshock": "descarga ígnea",
    "ice": "hielo",
    "slowing ice": "hielo ralentizador",
    "ice storm": "tormenta de hielo",
    "glacial vapour": "vapor glacial",
    "pinning cold": "frío inmovilizador",
    "freeze": "congelación",
    "sticky smoke": "humo pegajoso",
    "acid blind": "ácido cegador",
    "blinding darkness": "oscuridad cegadora",
    "blinding light": "luz cegadora",
    "dazing lightning": "relámpago aturdidor",
    "cold repulsion": "repulsión de frío",
    "bloodspring": "manantial de sangre",
    "fire repulsion": "repulsión de fuego",
    "burning repulsion": "repulsión ardiente",
    "darkness repulsion": "repulsión de oscuridad",
    "physical repulsion": "repulsión física",
    "fear repulsion": "repulsión de miedo",
    "poison": "veneno",
    "cleansing fire": "fuego purificador",
    "spydric poison": "veneno arácnido",
    "crippling poison": "veneno paralizante",
    "insidious poison": "veneno insidioso",
    "bleed": "sangrado",
    "physical bleed": "sangrado físico",
    "nature slow": "ralentización natural",
    "dig": "cavar",
    "slow": "ralentización",
    "congeal time": "tiempo coagulado",
    "time prison": "prisión temporal",
    "confusion": "confusión",
    "% chance of confusion": "%% de confusión",
    "% chance of gloom effects": "%% de efectos de penumbra",
    "item darkness numbing": "oscuridad entumecedora",
    "item expose": "exposición",
    "item temporal energize": "energía temporal",
    "item acid corrode": "corrosión ácida",
    "item blight disease": "enfermedad de plaga",
    "item manaburn arcane": "quemamaná arcano",
    "item nature slow": "ralentización natural",
    "item antimagic scouring": "castigo antimágico",
    "item lightning daze": "aturdimiento eléctrico",
    "item light blind": "ceguera luminosa",
    "item mind gloom": "penumbra mental",
    "stun": "aturdimiento",
    "slow'": "ralentización",
    "blinding": "cegador",
    "blinding physical": "cegador físico",
    "physical pinning": "inmovilización física",
    "regressive blight": "plaga regresiva",
    "draining blight": "plaga drenante",
    "sanguine blight": "plaga sanguínea",
    "vim draining blight": "plaga drenante de vim",
    "demonfire": "fuego demoníaco",
    "purging blight": "plaga purgante",
    "holy light": "luz sagrada",
    "healing": "curación",
    "healing light": "luz curativa",
    "healing nature": "curación natural",
    "judgement": "juicio",
    "infective blight": "plaga infecciosa",
    "hindering blight": "plaga obstructora",
    "life leech": "drenavidas",
    "physical stun": "aturdimiento físico",
    "warp": "distorsión",
    "temporal darkness": "oscuridad temporal",
    "gravity": "gravedad",
    "gravity pin": "inmovilización gravitatoria",
    "grow": "crecer",
    "pinning nature": "inmovilización natural",
    "impeding nature": "naturaleza obstructora",
    "confounding nature": "naturaleza confusa",
    "sanctity": "sanctidad",
    "defensive darkness": "oscuridad defensiva",
    "blazing light": "luz abrasadora",
    "prismatic repulsion": "repulsión prismática",
    "mind slow": "ralentización mental",
    "mind freeze": "congelación mental",
    "implosion": "implosión",
    "regressive temporal": "temporal regresivo",
    "wasting temporal": "temporal debilitante",
    "stop": "parar",
    "debilitating temporal": "temporal debilitador",
    "draining physical": "drenaje físico",
    "temporal slow": "ralentización temporal",
    "molten rock": "roca fundida",
    "entangle": "enredar",
    "manaworm arcane": "lombriz de maná",
    "arcane blast": "explosión arcana",
    "circle of death": "círculo de muerte",
    "decaying darkness": "oscuridad decadente",
    "abyssal darkness": "oscuridad abismal",
    "% chance to summon an orc spirit": "%% de invocar espíritu orco",
    "nightmare": "pesadilla",
    "cursed miasma": "miasma maldito",
    "weakness": "debilidad",
    "special effect": "efecto especial",
    "manaburn arcane": "quemamaná arcano",
    "leaves": "hojas",
    "distorting physical": "distorsión física",
    "dreamforge": "forja de sueños",
    "natural mucus": "mucosidad natural",
    "disarming acid": "ácido desarmador",
    "corrosive acid": "ácido corrosivo",
    "bouncing slime": "babosa saltarina",
    "caustic mire": "lodazal cáustico",
    "sun path": "camino solar",
    "telekinetic shove": "empujón telequinético",
    "dimensional anchor": "ancla dimensional",
    "phase pulse": "pulso de fase",
    "brain storm": "tormenta cerebral",
    "static net": "red estática",
    "wormblight": "plaga de gusano",
    "pestilent blight": "plaga pestilente",
    "blight poison": "veneno de plaga",
    "terror": "terror",
    "random poison": "veneno aleatorio",
    "blinding powder": "polvo cegador",
    "smokescreen": "cortina de humo",
    "flare": "bengala",
    "flare light": "luz de bengala",
    "sticky pitch": "brea pegajosa",
    "fire sunder": "ruptura ígnea",
    "shadow smoke": "humo sombrío",
    "frozen earth": "tierra helada",
    "void echoes": "ecos del vacío",
    "#YELLOW#Lite Light#LAST# Burst (radius 1)": "#YELLOW#Luz#LAST# Explosión (radio 1)",
    "dark light": "luz oscura",
    "meteor": "meteoro",
    "fetid": "hediondo",
    "frostdusk": "ocaso helado",
    "chill of the tomb": "escalofrío de la tumba",
    "putrescent liquefaction": "licuefacción pútrida",
    "boneyard": "osario",
    "desolate waste": "páramo desolado",
    "thaumic energy": "energía táumica",
    "black-hole gravity": "gravedad de agujero negro",
    "solar blood": "sangre solar",
    # === Verbos de muerte ===
    "battered": "golpeado",
    "bludgeoned": "apaleado",
    "sliced": "rebanado",
    "maimed": "lisiado",
    "raked": "rasgado",
    "bled": "desangrado",
    "impaled": "empalado",
    "dissected": "disecado",
    "disembowelled": "destripado",
    "decapitated": "decapitado",
    "stabbed": "apuñalado",
    "pierced": "perforado",
    "torn limb from limb": "desmembrado",
    "crushed": "aplastado",
    "shattered": "hecho añicos",
    "smashed": "machacado",
    "cleaved": "hendido",
    "swiped": "barrido",
    "struck": "golpeado",
    "mutilated": "mutilado",
    "tortured": "torturado",
    "skewered": "ensartado",
    "squished": "apestado",
    "mauled": "zurrado",
    "chopped into tiny pieces": "cortado en pedazos",
    "splattered": "salpicado",
    "ground": "moltriturado",
    "minced": "picado",
    "punctured": "punzado",
    "hacked apart": "hachado",
    "eviscerated": "eviscerado",
    "blasted": "volado",
    "energised": "energizado",
    "mana-torn": "desgarrado por maná",
    "dweomered": "encantado",
    "imploded": "implosionado",
    "burnt": "quemado",
    "scorched": "chamuscado",
    "blazed": "abrasado",
    "roasted": "asado",
    "flamed": "llameado",
    "fried": "frito",
    "combusted": "combustionado",
    "toasted": "tostado",
    "slowly cooked": "cocinado lentamente",
    "boiled": "hervido",
    "frozen": "congelado",
    "chilled": "enfriado",
    "iced": "helado",
    "cooled": "refrigerado",
    "frozen and shattered into a million little shards": "congelado y hecho trizas",
    "electrocuted": "electrocutado",
    "shocked": "electrizado",
    "bolted": "fulminado",
    "volted": "voltado",
    "amped": "amplificado",
    "zapped": "chispado",
    "dissolved": "disuelto",
    "corroded": "corroído",
    "scalded": "escaldado",
    "melted": "derretido",
    "slimed": "embadurnado",
    "splurged": "embadurnado",
    "treehugged": "abrazado por árboles",
    "naturalised": "naturalizado",
    "diseased": "enfermado",
    "poxed": "empozado",
    "infected": "infectado",
    "plagued": "apestado",
    "debilitated by noxious blight before falling": "debilitado por plaga nociva antes de caer",
    "fouled": "ensuciado",
    "tainted": "contaminado",
    "radiated": "radiado",
    "seared": "sellado",
    "purified": "purificado",
    "sun baked": "soleado",
    "jerkied": "cecinado",
    "tanned": "curtido",
    "shadowed": "sombreído",
    "darkened": "oscurecido",
    "swallowed by the void": "tragado por el vacío",
    "psyched": "psicodelizado",
    "mentally tortured": "torturado mentalmente",
    "mindraped": "violado mentalmente",
    "timewarped": "deformado temporalmente",
    "temporally distorted": "distorsionado temporalmente",
    "spaghettified across the whole of space and time": "espaguetificado a través del espacio-tiempo",
    "paradoxed": "paradójado",
    "replaced by a time clone (and no one ever knew the difference)": "reemplazado por un clon temporal",
    "grandfathered": "ancestrado",
    "time dilated": "dilatado temporalmente",
    "utterly vaporized": "totalmente vaporizado",
    "annihilated": "aniquilado",
    "disintegrated": "desintegrado",
    # === Logs ===
    "Something": "Algo",
    "Frozen!": "¡Congelado!",
    "Resist!": "¡Resiste!",
    "orc spirit": "espíritu orco",
    "An orc clad in massive armour, wielding a huge axe.": "Un orco con armadura masiva, empuñando un hacha enorme.",
    "Garkul Spirit": "Espíritu de Garkul",
    # === Mensajes de combate (logSeen) ===
    "%s forces the iceblock to shatter.": "%s obliga al bloque de hielo a romperse.",
    "You end your target with a crushing blow!": "¡Acabas con tu objetivo de un golpe aplastante!",
    "%s resists the stun!": "¡%s resiste el aturdimiento!",
    "%s resists the silence!": "¡%s resiste el silencio!",
    "%s resists!": "¡%s resiste!",
    "%s resists the blinding light!": "¡%s resiste la luz cegadora!",
    "%s avoids the blinding ink!": "¡%s evita la tinta cegadora!",
    "%s resists the darkness!": "¡%s resiste la oscuridad!",
    "%s resists the searing flame!": "¡%s resiste la llama abrasadora!",
    "%s is knocked back!": "¡%s es derribado!",
    "%s resists the wave!": "¡%s resiste la oleada!",
    "%s resists the bloody wave!": "¡%s resiste la oleada de sangre!",
    "%s resists the punch!": "¡%s resiste el puñetazo!",
    "%s resists the knockback!": "¡%s resiste el derribo!",
    "%s resists the frightening sight!": "¡%s resiste la visión aterradora!",
    "%s turns into %s.": "%s se convierte en %s.",
    "%s resists the time prison.": "%s resiste la prisión temporal.",
    "%s resists the blind!": "¡%s resiste la ceguera!",
    "%s resists the sandstorm!": "¡%s resiste la tormenta de arena!",
    "%s resists the pin!": "¡%s resiste la inmovilización!",
    "%s resists the pinning!": "¡%s resiste la inmovilización!",
    "%s resists the confusion!": "¡%s resiste la confusión!",
    "%s resists the freezing!": "¡%s resiste la congelación!",
    "%s has not been stopped!": "¡%s no ha sido detenido!",
    "%s resists the blindness!": "¡%s resiste la ceguera!",
    "%s resists entanglement!": "¡%s resiste el enredo!",
    "%s has no mana to burn.": "%s no tiene maná que quemar.",
    "%s resists the baneful energy!": "¡%s resiste la energía nefasta!",
    "%s resists the forge bellow!": "¡%s resiste el rugido de la forja!",
    "%s resists the dream forge!": "¡%s resiste la forja de sueños!",
    "%s resists disarming!": "¡%s resiste el desarme!",
    "%s resists pinning!": "¡%s resiste la inmovilización!",
    "%s resists the shove!": "¡%s resiste el empujón!",
    "%s resists the mind attack!": "¡%s resiste el ataque mental!",
    "%s resists the blinding flare!": "¡%s resiste la bengala cegadora!",
    "%s resists the void!": "¡%s resiste el vacío!",
    "%s is pulled in!": "¡%s es atraído!",
    "%s resists the gravity!": "¡%s resiste la gravedad!",
    # === Logs de combate (logCombat) ===
    "#Source# drains life from #Target#!": "¡#Source# drena vida de #Target#!",
    "#Source# drains experience from #Target#!": "¡#Source# drena experiencia de #Target#!",
    "#Source# consumes %d life from #Target#!": "¡#Source# consume %d de vida de #Target#!",
    # === Logs del jugador (logPlayer) ===
    "#DARK_ORCHID#Your damage shield cannot be extended any farther and has exploded.": "#DARK_ORCHID#Tu escudo de daño no puede extenderse más y ha explotado.",
    # === Logs retrasados (delayedLogMessage) ===
    "#Source# strikes #Target# in the darkness (%+d%%%%%%%% damage).": "#Source# golpea a #Target# en la oscuridad (%+d%%%% de daño).",
    "#CRIMSON##Source# damages %s through Martyrdom!": "#CRIMSON##Source# daña a %s mediante Martirio!",
    "#CRIMSON##Source# reflects damage back to #Target#!": "#CRIMSON##Source# refleja el daño de vuelta a #Target#!",
    # === Format strings (tformat) ===
    "%s(%d warded)#LAST#": "%s(%d protegido)#LAST#",
    "%s(%d to psi shield)#LAST#": "%s(%d a escudo psi)#LAST#",
    "%s(%d blocked)#LAST#": "%s(%d bloqueado)#LAST#",
    "%s(%d abyssal shield)#LAST#": "%s(%d escudo abismal)#LAST#",
    "%s(%d antimagic)#LAST#": "%s(%d antimagia)#LAST#",
    "%s(%d flat reduction)#LAST#": "%s(%d reducción plana)#LAST#",
    "#LIGHT_GREY#(%d resilience)#LAST#": "#LIGHT_GREY#(%d resistencia)#LAST#",
    "#Source##LIGHT_GREEN# HEALS#LAST# from %s %s #LAST# damage!": "¡#Source##LIGHT_GREEN# SE CURA#LAST# de %s %s #LAST# de daño!",
    "* #LIGHT_GREEN#%d%%#LAST# chance to reduce damage dealt by #YELLOW#%d%%#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de reducir daño en #YELLOW#%d%%#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to reduce all saves and defense by #YELLOW#%d#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de reducir salvaciones y defensa en #YELLOW#%d#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to gain 10%% of a turn (3/turn limit)%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de ganar 10%% de turno (límite 3/turno)%s",
    "#LIGHT_STEEL_BLUE#%s can't gain any more energy this turn! ": "#LIGHT_STEEL_BLUE#%s no puede ganar más energía este turno! ",
    "* #LIGHT_GREEN#%d%%#LAST# chance to reduce armor by #VIOLET#%d%%#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de reducir armadura en #VIOLET#%d%%#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to reduce strength, dexterity, and constitution by #VIOLET#%d#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de reducir fuerza, destreza y constitución en #VIOLET#%d#LAST#%s",
    "* #DARK_ORCHID#%d arcane resource#LAST# burn%s": "* #DARK_ORCHID#%d recurso arcano#LAST# quemado%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to slow global speed by #YELLOW#%d%%#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de ralentizar velocidad global en #YELLOW#%d%%#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to #ORCHID#reduce effective powers#LAST# by %d%%%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de #ORCHID#reducir poderes#LAST# en %d%%%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to #ROYAL_BLUE#daze#LAST# at end of turn%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de #ROYAL_BLUE#atontar#LAST# al final del turno%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to #YELLOW#blind#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de #YELLOW#cegar#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to cause #YELLOW#random gloom#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de causar #YELLOW#penumbra aleatoria#LAST#%s",
    "* #LIGHT_GREEN#%d%%#LAST# chance to cause #GREEN#random blight#LAST#%s": "* #LIGHT_GREEN#%d%%#LAST# prob. de causar #GREEN#plaga aleatoria#LAST#%s",
    "%s<%d%%%% orc summon chance>#LAST#": "%s<%d%%%% prob. invocación orco>#LAST#",
    "%s<orc summon>#LAST#": "%s<invocar orco>#LAST#",
    "%s<terror chance>#LAST#": "%s<prob. terror>#LAST#",
    "%s<blinding powder>#LAST#": "%s<polvo cegador>#LAST#",
    "%s<smoke>#LAST#": "%s<humo>#LAST#",
}


def translate_file():
    with open(DAMAGE_FILE, "r", encoding="utf-8") as f:
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

    with open(DAMAGE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return count


def main():
    print("=" * 60)
    print("  FASE 1: damage_types.lua")
    print("=" * 60)

    count = translate_file()
    print(f"\n  ✅ {count} cadenas traducidas")

    with open(DAMAGE_FILE) as f:
        remaining = sum(1 for line in f if re.match(r't\("([^"]*)",\s*"\1"', line))
    print(f"  📊 Quedan {remaining} sin traducir")
    print()


if __name__ == "__main__":
    main()
