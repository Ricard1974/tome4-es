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
    "Acid": "Acido", "Fire": "Fuego", "Ice": "Hielo", "Cold": "Frio",
    "Lightning": "Relampago", "Nature": "Naturaleza", "Blight": "Plaga",
    "Arcane": "Arcano", "Light": "Luz", "Darkness": "Oscuridad",
    "Temporal": "Temporal", "Mind": "Mental", "Physical": "Fisico",
    "Poison": "Veneno", "Bleed": "Sangrado", "Stun": "Aturdimiento",
    # Verbos/Acciones
    "Strike": "Golpe", "Blow": "Golpe", "Strikes": "Golpea",
    "Beam": "Rayo", "Breath": "Aliento", "Spit": "Escupir",
    "Splash": "Salpicadura", "Spray": "Rociada", "Infusion": "Infusion",
    "Wave": "Ola", "Shield": "Escudo", "Armor": "Armadura", "Armour": "Armadura",
    "Aura": "Aura", "Skin": "Piel", "Blood": "Sangre", "Soil": "Suelo",
    "Bolt": "Proyectil", "Burst": "Explosion", "Nova": "Nova",
    "Storm": "Tormenta", "Surge": "Surge", "Mark": "Marca", "Trap": "Trampa",
    "Mastery": "Maestria", "Training": "Entrenamiento",
    # Modificadores
    "Absorb": "Absorber", "Absorption": "Absorcion",
    "Advanced": "Avanzado", "Agile": "Agil", "Anomaly": "Anomalia",
    "Avatar": "Avatar", "Blazing": "Abrazador", "Call": "Invocacion",
    "Haste": "Celeridad", "Slow": "Ralentizar", "Teleport": "Teletransporte",
    "Swap": "Intercambio", "Summon": "Invocar", "Summoning": "Invocacion",
    "Quickening": "Aceleracion", "Destruction": "Destruccion",
    "Rend": "Desgarrar", "Fusion": "Fusion", "Overpower": "Aplastar",
    "Block": "Bloquear", "Assault": "Asalto", "Protection": "Proteccion",
    "Permeation": "Permeacion", "Veteran": "Veterano",
    "Savage": "Salvaje", "Torment": "Tormento",
    # Nombres comunes de talentos
    "Meditation": "Meditacion", "Contemplation": "Contemplacion",
    "Track": "Rastrear", "Aim": "Apuntar",
    "Volley": "Lluvia", "Barrage": "Barrera", "Snipe": "Francotiro",
    "Shoot": "Disparar", "Backstab": "Apunalar", "Flurry": "Rafaga",
    "Whirlwind": "Torbellino", "Sweep": "Barrido", "Rush": "Embestida",
    "Charge": "Carga", "Rampage": "Rabia", "Bloodbath": "Bano de sangre",
    "Regeneration": "Regeneracion", "Healing": "Curacion",
    "Adept": "Experto", "Arrow": "Flecha",
    "Blade": "Hoja", "Blast": "Explosion", "Blinding": "Cegador",
    "Blink": "Parpadeo", "Body": "Cuerpo", "Chant": "Cantico",
    "Command": "Mando", "Corrosive": "Corrosivo", "Curse": "Maldicion",
    "Dark": "Oscuro", "Death": "Muerte", "Dirge": "Elegia",
    "Dream": "Sueno", "Echoes": "Ecos", "Eldritch": "Arcano",
    "Elemental": "Elemental", "Energy": "Energia", "Fade": "Desvanecer",
    "Fate": "Destino", "Feed": "Alimentar", "Field": "Campo",
    "Focus": "Enfoque", "Fold": "Plegar", "Form": "Forma",
    "Fury": "Furia", "Gesture": "Gesto", "Glyph": "Glifo",
    "Golem": "Golem", "Grab": "Agarre", "Gravity": "Gravedad",
    "Hands": "Manos", "Hex": "Maleficio", "History": "Historia",
    "Hymn": "Himno", "Kick": "Patada", "Leech": "Drenar",
    "Life": "Vida", "Moss": "Musgo", "Night": "Noche",
    "Phase": "Fase", "Pool": "Piscina", "Power": "Poder",
    "Senses": "Sentidos", "Shadow": "Sombra", "Shadows": "Sombras",
    "Shift": "Desplazar", "Shot": "Disparo", "Sight": "Vision",
    "Soul": "Alma", "Spike": "Pua", "Spikes": "Puas",
    "Static": "Estatico", "Stone": "Piedra", "Sun": "Sol",
    "Threads": "Hilos", "Throw": "Lanzar", "Time": "Tiempo",
    "Touch": "Tocar", "Trance": "Trance", "Transcendent": "Trascendente",
    "Unity": "Unidad", "Walk": "Caminar", "Warp": "Distorsion",
    "Will": "Voluntad", "Wrath": "Ira", "Dimensional": "Dimensional",
    "Weakness": "Debilidad", "Repulsion": "Repulsion",
    "Rune:": "Runa:",
    # Razas
    "Human": "Humano", "Elf": "Elfo", "Dwarf": "Enano",
    "Halfling": "Mediano", "Ogre": "Ogro", "Troll": "Trol",
    "Orc": "Orco", "Skeleton": "Esqueleto", "Ghoul": "Ghul", "Undead": "No-muerto",
    # Clases
    "Warrior": "Guerrero", "Mage": "Mago", "Rogue": "Picaro",
    "Archer": "Arquero", "Berserker": "Berserker",
    # Atributos
    "Strength": "Fuerza", "Dexterity": "Destreza",
    "Constitution": "Constitucion", "Magic": "Magia",
    "Willpower": "Voluntad", "Cunning": "Astucia",
}# Patrones para traducir combinaciones
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
