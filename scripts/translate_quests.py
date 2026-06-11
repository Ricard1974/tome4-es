#!/usr/bin/env python3
"""
FASE 5: Traduce misiones (data/quests/*).
~480 cadenas de nombres y descripciones de misiones.

Uso: python3 scripts/translate_quests.py
"""

import re
from pathlib import Path

QUESTS_DIR = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "data"
    / "quests"
)

# =============================================================================
# DICCIONARIO DE MISIONES
# =============================================================================
DICT = {
    # === Nombres de misiones ===
    "The Arena": "La Arena",
    "The Island of Dread": "La Isla del Pavor",
    "Dreadfell": "Pavorosa",
    "Seeking wealth, glory, and a great fight, you challenge the Arena!": "Buscando riqueza, gloria y una gran batalla, ¡desafías a la Arena!",
    "Can you defeat your foes and become Master of Arena?": "¿Puedes derrotar a tus enemigos y convertirte en Maestro de la Arena?",
    "Winner": "Ganador",
    "#GOLD#Well done! You have won the Arena: Challenge of the Master#WHITE#": "#GOLD#¡Bien hecho! Has ganado la Arena: Desafío del Maestro#WHITE#",
    "You valiantly fought every creature the arena could throw at you and you emerged victorious!": "¡Luchaste valientemente contra todas las criaturas de la Arena y saliste victorioso!",
    "Glory to you, you are now the new master and your future characters will challenge you.": "Gloria a ti, ahora eres el nuevo maestro y tus futuros personajes te desafiarán.",
    "You have heard that near the Charred Scar, to the south, lies a ruined tower known as the Dreadfell.": "Has oído que cerca de la Cicatriz Carbonizada, al sur, hay una torre en ruinas conocida como la Pavorosa.",
    "There are disturbing rumors of greater undead, and nobody who reached it ever returned.": "Hay rumores perturbadores de no-muertos poderosos, y nadie que llegó allí regresó jamás.",
    "Perhaps you should explore it and find the truth, and the treasures, for yourself!": "¡Quizás deberías explorarla y descubrir la verdad, y los tesoros, por ti mismo!",
    "The Brotherhood of Alchemists": "La Hermandad de Alquimistas",
    "Brotherhood of Alchemists": "Hermandad de Alquimistas",
    "Escort duty": "Escolta",
    "Escort Duty": "Escolta",
    "The Orbs of Command": "Los Orbes de Mando",
    "Orb Command": "Orbe de Mando",
    "The Sunwall": "El Muro Solar",
    "The Eastern Portals": "Los Portales del Este",
    "Eastern Portals": "Portales del Este",
    "The West Portals": "Los Portales del Oeste",
    "West Portals": "Portales del Oeste",
    "The Lichform": "La Forma de Liche",
    "Lichform": "Forma de Liche",
    "Melinda's love": "El amor de Melinda",
    "Love Melinda": "Amar a Melinda",
    "The lost merchant": "El mercader perdido",
    "The Mage Apprentice": "El Aprendiz de Mago",
    "Mage Apprentice": "Aprendiz de Mago",
    "The Master Jeweler": "El Maestro Joyero",
    "Master Jeweler": "Maestro Joyero",
    "The Arena unlock": "Desbloqueo de la Arena",
    "The Arena's secrets": "Los secretos de la Arena",
    "Spydric Infestation": "Infestación Arácnida",
    "The Spydric Infestation": "La Infestación Arácnida",
    "The Deep Bellow": "El Rugido Profundo",
    "Deep Bellow": "Rugido Profundo",
    "The Temple of Creation": "El Templo de la Creación",
    "Temple of Creation": "Templo de la Creación",
    "A strange new world": "Un extraño nuevo mundo",
    "Strange New World": "Extraño Nuevo Mundo",
    "The Trollmire Treasure": "El Tesoro del Trolmarlo",
    "Trollmire Treasure": "Tesoro del Trolmarlo",
    "The Vault of Sher'Tul": "La Bóveda de Sher'Tul",
    "Sher'Tul Fortress": "Fortaleza Sher'Tul",
    "Circle of Death": "Círculo de Muerte",
    "The Grave Necromancer": "El Nigromante de la Tumba",
    "Grave Necromancer": "Nigromante de la Tumba",
    "The Lightning Overload": "La Sobrecarga Eléctrica",
    "Lightning Overload": "Sobrecarga Eléctrica",
    "The Orc Breed Pits": "Las Fosas de Cría Orcas",
    "Orc Breeding Pits": "Fosas de Cría Orcas",
    "The Orc Hunt": "La Cacería de Orcos",
    "Orc Hunt": "Cacería de Orcos",
    "The Orc Prides": "Los Orgullos Orcos",
    "Orc Prides": "Orgullos Orcos",
    "The High Peak": "El Pico Alto",
    "High Peak": "Pico Alto",
    "The Ring of Blood": "El Anillo de Sangre",
    "Ring of Blood": "Anillo de Sangre",
    "The Temporal Rift": "La Grieta Temporal",
    "Temporal Rift": "Grieta Temporal",
    "Paradoxology": "Paradoxología",
    "The Infinite Dungeon": "La Mazmorra Infinita",
    "Infinite Dungeon": "Mazmorra Infinita",
    "The Lumberjack's Curse": "La Maldición del Leñador",
    "The KeepSake's Meadow": "El Prado del Recuerdo",
    "KeepSake": "Recuerdo",
    "The War in the East": "La Guerra en el Este",
    "The Rel Tunnels": "Los Túneles Rel",
    "The Void Gerlyk": "El Gerlyk del Vacío",
    "Void Gerlyk": "Gerlyk del Vacío",
    "Alchemy Scroll": "Pergamino de Alquimia",
    "Anti-Antimagic": "Anti-Antimagia",
    "Off to the East": "Hacia el Este",
    "Wild, wild, east": "Salvaje, salvaje este",
    "Wild Wild East": "Salvaje Salvaje Este",
    "Staff of Absorption": "Bastón de Absorción",
    "The staff of Absorption": "El Bastón de Absorción",
    "Into the void": "Hacia el vacío",
    "The Charred Scar": "La Cicatriz Carbonizada",
    "Before Charred Scar": "Antes de la Cicatriz Carbonizada",
    "Pre-Charred Scar": "Pre-Cicatriz Carbonizada",
    "Tutorial": "Tutorial",
    "Tutorial: Combat Stats": "Tutorial: Estadísticas de combate",
    "The Kryl-Feijan Escape": "La Huida de Kryl-Feijan",
    "Kryl-Feijan": "Kryl-Feijan",
    "Save the lost merchant": "Salva al mercader perdido",
    # === Descripciones ===
    "An unusual book, a scroll and some potions.": "Un libro inusual, un pergamino y algunas pociones.",
    "A strange artifact found in the East.": "Un extraño artefacto encontrado en el Este.",
    # === start-* quests ===
    "The Allied Kingdoms": "Los Reinos Aliados",
    "The Dwarf Race": "La Raza Enana",
    "The Halfling Race": "La Raza Mediana",
    "The Shaloren Race": "La Raza Shalore",
    "The Thaloren Race": "La Raza Thalore",
    "The Yeek Race": "La Raza Yeek",
    "The Undead Race": "La Raza No-muerta",
    "The Archmage": "El Archimago",
    "The Sunwall Campaign": "La Campaña del Muro Solar",
    "The Point Zero Campaign": "La Campaña del Punto Cero",
    # === Misc ===
    "Quest Complete": "Misión completada",
    "Quest completed": "Misión completada",
    "Quest failed": "Misión fallida",
    "Quest updated": "Misión actualizada",
    "Quest Received": "Misión recibida",
    "You have received a new quest.": "Has recibido una nueva misión.",
    "You have completed this quest.": "Has completado esta misión.",
    "You have failed this quest.": "Has fallado esta misión.",
    "You have updated this quest.": "Has actualizado esta misión.",
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
    print("  FASE 5: misiones (data/quests/*)")
    print("=" * 60)

    files = sorted(QUESTS_DIR.glob("*.lua"))
    total = 0
    affected = 0

    for fpath in files:
        count = translate_file(fpath)
        if count > 0:
            print(f"  ✅ {fpath.name}: +{count}")
            total += count
            affected += 1

    print(f"\n  📊 Total: {total} traducciones en {affected} archivos")
    print()


if __name__ == "__main__":
    main()
