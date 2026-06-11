"""
Traductor ligero para ToME4-es.
Sin descargas, sin modelos, solo diccionario + reglas.
Funciona instantáneamente.
"""

import re

# =============================================================================
# TRADUCTOR BASADO EN DICCIONARIO + REGLAS
# =============================================================================

# Palabras que NO se traducen (nombres propios del juego)
NO_TRANSLATE = {
    "Maj'Eyal",
    "Eyal",
    "Sher'Tul",
    "ToME",
    "ToME4",
    "Amakthel",
    "Elandar",
    "Aeryn",
    "Urkis",
    "Voratun",
    "Stralite",
    "Mithril",
    "Trollmire",
    "Kor'Pul",
    "Daikara",
    "Dreadfell",
    "Angolwen",
    "Zigur",
    "Derth",
    "Elvala",
    "Shasshhiy'Kaish",
    "Kryl-Feijan",
}

# Traducciones exactas de términos completos
DICT = {
    # Elementos
    "Acid": "Ácido",
    "Fire": "Fuego",
    "Ice": "Hielo",
    "Cold": "Frío",
    "Lightning": "Relámpago",
    "Nature": "Naturaleza",
    "Blight": "Plaga",
    "Arcane": "Arcano",
    "Light": "Luz",
    "Darkness": "Oscuridad",
    "Temporal": "Temporal",
    "Mind": "Mental",
    "Physical": "Físico",
    "Poison": "Veneno",
    "Bleed": "Sangrado",
    "Stun": "Aturdimiento",
    # Verbos/Acciones
    "Strike": "Golpe",
    "Blow": "Golpe",
    "Strikes": "Golpea",
    "Beam": "Rayo",
    "Breath": "Aliento",
    "Spit": "Escupir",
    "Splash": "Salpicadura",
    "Spray": "Rociada",
    "Infusion": "Infusión",
    "Wave": "Ola",
    "Shield": "Escudo",
    "Armor": "Armadura",
    "Armour": "Armadura",
    "Aura": "Aura",
    "Skin": "Piel",
    "Blood": "Sangre",
    "Soil": "Suelo",
    "Bolt": "Proyectil",
    "Burst": "Explosión",
    "Nova": "Nova",
    "Storm": "Tormenta",
    "Surge": "Surge",
    "Mark": "Marca",
    "Trap": "Trampa",
    "Mastery": "Maestría",
    "Training": "Entrenamiento",
    # Modificadores
    "Absorb": "Absorber",
    "Absorption": "Absorción",
    "Advanced": "Avanzado",
    "Agile": "Ágil",
    "Anomaly": "Anomalía",
    "Avatar": "Avatar",
    "Blazing": "Abrazador",
    "Call": "Invocación",
    "Haste": "Celeridad",
    "Slow": "Ralentizar",
    "Teleport": "Teletransporte",
    "Swap": "Intercambio",
    "Summon": "Invocar",
    "Summoning": "Invocación",
    "Quickening": "Aceleración",
    "Destruction": "Destrucción",
    "Rend": "Desgarrar",
    "Fusion": "Fusión",
    "Overpower": "Aplastar",
    "Block": "Bloquear",
    "Assault": "Asalto",
    "Protection": "Protección",
    "Permeation": "Permeación",
    "Veteran": "Veterano",
    "Savage": "Salvaje",
    "Torment": "Tormento",
    # Nombres comunes de talentos
    "Meditation": "Meditación",
    "Contemplation": "Contemplación",
    "Track": "Rastrear",
    "Aim": "Apuntar",
    "Volley": "Lluvia",
    "Barrage": "Barrera",
    "Snipe": "Francotiro",
    "Shoot": "Disparar",
    "Backstab": "Apuñalar",
    "Flurry": "Ráfaga",
    "Whirlwind": "Torbellino",
    "Sweep": "Barrido",
    "Rush": "Embestida",
    "Charge": "Carga",
    "Rampage": "Rabia",
    "Bloodbath": "Baño de sangre",
    "Regeneration": "Regeneración",
    "Healing": "Curación",
    # Razas
    "Human": "Humano",
    "Elf": "Elfo",
    "Dwarf": "Enano",
    "Halfling": "Mediano",
    "Ogre": "Ogro",
    "Troll": "Trol",
    "Orc": "Orco",
    "Skeleton": "Esqueleto",
    "Ghoul": "Ghul",
    "Undead": "No-muerto",
    # Clases
    "Warrior": "Guerrero",
    "Mage": "Mago",
    "Rogue": "Pícaro",
    "Archer": "Arquero",
    "Berserker": "Berserker",
    # Atributos
    "Strength": "Fuerza",
    "Dexterity": "Destreza",
    "Constitution": "Constitución",
    "Magic": "Magia",
    "Willpower": "Voluntad",
    "Cunning": "Astucia",
}

# Patrones para traducir combinaciones
PATTERNS = [
    (r"^Anomaly (.+)", r"Anomalía de \1"),
    (r"^Acid (.+)", r"Ácido \1"),
    (r"^Fire (.+)", r"Fuego \1"),
    (r"^Cold (.+)", r"Frío \1"),
    (r"^Lightning (.+)", r"Relámpago \1"),
    (r"^Arcane (.+)", r"Arcano \1"),
    (r"^Temporal (.+)", r"Temporal \1"),
    (r"^Summon (.+)", r"Invocar \1"),
    (r"^Absorb (.+)", r"Absorber \1"),
    (r"^Acidic (.+)", r"Ácido \1"),
    (r"^Venom (.+)", r"Venenoso \1"),
]


class LightTranslator:
    """Traductor basado en diccionario + reglas, sin descargas."""

    def translate(self, text):
        if not text or text.strip() == "":
            return text

        # 1. NO_TRANSLATE
        if text in NO_TRANSLATE:
            return text

        # 2. DICT exacto
        if text in DICT:
            return DICT[text]

        # 3. Patrones
        for pattern, replacement in PATTERNS:
            m = re.match(pattern, text)
            if m:
                # Traducir la segunda parte recursivamente
                rest = self.translate(m.group(1))
                return (
                    re.sub(pattern, f"Anomalía de {rest}", text)
                    if "Anomaly" in pattern
                    else re.sub(pattern, replacement, text)
                )

        # 4. Separar palabras y traducir cada una
        words = text.split()
        translated = []
        for word in words:
            # Mantener puntuacion
            clean = word.strip(",.!?;:()[]{}'\"")
            punct_start = word[: len(word) - len(word.lstrip(",.!?;:()[]{}'\""))]
            punct_end = word[len(word.rstrip(",.!?;:()[]{}'\"")) :]

            if clean in DICT:
                trans = DICT[clean]
            else:
                # Mantener mayusculas
                trans = clean

            # Preservar mayuscula inicial
            if clean and clean[0].isupper() and trans:
                trans = (
                    trans[0].upper() + trans[1:] if len(trans) > 1 else trans.upper()
                )

            translated.append(punct_start + trans + punct_end)

        return " ".join(translated)


def test():
    t = LightTranslator()
    tests = [
        "Flame",
        "Fireflash",
        "Acid Breath",
        "Arcane Combat",
        "Anomaly Slow",
        "Summon War Hound",
        "Absorb Life",
        "Talent cooldown reduced",
        "%d turns",
    ]
    for test in tests:
        result = t.translate(test)
        print(f"  {test:40} -> {result}")


if __name__ == "__main__":
    test()
