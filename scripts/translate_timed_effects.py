#!/usr/bin/env python3
"""
FASE 2: Traduce timed_effects/* (physical, magical, mental, other, floor).
~2.232 cadenas de efectos de estado y mensajes de combate.

Uso: python3 scripts/translate_timed_effects.py
"""

import re
from pathlib import Path

EFFECTS_DIR = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "data"
    / "timed_effects"
)

# =============================================================================
# DICCIONARIO PARA EFECTOS FÍSICOS, MÁGICOS Y MENTALES
# =============================================================================
DICT = {
    # === Subtipos de efecto ===
    "acid": "ácido",
    "arcane": "arcano",
    "blight": "plaga",
    "cold": "frío",
    "darkness": "oscuridad",
    "disease": "enfermedad",
    "fire": "fuego",
    "light": "luz",
    "lightning": "relámpago",
    "nature": "naturaleza",
    "physical": "físico",
    "poison": "veneno",
    "temporal": "temporal",
    "mind": "mente",
    "mental": "mental",
    "magical": "mágico",
    # === Physical: subtipos ===
    "wound": "herida",
    "cut": "corte",
    "bleed": "sangrado",
    "healing": "curación",
    "regeneration": "regeneración",
    "stun": "aturdimiento",
    "knockback": "derribo",
    "pin": "inmovilización",
    "slow": "ralentización",
    "speed": "velocidad",
    "haste": "celeridad",
    "armour": "armadura",
    "armor": "armadura",
    "defense": "defensa",
    "resistance": "resistencia",
    "trap": "trampa",
    # === Magical: subtipos ===
    "sunder": "romper",
    "mana surge": "surge de maná",
    "dispel": "disipar",
    "shield": "escudo",
    "ward": "protección",
    "phase door": "puerta dimensional",
    "teleport": "teletransporte",
    "glow": "brillo",
    "illumination": "iluminación",
    "burn": "quemadura",
    "freeze": "congelación",
    "ice": "hielo",
    "blaze": "abrasar",
    # === Mental: subtipos ===
    "silence": "silencio",
    "confusion": "confusión",
    "fear": "miedo",
    "sleep": "sueño",
    "daze": "aturdimiento",
    "paranoia": "paranoia",
    "nightmare": "pesadilla",
    "gloom": "penumbra",
    "focus": "concentración",
    "disarm": "desarme",
    "exposed": "expuesto",
    # === Efectos físicos ===
    "Scoured": "Erosionado",
    "Scoured by natural acid, reducing their offensive power ratings by %d%%.": "Erosionado por ácido natural, reduciendo su poder ofensivo en %d%%.",
    "#Target#'s power is greatly reduced!": "¡El poder de #Target# se ha reducido enormemente!",
    "#Target# power has recovered.": "#Target# ha recuperado su poder.",
    "Relentless Tempo": "Tempo implacable",
    "All Resistance:  20%": "Todas las resistencias: 20%",
    "#Target# is gaining tempo.": "#Target# está cogiendo ritmo.",
    "+Tempo": "+Ritmo",
    "#Target# loses their tempo.": "#Target# pierde el ritmo.",
    "-Tempo": "-Ritmo",
    "Concussion": "Conmoción",
    "The target can't think straight, causing their actions to fail.": "El objetivo no puede pensar con claridad, sus acciones fallan.",
    "#Target#'s brain isn't quite working right!": "¡El cerebro de #Target# no funciona bien!",
    "+Concussion": "+Conmoción",
    "#Target# regains their concentration.": "#Target# recupera la concentración.",
    "-Concussion": "-Conmoción",
    "Bleeding": "Sangrado",
    "Huge cut that bleeds, doing %0.2f physical damage per turn.": "Gran corte sangrante que hace %0.2f de daño físico por turno.",
    "#Target# starts to bleed.": "#Target# empieza a sangrar.",
    "+Bleeds": "+Sangra",
    "#Target# stops bleeding.": "#Target# deja de sangrar.",
    "-Bleeds": "-Sangra",
    "Deep Wound": "Herida profunda",
    "Huge cut that bleeds, doing %0.2f physical damage per turn and decreasing all heals received by %d%%.": "Gran corte que sangra haciendo %0.2f de daño y reduciendo curaciones recibidas en %d%%.",
    "#Target# is cut deeply.": "#Target# está profundamente cortado.",
    "+Deep Wounds": "+Heridas profundas",
    "#Target#'s deep wound closes.": "La herida profunda de #Target# se cierra.",
    "-Deep Wounds": "-Heridas profundas",
    "Regeneration": "Regeneración",
    "A flow of life spins around the target, regenerating %0.2f life per turn.": "Un flujo de vida rodea al objetivo, regenerando %0.2f de vida por turno.",
    "#Target# starts regenerating health quickly.": "#Target# empieza a regenerar vida rápidamente.",
    "+Regen": "+Regen",
    "#Target# stops regenerating health quickly.": "#Target# deja de regenerar vida.",
    "-Regen": "-Regen",
    "Stunned": "Aturdido",
    "#Target# is stunned!": "¡#Target# está aturdido!",
    "+Stun": "+Aturdimiento",
    "#Target# is not stunned anymore.": "#Target# ya no está aturdido.",
    "-Stun": "-Aturdimiento",
    "Confused": "Confundido",
    "#Target# is confused!": "¡#Target# está confundido!",
    "+Confuse": "+Confusión",
    "#Target# is no longer confused.": "#Target# ya no está confundido.",
    "-Confuse": "-Confusión",
    "Pinned": "Inmovilizado",
    "#Target# is pinned!": "¡#Target# está inmovilizado!",
    "+Pinned": "+Inmovilizado",
    "#Target# is released from the pin.": "#Target# es liberado de la inmovilización.",
    "-Pinned": "-Inmovilizado",
    "Slowed": "Ralentizado",
    "+Slow": "+Ralentizado",
    "#Target# has left the slowing effect.": "#Target# ha salido del efecto de ralentización.",
    "-Slow": "-Ralentizado",
    "Dazed": "Atontado",
    "#Target# is dazed!": "¡#Target# está atontado!",
    "#Target# is no longer dazed.": "#Target# ya no está atontado.",
    "Silenced": "Silenciado",
    "#Target# is silenced!": "¡#Target# está silenciado!",
    "+Silenced": "+Silenciado",
    "#Target# is not silenced anymore.": "#Target# ya no está silenciado.",
    "-Silenced": "-Silenciado",
    "Blinded": "Cegado",
    "#Target# is blinded!": "¡#Target# está cegado!",
    "+Blind": "+Ceguera",
    "#Target# is no longer blinded.": "#Target# ya no está cegado.",
    "-Blind": "-Ceguera",
    "Disarmed": "Desarmado",
    "#Target# is disarmed!": "¡#Target# está desarmado!",
    "+Disarm": "+Desarme",
    "#Target# is no longer disarmed.": "#Target# ya no está desarmado.",
    "-Disarm": "-Desarme",
    "Knocked back": "Derribado",
    "#Target# is knocked back!": "¡#Target# es derribado!",
    "Saving": "Guardando",
    # === Efectos mágicos ===
    "Illness": "Enfermedad",
    "The target is infected by a disease, reducing its dexterity, strength, and constitution by %d.": "El objetivo está infectado por una enfermedad reduciendo su destreza, fuerza y constitución en %d.",
    "#Target# is afflicted by a crippling illness!": "¡#Target# está afectado por una enfermedad debilitante!",
    "#Target# is free from the illness.": "#Target# está libre de la enfermedad.",
    "Armor Corroded": "Armadura corroída",
    "The target has been splashed with acid, reducing armour by %d%% (#RED#%d#LAST#).": "El objetivo ha sido rociado con ácido reduciendo su armadura en %d%% (#RED#%d#LAST#).",
    "#Target#'s armor corrodes!": "¡La armadura de #Target# se corroe!",
    "#Target# is fully armored again.": "#Target# está completamente armado de nuevo.",
    "Surging mana": "Surge de maná",
    "The mana surge engulfs the target, regenerating %0.2f mana per turn.": "El surge de maná envuelve al objetivo regenerando %0.2f de maná por turno.",
    "#Target# starts to surge mana.": "#Target# empieza a surtir maná.",
    "+Manasurge": "+Surge de maná",
    "#Target# stops surging mana.": "#Target# deja de surtir maná.",
    "-Manasurge": "-Surge de maná",
    "Mana Overflow": "Desbordamiento de maná",
    "Mana surge near max values, granting a bonus to all spell damage of %d%%.": "Surge de maná cerca del máximo otorgando un bonus de %d%% a todo daño de hechizos.",
    "Decrepitude": "Decrepitud",
    "The target is infected by a disease, reducing its dexterity by %d and doing %0.2f blight damage per turn.": "El objetivo está infectado reduciendo su destreza en %d y haciendo %0.2f de daño de plaga por turno.",
    "Rotting Disease": "Enfermedad podrida",
    "The target is infected by a disease, reducing its constitution by %d and doing %0.2f blight damage per turn.": "El objetivo está infectado reduciendo su constitución en %d y haciendo %0.2f de daño de plaga por turno.",
    "Weakness Disease": "Enfermedad debilitante",
    "The target is infected by a disease, reducing its strength by %d and doing %0.2f blight damage per turn.": "El objetivo está infectado reduciendo su fuerza en %d y haciendo %0.2f de daño de plaga por turno.",
    "Burning": "Ardiendo",
    "#Target# is on fire!": "¡#Target# está en llamas!",
    "+Burn": "+Quemadura",
    "#Target# stops burning.": "#Target# deja de arder.",
    "-Burn": "-Quemadura",
    "Frozen": "Congelado",
    "#Target# is frozen!": "¡#Target# está congelado!",
    "+Freeze": "+Congelación",
    "#Target# is no longer frozen.": "#Target# ya no está congelado.",
    "-Freeze": "-Congelación",
    "Poisoned": "Envenenado",
    "#Target# is poisoned!": "¡#Target# está envenenado!",
    "+Poison": "+Veneno",
    "#Target# is no longer poisoned.": "#Target# ya no está envenenado.",
    "-Poison": "-Veneno",
    "Shocked": "Electrizado",
    "#Target# is shocked!": "¡#Target# está electrizado!",
    "Phase Door": "Puerta dimensional",
    # === Efectos mentales ===
    "Exposed": "Expuesto",
    "Mind and body exposed to effects and attacks, reducing all saves and defense by %d.": "Mente y cuerpo expuestos reduciendo todas las salvaciones y defensa en %d.",
    "#Target#'s is vulnerable to attacks and effects!": "¡#Target# es vulnerable a ataques y efectos!",
    "#Target# is less vulnerable.": "#Target# es menos vulnerable.",
    "Numbing Darkness": "Oscuridad entumecedora",
    "The target is losing hope, all damage it does is reduced by %d%%.": "El objetivo pierde la esperanza, todo su daño se reduce en %d%%.",
    "#Target# is weakened by the darkness!": "¡#Target# está debilitado por la oscuridad!",
    "+Numbing Darkness": "+Oscuridad entumecedora",
    "#Target# regains their energy.": "#Target# recupera su energía.",
    "-Numbing Darkness": "-Oscuridad entumecedora",
    "Sleeping": "Dormido",
    "#Target# is asleep!": "¡#Target# está dormido!",
    "#Target# wakes up.": "#Target# se despierta.",
    "Fear": "Miedo",
    "#Target# is stricken by fear!": "¡#Target# está aterrorizado!",
    "#Target# is no longer afraid.": "#Target# ya no tiene miedo.",
    "Paranoia": "Paranoia",
    "#Target# is paranoid!": "¡#Target# está paranoico!",
    "Terrified": "Aterrorizado",
    # === Varios ===
    "Something": "Algo",
    "saving": "guardando",
    "#Target# leaves the level.": "#Target# abandona el nivel.",
    "#Target# enters the level.": "#Target# entra al nivel.",
    "#Target# has died.": "#Target# ha muerto.",
    "#Target# has been slain.": "#Target# ha sido aniquilado.",
    "#Target# levels up!": "¡#Target# sube de nivel!",
    "#Target# appears.": "#Target# aparece.",
    "#Target# disappears.": "#Target# desaparece.",
    "#Target# teleports.": "#Target# se teletransporta.",
    "uncontrolled": "descontrolado",
    "wait": "esperar",
    "blind": "ciego",
    "dazed": "atontado",
    "encased in ice": "encerrado en hielo",
    "summon": "invocar",
    "summoned": "invocado",
    "on the ground": "en el suelo",
    "explode": "explotar",
    "explodes": "explota",
    "invisible": "invisible",
    "detect": "detectar",
    "track": "rastrear",
    "see invisible": "ver invisibilidad",
    "telepathy": "telepatía",
    "blindsight": "visión ciega",
    "hearing": "oído",
    "#Target# casts a spell.": "#Target# lanza un hechizo.",
    "#Target# uses a talent.": "#Target# usa un talento.",
    "#Target# uses %s.": "#Target# usa %s.",
    # === Más efectos físicos ===
    "frenzy": "frenesí",
    "tactic": "táctica",
    "curse": "maldición",
    "sense": "sentido",
    "heal": "cura",
    "cross tier": "nivel cruzado",
    "earth": "tierra",
    "evade": "evasión",
    "telekinesis": "telequinesis",
    "status": "estado",
    "morale": "moral",
    "cooldown": "enfriamiento",
    "spacetime": "espaciotiempo",
    "phantasm": "fantasmal",
    "circle": "círculo",
    "sun": "sol",
    "rune": "runa",
    "time": "tiempo",
    "elemental": "elemental",
    "dominate": "dominar",
    "power": "poder",
    "dirge": "elegía",
    "lich": "liche",
    "undead": "no-muerto",
    "Spydric Poison": "Veneno arácnido",
    "Insidious Poison": "Veneno insidioso",
    "Crippling Poison": "Veneno paralizante",
    "Numbing Poison": "Veneno entumecedor",
    "Stoning Poison": "Veneno petrificante",
    "Burning Shock": "Descarga ardiente",
    "Constricted": "Constreñido",
    "Evasion": "Evasión",
    "Speed": "Velocidad",
    "Marked for Death": "Marcado para la muerte",
    "Receptive Mind": "Mente receptiva",
    "Warden's Focus": "Enfoque del guardián",
    "Grappled": "Agarrado",
    "Grapple": "Agarre",
    "Swallowed": "Tragado",
    "#Target# speeds up.": "#Target# acelera.",
    "#Target# slows down.": "#Target# ralentiza.",
    "#Target# rearms.": "#Target# se rearma.",
    "#Target# loses sight!": "¡#Target# pierde la visión!",
    "#Target# recovers sight.": "#Target# recupera la visión.",
    "#Target# is crippled.": "#Target# está lisiado.",
    "#Target# is not crippled anymore.": "#Target# ya no está lisiado.",
    "#Target# hardens its skin.": "#Target# endurece su piel.",
    "#Target#'s skin returns to normal.": "La piel de #Target# vuelve a la normalidad.",
    "#Target# is in a deep sleep.": "#Target# está en un sueño profundo.",
    "#Target# is no longer sleeping.": "#Target# ya no está dormido.",
    "#Target# wanders around!": "¡#Target# deambula!",
    "#Target# seems more focused.": "#Target# parece más concentrado.",
    "You are yanked out of this place!": "¡Eres arrancado de este lugar!",
    "Space restabilizes around you.": "El espacio se reestabiliza a tu alrededor.",
    "#Target#'s awareness returns to normal.": "La percepción de #Target# vuelve a la normalidad.",
    "#Target# is doomed!": "¡#Target# está condenado!",
    "#Target# calms down.": "#Target# se calma.",
    "The target is immune to all detrimental effects.": "El objetivo es inmune a todos los efectos negativos.",
    "Improves senses, allowing the detection of unseen things.": "Mejora los sentidos permitiendo detectar cosas ocultas.",
    "antimagic": "antimagia",
    "Stun": "Aturdimiento",
    "Armor": "Armadura",
    "+Stunned": "+Aturdido",
    "-Stunned": "-Aturdido",
    "+Disarmed": "+Desarmado",
    "-Disarmed": "-Desarmado",
    "+Confused": "+Confundido",
    "-Confused": "-Confundido",
    "+Shield": "+Escudo",
    "-Shield": "-Escudo",
    "+Illumination": "+Iluminación",
    "-Illumination": "-Iluminación",
    "+Warden's Focus": "+Enfoque guardián",
    "-Warden's Focus": "-Enfoque guardián",
    "+Fast": "+Rápido",
    "-Fast": "-Rápido",
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
    print("  FASE 2: timed_effects/*")
    print("=" * 60)

    files = sorted(EFFECTS_DIR.glob("*.lua"))
    total = 0

    for fpath in files:
        count = translate_file(fpath)
        if count > 0:
            # Contar total en el archivo
            with open(fpath) as f:
                total_strs = sum(1 for line in f if re.match(r"t\(", line))
            print(f"  ✅ {fpath.name}: +{count} ({total_strs} total)")
            total += count

    print(f"\n  📊 Total en timed_effects: {total} traducciones")
    print()


if __name__ == "__main__":
    main()
