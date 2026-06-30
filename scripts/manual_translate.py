#!/usr/bin/env python3
"""
Traducciones manuales v2 - usa regex limpio para extraer argumentos.
"""

import re
from pathlib import Path

BASE = Path("/home/ricard/proyectos/tome4-es/translations/es/mod-tome-split")

# Regex para extraer: t("ORIG", "TRANS", "tipo")
T_PATTERN = re.compile(r'^t\("((?:[^"]|\\")*)"\s*,\s*"((?:[^"]|\\")*)"')


###############################################################################
# 1. STAT TEMPLATES
###############################################################################
def translate_stat_templates():
    count = 0
    for f in sorted((BASE / "data" / "birth").rglob("*.lua")):
        content = f.read_text("utf-8")
        lines = content.split("\n")
        new_lines = list(lines)
        changed = False

        for i, line in enumerate(lines):
            stripped = line.strip()
            m = T_PATTERN.match(stripped)
            if not m:
                continue
            orig, trans = m.group(1), m.group(2)

            if orig != trans:
                continue
            if "#LIGHT_BLUE# *" not in orig:
                continue

            new_trans = orig
            new_trans = new_trans.replace("Magic", "Magia")
            new_trans = new_trans.replace("Willpower", "Voluntad")
            new_trans = new_trans.replace("Cunning", "Astucia")

            if new_trans != orig:
                indent = line[: len(line) - len(line.lstrip())]
                new_lines[i] = f'{indent}t("{orig}", "{new_trans}", "_t")'
                changed = True
                count += 1
                print(f"  ✓ {f.name}: {orig[:60]}")

        if changed:
            f.write_text("\n".join(new_lines), "utf-8")

    print(f"\nStat templates: {count}")
    return count


###############################################################################
# 2. TODAS LAS DEMÁS TRADUCCIONES MANUALES
###############################################################################

TRANSLATIONS = {
    # === TIMED EFFECTS: Magical ===
    "Stoned": "Petrificado",
    "Arcane Storm": "Tormenta Arcana",
    "Earthen Barrier": "Barrera de Tierra",
    "Vimsense": "Sensor de Vim",
    "-Invis": "-Invisibilidad",
    "Ethereal": "Etéreo",
    "Stormshield": "Escudo de Tormenta",
    "+Stormshield": "+Escudo de Tormenta",
    "-Stormshield": "-Escudo de Tormenta",
    "PURGING": "PURGANDO",
    "-Purging": "-Purgando",
    "Sensing (Vim)": "Detección (Vim)",
    "Supercharge Golem": "Sobrecargar Gólem",
    "Life Tap": "Drenar Vida",
    "+Martyr": "+Mártir",
    "-Martyr": "-Mártir",
    "Radiance Lost": "Resplandor Perdido",
    "Curse of Defenselessness": "Maldición de Indefensión",
    "Corrupting Strike": "Golpe Corruptor",
    "Acid Splash": "Salpicadura Ácida",
    "Bloodfury": "Furia Sangrienta",
    "-Phoenix": "-Fénix",
    "Timeport: Point Zero": "Teletransporte: Punto Cero",
    "Wraithform": "Forma Espectral",
    "Invigorate": "Vigorizar",
    "Bone Shield": "Escudo de Hueso",
    "Haste": "Celeridad",
    "Congeal Time": "Solidificar Tiempo",
    "Aether Breach": "Brecha de Éter",
    "Aether Avatar": "Avatar de Éter",
    "#Target#'s solar fury subsides.": "La furia solar de #Target# se calma.",
    "Probability Travel": "Viaje Probabilístico",
    "Metaflow": "Metacorriente",
    "Empowered Healing": "Curación Potenciada",
    "Fatiguing Starlight": "Luz Estelar Agotadora",
    "Shifting Shadows": "Sombras Cambiantes",
    "Blazing Light": "Luz Abrasadora",
    "Surge of Undeath": "Surge de No-Muerte",
    "-Bone Shield": "-Escudo de Hueso",
    "Impending Doom": "Perdición Inminente",
    "Rigor Mortis": "Rigor Mortis",
    "-Rigor Mortis": "-Rigor Mortis",
    "Death Rush": "Aceleración Mortal",
    "Abyssal Shroud": "Sudario Abisal",
    "Spin Fate": "Girar el Destino",
    "-Spin Fate": "-Girar el Destino",
    "Woeful Darkness": "Oscuridad Afligida",
    "Woeful Cripple": "Lisiadura Afligida",
    "Worm Rot": "Podredumbre de Gusano",
    "Ghoul Rot": "Podredumbre de Ghul",
    "Arcane Vortex": "Vórtice Arcano",
    "-Arcane Vortex": "-Vórtice Arcano",
    "-Aether Breach": "-Brecha de Éter",
    "Caustic Golem": "Gólem Cáustico",
    "-Light Burst": "-Estallido de Luz",
    "Light Burst Speed": "Velocidad de Estallido de Luz",
    "+Light Burst Speed": "+Velocidad de Estallido de Luz",
    "-Light Burst Speed": "-Velocidad de Estallido de Luz",
    "-Probability Travel": "-Viaje Probabilístico",
    "Ogric Wrath": "Ira Ógrica",
    "-Ogric Wrath": "-Ira Ógrica",
    "Ogre Fury": "Furia Ogro",
    "Writ Large": "Amplificado",
    "Arrow Echoes": "Ecos de Flecha",
    "Fold Fate": "Plegar Destino",
    "Blight Poison": "Veneno de Plaga",
    "Insidious Blight": "Plaga Insidiosa",
    "Eldritch Stone Shield": "Escudo de Piedra Arcano",
    "Deeprock Form": "Forma de Roca Profunda",
    "Pacification Hex": "Maleficio de Pacificación",
    "Domination Hex": "Maleficio de Dominación",
    "-Domination hex": "-Maleficio de Dominación",
    "Shadowguard Immunity": "Inmunidad de Guardia Sombría",
    "Shadow Cut": "Corte Sombrío",
    "Draining Moonlight": "Luz Lunar Drenante",
    "-Draining Moonlight": "-Luz Lunar Drenante",
    "Auger of Destruction": "Barrena de Destrucción",
    "Immune to Frightening Presence": "Inmune a Presencia Aterradora",
    "Consume Soul": "Consumir Alma",
    "Necrotic Aura": "Aura Necrótica",
    "Lord of Skulls": "Señor de las Calaveras",
    "Lord of Skulls (warrior)": "Señor de las Calaveras (guerrero)",
    "Lord of Skulls (archer)": "Señor de las Calaveras (arquero)",
    "Lord of Skulls (mage)": "Señor de las Calaveras (mago)",
    "Spike of Decrepitude": "Púa de Decrepitud",
    "Soul Leech": "Drenar Alma",
    "Chill of the Tomb": "Frío de la Tumba",
    "Dire Plague": "Plaga Aterradora",
    "Rime Wraith": "Espectro de Escarcha",
    "Rime Wraith (Gelid Host)": "Espectro de Escarcha (Anfitrión Gélido)",
    "Ghost Walk": "Paso Fantasmal",
    "-Ghost Walk": "-Paso Fantasmal",
    "Orb Of Thaumaturgy": "Orbe de Taumaturgia",
    "Dirge of Famine": "Canto de Hambruna",
    "Dirge of Conquest": "Canto de Conquista",
    "Blinding Light": "Luz Cegadora",
    "Devourer Stance": "Postura Devoradora",
    "Reality Smearing": "Difuminar Realidad",
    "Time Shield": "Escudo Temporal",
    "Lich Hunger": "Hambre de Lich",
    # === TIMED EFFECTS: Mental ===
    "Battle Cry": "Grito de Guerra",
    "#Target#'s frantic summoning ends.": "La invocación frenética de #Target# termina.",
    "Spell Feedback": "Retroalimentación de Hechizo",
    "Battle Shout": "Grito de Batalla",
    "Willful Combat": "Combate Voluntarioso",
    "Gloom Weakness": "Debilidad de Oscuridad",
    "Hateful Whisper": "Susurro Odioso",
    "Frenzied Focus": "Enfoque Frenético",
    "Void Echoes": "Ecos del Vacío",
    "Waking Nightmare": "Pesadilla Vigilante",
    "Deadly Strikes": "Golpes Mortales",
    "Orcish Fury": "Furia Orca",
    "Orcish Triumph": "Triunfo Orco",
    "Frantic Summoning": "Invocación Frenética",
    "Lobotomized (confused)": "Lobotomizado (confuso)",
    "Psionic Shield": "Escudo Psiónico",
    "Feedback Loop": "Bucle de Retroalimentación",
    "-Feedback Loop": "-Bucle de Retroalimentación",
    "Forge Shield": "Escudo de Forja",
    "Mind Parasite": "Parásito Mental",
    "-Mind Parasite": "-Parásito Mental",
    "Shadow Decoy": "Señuelo Sombrío",
    "Transcendent Telekinesis": "Telequinesis Trascendente",
    "Transcendent Electrokinesis": "Electroquinesis Trascendente",
    "Psionic Maelstrom": "Maelstrom Psiónico",
    "Caught Lightning": "Relámpago Atrapado",
    "-Vampire Mark": "-Marca Vampírica",
    # === TIMED EFFECTS: Physical ===
    "-Regen": "-Regeneración",
    "-Crippling Poison": "-Veneno Debilitante",
    "-Constricted": "-Constreñido",
    "Stoneskin": "Piel de Piedra",
    "Thorny Skin": "Piel Espinosa",
    "Frozen Feet": "Pies Congelados",
    "-Frozen": "-Congelado",
    "Iceblock": "Bloque de Hielo",
    "Wrath of the Woods": "Ira de los Bosques",
    "Wrath of the Highborn": "Ira de los Nobles",
    "Shell Shield": "Escudo de Caparazón",
    "Serpentine Nature": "Naturaleza Serpentina",
    "Primal Attunement": "Sintonía Primal",
    "-Primal": "-Primal",
    "Purge Blight": "Purga de Plaga",
    "-Purge": "-Purga",
    "Sensing": "Detección",
    "Sunder Armour": "Romper Armadura",
    "-Sunder Armor": "-Romper Armadura",
    "Sunder Arms": "Romper Brazos",
    "-Sunder Arms": "-Romper Brazos",
    "Cripple": "Lisiar",
    "Feint": "Finta",
    "Snipe": "Francotiro",
    "Shadowstrike": "Golpe Sombrío",
    "Pinned to the ground": "Clavado al suelo",
    "-Bone Grab": "-Agarre de Hueso",
    "Crushing Hold": "Presa Aplastante",
    "-Crushing Hold": "-Presa Aplastante",
    "Strangle Hold": "Presa Estranguladora",
    "Healing Nexus Redirection": "Redirección de Nexo Curativo",
    "Imploding (slow)": "Implosionando (lento)",
    "Adrenaline Surge": "Surge de Adrenalina",
    "Blindside Bonus": "Bonus de Punto Ciego",
    "Thorn Grab": "Agarre Espinoso",
    "Berserker Rage": "Furia de Berserker",
    "Soothing Darkness": "Oscuridad Calmante",
    "Shadow Dance": "Danza de Sombras",
    "Rogue's Brew": "Poción del Pícaro",
    "Stone Vine": "Enredadera de Piedra",
    "-Stone Vine": "-Enredadera de Piedra",
    "Mobile Defense": "Defensa Móvil",
    "Ghoulish Leap": "Salto Ghulesco",
    "Mana Clash": "Choque de Maná",
    "Swift Shot": "Disparo Rápido",
    "+Silent stealth": "+Sigilo Silencioso",
    # === TIMED EFFECTS: Other ===
    "Spacetime Tuning": "Sintonización Espaciotemporal",
    "Cauterize": "Cauterizar",
    "Spellblaze Aura": "Aura de Hechizo Llameante",
    "Fumble": "Torpeza",
    "Flare": "Bengala",
    "Elemental Surge: Cold": "Surge Elemental: Frío",
    "Circle Surge": "Surge de Círculo",
    "Time Prison": "Prisión Temporal",
    "Imminent Paradox Clone": "Clon de Paradoja Inminente",
    "Paradox Clone": "Clon de Paradoja",
    "Sever Lifeline": "Cortar Línea Vital",
    "Shadow Veil": "Velo de Sombras",
    "Zero Gravity": "Gravedad Cero",
    "Curse of Corpses": "Maldición de Cadáveres",
    "Curse of Shrouds": "Maldición de Sudarios",
    "Shroud of Passing": "Sudario de Paso",
    "Shroud of Death": "Sudario de Muerte",
    "Curse of Nightmares": "Maldición de Pesadillas",
    "Curse of Misfortune": "Maldición de Infortunio",
    "Unstable Probabilites": "Probabilidades Inestables",
    "Dream Self": "Yo Onírico",
    "Noxious fumes": "Humos Nocivos",
    "Slimy floor": "Suelo Viscoso",
    "Cloak of Deception": "Capa de Engaño",
    "Draconic Will": "Voluntad Dráconica",
    "-Draconic Will": "-Voluntad Dráconica",
    "Aeons Stasis": "Estatismo Eónico",
    "-Aeons Stasis": "-Estatismo Eónico",
    "Hit Penalty": "Penalización de Golpe",
    "Twist Fate": "Torcer el Destino",
    "-Twist Fate": "-Torcer el Destino",
    "Natural Aura": "Aura Natural",
    "Sorcerous Aura": "Aura Hechicera",
    "Sinister Aura": "Aura Siniestra",
    "Heady Scent": "Olor Embriagador",
    "Abashed Expanse": "Extensión Abochornada",
    "Touch of Death": "Toque de Muerte",
    "-Touch of Death": "-Toque de Muerte",
    "Pinned Down": "Inmovilizado",
    "Frozen Ground": "Suelo Congelado",
    "-Frozen Ground": "-Suelo Congelado",
    "Aether Permeation": "Permeación de Éter",
    "Pestilence Saturation": "Saturación de Pestilencia",
    "Temporal Clone": "Clon Temporal",
    "Fugue Clone": "Clon de Fuga",
    "Bane of Blindness": "Azote de Ceguera",
    "Bane of Confusion": "Azote de Confusión",
    "-Bane": "-Azote",
    # === COMBAT MESSAGES ===
    "#LIGHT_GREEN#[slip peacefully into death.]": "#LIGHT_GREEN#[deslízate pacíficamente hacia la muerte.]",
    "#STEEL_BLUE#A time vortex briefly appears in front of you.": "#STEEL_BLUE#Un vórtice temporal aparece brevemente frente a ti.",
    "#DARK_GREY#A shroud of shadow dances around %s!": "#DARK_GREY#Un sudario de sombras baila alrededor de %s!",
    "#Source# strikes at a vital spot on #target#!": "¡#Source# golpea un punto vital de #target#!",
    "#Source# hits #Target# for %s damage.": "#Source# golpea a #Target# por %s de daño.",
    "#Source# receives %s.": "#Source# recibe %s.",
    "#Source# shares damage with %s oozes!": "¡#Source# comparte daño con %s limos!",
    "#Source# aims %s %s at #target#!": "¡#Source# apunta con %s %s a #target#!",
    "#Source# strikes out at #target# with %s %s!": "¡#Source# golpea a #target# con %s %s!",
    "The target has been set on fire": "El objetivo ha sido incendiado",
    "You are covered in blazing sunlight": "Estás cubierto de luz solar ardiente",
    "You are on fire!": "¡Estás en llamas!",
    # === ZONE NAMES ===
    "Ruined Dungeon": "Mazmorra en Ruinas",
    "Tranquil Meadow": "Prado Tranquilo",
    "Shadow Crypt": "Cripta Sombría",
    "Cursed Village": "Aldea Maldita",
    "Elven Ruins": "Ruinas Élficas",
    "The Deep Bellow": "El Rugido Profundo",
    "Eidolon Plane": "Plano Eidolon",
    "Gorbat Pride": "Orgullo Gorbat",
    "Grushnak Pride": "Orgullo Grushnak",
    "Illusory Castle": "Castillo Ilusorio",
    "Murgol Lair": "Guarida de Murgol",
    "Norgos Lair": "Guarida de Norgos",
    "Dogroth Caldera": "Caldera Dogroth",
    "Old Forest": "Bosque Antiguo",
    "Orc Breeding Pit": "Foso de Cría Orca",
    "Paradox Plane": "Plano de la Paradoja",
    "Lost Dwarven Kingdom of Reknor": "Reino Enano Perdido de Reknor",
    "Rhaloren Camp": "Campamento Rhaloren",
    "Ritches Tunnels": "Túneles Ritch",
    "Sandworm lair": "Guarida de Gusano de Arena",
    "Unknown Sher'Tul Fortress": "Fortaleza Desconocida Sher'Tul",
    "Slazish Fens": "Pantanos Slazish",
    "Southern Beach": "Playa del Sur",
    "Temporal Rift: Lumberjack village": "Brecha Temporal: Aldea Leñadora",
    "Temporal Rift: Daikara": "Brecha Temporal: Daikara",
    "Iron Council": "Consejo de Hierro",
    "Vor Armoury": "Armería Vor",
    "Vor Pride": "Orgullo Vor",
    "World of Eyal": "Mundo de Eyal",
    "Derth (Southeast)": "Derth (Sureste)",
    # === NPC/ENTITY NAMES ===
    "Director Hompalan": "Director Hompalan",
    "Sun Paladin Rashim": "Paladín Solar Rashim",
    "High Sun Paladin Aeryn": "Alta Paladín Solar Aeryn",
    "High Chronomancer Zemekkys": "Alto Cronomante Zemekkys",
    "Grand Corruptor": "Gran Corruptor",
    "Meranas, Herald of Angolwen": "Meranas, Heraldo de Angolwen",
    "Limmir (Quest)": "Limmir (Misión)",
    "Grand Necromancer #rng#": "Gran Nigromante #rng#",
    "Inquisitor #rng#": "Inquisidor #rng#",
    "Combat Trainer #rng#": "Entrenador de Combate #rng#",
    "Elite Combat Trainer #rng#": "Entrenador de Combate de Élite #rng#",
    "Bandit Leader #rng#": "Líder Bandido #rng#",
    "Weaver Queen": "Reina Tejedora",
    "#rng# the Witherer": "#rng# el Marchitador",
    "#rng# the Herald": "#rng# el Heraldo",
    "#rng# the Storm Terror": "#rng# el Terror de Tormentas",
    "#rng# the Caustic Terror": "#rng# el Terror Cáustico",
    "#rng# the Thug": "#rng# el Matón",
    "#rng# the Neverdead": "#rng# el No-Muerto",
    "Ra'kk kor merk ZUR!!!": "¡¡¡Ra'kk kor merk ZUR!!!",
    # === OBJECT/ITEM NAMES ===
    "Crown of Burning Pain": "Corona de Dolor Ardiente",
    "Coral Portal": "Portal de Coral",
    "Demonic Orb of Many Ways": "Orbe Demoníaco de Muchos Caminos",
    "Rod of Recall": "Vara de Retorno",
    "Glittering amulet.": "Amuleto brillante.",
    "Stone Guardian": "Guardia de Piedra",
    "Malevolent Portal": "Portal Malévolo",
    "Mocking Note": "Nota de Burla",
    "Recall Portal": "Portal de Retorno",
    "Spellblaze Fallouts": "Secuelas del Hechizo Llameante",
    "writhing mindstar": "mente-estrella retorcido",
    # === QUEST/MISSION NAMES ===
    "A Second Vault": "Una Segunda Bóveda",
    "Lost Knowledge": "Conocimiento Perdido",
    # === ABILITY/SPELL NAMES ===
    "Lashing Tentacle": "Tentáculo Latigante",
    "Spacetime Tear": "Desgarro Espaciotemporal",
    "Polarity Bolt": "Rayo de Polaridad",
    "Cursed Sentry": "Centinela Maldito",
    "Hammer Toss": "Lanzamiento de Martillo",
    "Necrotic Minion": "Esbirro Necrótico",
    "Quickdraw Knife": "Cuchillo de Sacado Rápido",
    "Risen Ghoul": "Ghul Resucitado",
    "Ghoulish Minion": "Esbirro Ghulesco",
    "Purging Trap": "Trampa Purificadora",
    "dragonsfire trap": "trampa de fuego de dragón",
    "Tutorial Lobby Portal": "Portal del Vestíbulo Tutorial",
    # === LORE NAMES ===
    "Tales of the Spellblaze": "Cuentos del Hechizo Llameante",
    "The Spellblaze Chronicles(1): A Fateful Meeting": "Crónicas del Hechizo Llameante(1): Un Encuentro Fatídico",
    "The Spellblaze Chronicles(3): The Farportal": "Crónicas del Hechizo Llameante(3): El Lejano Portal",
    "The Spellblaze Chronicles(6): A Changed Eyal": "Crónicas del Hechizo Llameante(6): Un Eyal Cambiado",
    "The Spellblaze Chronicles(8): Forbidden": "Crónicas del Hechizo Llameante(8): Prohibido",
    "Iron Throne Profits History: Age of Allure": "Historia de Beneficios del Trono de Hierro: Era del Encanto",
    "Iron Throne Profits History: Age of Dusk": "Historia de Beneficios del Trono de Hierro: Era del Ocaso",
    "Iron Throne Profits History: Age of Pyre": "Historia de Beneficios del Trono de Hierro: Era de la Pira",
    "Iron Throne Profits History: Age of Ascendancy": "Historia de Beneficios del Trono de Hierro: Era de Ascendencia",
    "Iron Throne trade ledger": "Libro de contabilidad del Trono de Hierro",
    "Tale of the Moonsisters": "Cuento de las Hermanas Lunares",
    "Lament for Lands now Lost": "Lamento por Tierras Ahora Perdidas",
    "Rashim Journal (1)": "Diario de Rashim (1)",
    "Rashim Journal (2)": "Diario de Rashim (2)",
    "Rashim Journal (3)": "Diario de Rashim (3)",
    "conch (2)": "caracola (2)",
    "conch (3)": "caracola (3)",
    # === DIALOG/UI ===
    "Select Prepared Traps": "Seleccionar Trampas Preparadas",
    "Donator Cosmetic Feature": "Función Cosmética de Donante",
    "Donate": "Donar",
    "Shimmer Demo": "Demostración de Brillo",
    "Shimmer Sets: %s": "Conjuntos de Brillo: %s",
    "Shimmer: Remove Sustains Effects": "Brillo: Eliminar Efectos Sostenidos",
    "Empower": "Potenciar",
    "Quicken": "Acelerar",
    "Arcane Combat": "Combate Arcano",
    "Wield/Wear": "Equipar/Usar",
    "Tag": "Marcar",
    "Untag": "Desmarcar",
    "Tag:": "Marca:",
    "Off Set": "Fuera de Lugar",
    "Rename": "Renombrar",
    "Managed readied tools": "Gestionar herramientas preparadas",
    "Default": "Por Defecto",
    "Tank": "Tanque",
    "Standby": "Espera",
    "[G]eneral": "[G]eneral",
    "Quest Log": "Registro de Misiones",
    "Inspect Creature": "Inspeccionar Criatura",
    "Lua inspect [Trap]": "Inspeccionar Lua [Trampa]",
    "Store": "Tienda",
    "Prodigies: %s": "Prodigios: %s",
    "Lore found: #0080FF#%s": "Saber encontrado: #0080FF#%s",
    "Lore": "Saber",
    "Killed": "Asesinado",
    "Toggle Demi-Godmode": "Alternar Semi-Dios",
    "Toggle Godmode": "Alternar Modo Dios",
    "Alter Faction": "Alterar Facción",
    "DEBUG -- Alter Faction": "DEBUG -- Alterar Facción",
    "Grant/Alter Quests": "Conceder/Alterar Misiones",
    "Advance Player": "Avanzar Jugador",
    "Spawn Event": "Generar Evento",
    "Reload/regenerate Zone and level": "Recargar/regenerar Zona y nivel",
    "#GREY#None#LAST#": "#GREY#Ninguno#LAST#",
    "#GREY#[Invisible]": "#GREY#[Invisible]",
    "#GREY#[Default]": "#GREY#[Por Defecto]",
    "#GREY#No Tooltip to Display#LAST#": "#GREY#Sin Información que Mostrar#LAST#",
    "#ORANGE#Randart#LAST#": "#ORANGE#Artefacto Aleatorio#LAST#",
    "#LIGHT_BLUE#Base Object#LAST#": "#LIGHT_BLUE#Objeto Base#LAST#",
    "#YELLOW#Random Actor#LAST#": "#YELLOW#Actor Aleatorio#LAST#",
    "#PINK#Test Dummy#LAST#": "#PINK#Maniquí de Prueba#LAST#",
    "#VIOLET#Option unlocked: %s": "#VIOLET#Opción desbloqueada: %s",
    "Attach Tinker": "Colocar Ingenio",
    "NPC Inventory": "Inventario de PNJ",
    "Ego": "Ego",
    "Debug -- Grant/Alter Quest": "Debug -- Conceder/Alterar Misión",
    "Failed to generate %s": "Fallo al generar %s",
    "euro": "euro",
    "%0.2f %s": "%0.2f %s",
    "#LIGHT_BLUE#Mental:": "#LIGHT_BLUE#Mental:",
    "Stat": "Estadística",
    "Spellcrit": "Crítico de Hechizo",
    "%-8.8s:": "%-8.8s:",
    "Wave %d": "Ola %d",
    "Wave %d %s": "Ola %d %s",
    "Wave(TOP) %d %s": "Ola(SUPERIOR) %d %s",
    "Lvl %d": "Nv %d",
    "[Final]": "[Final]",
    "%+.0f max": "%+.0f máx",
    "Foes left: #LIGHT_RED#%s": "Enemigos restantes: #LIGHT_RED#%s",
    "#LIGHT_GREEN#enabled": "#LIGHT_GREEN#activado",
    "#GOLD#Automatic accept target mode: %s": "#GOLD#Modo de aceptación automática: %s",
    "Maj'Eyal": "Maj'Eyal",
    "%s (Roguelike)": "%s (Roguelike)",
    "%s (Nightmare (Adventure) difficulty)": "%s (dificultad Pesadilla (Aventura))",
    "%s (Insane (Adventure) difficulty)": "%s (dificultad Insano (Aventura))",
    "Cloak": "Capa",
    "Quiver": "Aljaba",
    "Socketed Gems": "Gemas Engastadas",
    "Gems": "Gemas",
    "Tinkers": "Ingenios",
    "Luck": "Suerte",
    "New Class: #LIGHT_GREEN#Paradox Mage (Chronomancer)": "Nueva Clase: #LIGHT_GREEN#Mago de la Paradoja (Cronomante)",
    "New Class: #LIGHT_GREEN#Temporal Warden (Chronomancer)": "Nueva Clase: #LIGHT_GREEN#Guardián Temporal (Cronomante)",
    "#LIGHT_GREEN#*dance*": "#LIGHT_GREEN#*baila*",
    "Temporal": "Temporal",
    "Melinda": "Melinda",
    "GIRL": "CHICA",
    "GUY": "CHICO",
    "Briagh?": "¿Briagh?",
    "Tutorial": "Tutorial",
    "Normal": "Normal",
    "Roguelike": "Roguelike",
    "Neutral": "Neutral",
    "Merchant Caravan": "Caravana Mercante",
    "Shalore": "Shalore",
    "Thalore": "Thalore",
    "Yeek": "Yeek",
    "Lich": "Lich",
    "Tatoos": "Tatuajes",
    "UI": "UI",
    "Online": "Online",
    "Metal": "Metal",
    "Simple": "Simple",
    "ASCII": "ASCII",
    "Altefcat/Gervais": "Altefcat/Gervais",
    "64x64": "64x64",
    "48x48": "48x48",
    "32x32": "32x32",
    "Unarmed:": "Sin armas:",
    "mental": "mental",
    "Atamathoned!": "¡Atamathoneado!",
    "Deus Ex Machina": "Deus Ex Machina",
    "Orcrist": "Orcrist",
    "Wibbly Wobbly Timey Wimey Stuff": "Cosas Raras del Tiempo",
    "Golem arcane capacity.": "Capacidad arcana del Gólem.",
    "Slimy, wriggling, and crackling with electricity.": "Viscoso, retorciéndose y crepitando con electricidad.",
    "Transmogrify all %s item(s) on the floor?": "¿Transmutar todos los objetos %s del suelo?",
    "Transmogrify all %s item(s) in your chest?": "¿Transmutar todos los objetos %s del cofre?",
    "%s revels in the spilt blood and grows stronger!": "¡%s se regocija en la sangre derramada y se vuelve más fuerte!",
    "During the invasion of Eldoral the Halfling Rogue Herah is said to have slain over one hundred orcs while defending a great vault of magical knowledge before finally falling": "Durante la invasión de Eldoral, se dice que la pícara mediana Herah mató a más de cien orcos mientras defendía una gran bóveda de conocimiento mágico antes de caer finalmente",
    "#LIGHT_BLUE#Revealing Map.": "#LIGHT_BLUE#Revelando Mapa.",
    "#LIGHT_BLUE# Current base actor: %s": "#LIGHT_BLUE# Actor base actual: %s",
    "#LIGHT_BLUE# Clear base actor: %s": "#LIGHT_BLUE# Limpiar actor base: %s",
    "#LIGHT_BLUE# Reset Randboss Data": "#LIGHT_BLUE# Reiniciar Datos de Jefe Aleatorio",
    "#LIGHT_BLUE#Bad filter for base actor: %s": "#LIGHT_BLUE#Filtro incorrecto para actor base: %s",
    "#LIGHT_BLUE#AdvanceActor inputs: %s": "#LIGHT_BLUE#Entradas de AdvanceActor: %s",
    "%s #GOLD#Forcing all Base Stats to %s": "%s #GOLD#Forzando todas las Estadísticas Base a %s",
    "%s #GOLD#Forcing all Bonus Stats to %s": "%s #GOLD#Forzando todas las Estadísticas de Bonus a %s",
    "%d category point(s)": "%d punto(s) de categoría",
    "#LIGHT_BLUE# Creating %d items:": "#LIGHT_BLUE# Creando %d objetos:",
    "#LIGHT_BLUE# * +5 Luck": "#LIGHT_BLUE# * +5 Suerte",
    "%s (blighted aura)": "%s (aura corrupta)",
    "%s (fell aura)": "%s (aura siniestra)",
    "%s (life aura)": "%s (aura de vida)",
    "%s (protective aura)": "%s (aura protectora)",
    "%s (spellblaze aura)": "%s (aura de hechizo llameante)",
    "%s (slimey)": "%s (viscoso)",
    "Crystalline %s": "%s Cristalino",
    # "elemental" → same in Spanish
    # "gwelgoroth" → proper name
    # NPC type names that should stay
    "affinity %d%%; reduction %d; dur %d; cd %d": "afinidad %d%%; reducción %d; dur %d; cd %d",
    "No Winter Storm Active": "No hay Tormenta Invernal Activa",
    "Tales of Maj'Eyal: Age of Ascendancy": "Tales of Maj'Eyal: Era de Ascendencia",
    "Scintillating Caves": "Cuevas Centelleantes",
    "Toggle UI display": "Alternar pantalla de IU",
    "Bikini / Mankini": "Bikini / Mankini",
    # === Última pasada: mensajes de combate y format restantes ===
    "%s quaffs the %s!": "¡%s bebe %s!",
    "%s siphons space and time into %s %s!": "¡%s drena espacio y tiempo en %s %s!",
    "%s revels in the bloodlust of %s %s!": "¡%s se regocija en la sed de sangre de %s %s!",
    "Poltergeist %s": "Poltergeist %s",
    "Moving %s": "Moviendo %s",
    "#GOLD#PLACED LESSER VAULT: %s": "#GOLD#BÓVEDA MENOR COLOCADA: %s",
    "#STEEL_BLUE#Casts %s.": "#STEEL_BLUE#Lanza %s.",
    "#STEEL_BLUE#Targeting %s": "#STEEL_BLUE#Apuntando %s",
    "range %d": "alcance %d",
    "#CADET_BLUE#Placing %s...": "#CADET_BLUE#Colocando %s...",
    "rad %d; dur %d;": "rad %d; dur %d;",
    "dur %d; cd %d": "dur %d; rec %d;",
    "#Source#'s mindstar telekinetically grabs #target#!": "¡La mente-estrella de #Source# agarra telequinéticamente a #target#!",
    "imbue %s": "imbuir %s",
    "#Source#'s rage subsides!": "¡La furia de #Source# se calma!",
    "#SANDY_BROWN#%s (Race Evolution)": "#SANDY_BROWN#%s (Evolución de Raza)",
    "-Wraithform": "-Forma Espectral",
    "-Flawed": "-Defectuoso",
    "+Spellshocked": "+Conmocionado por Hechizos",
    "#Target# warded against %s!": "¡#Target# protegido contra %s!",
    "#Target#'s %s ward fades": "La protección %s de #Target# se desvanece",
    "-Ward": "-Protección",
    "-Suncloak": "-Manto Solar",
    "-Lightburn": "-Quemadura de Luz",
    "-Blink": "-Parpadeo",
    "-Breach": "-Brecha",
    "-Braided": "-Trenzado",
    "%d Fateweaver": "Tejedor de Destino %d",
    "-Fateweaver": "-Tejedor de Destino",
    "-Tether": "-Atadura",
    "-Shadowguard": "-Guardia Sombría",
    "-Agony": "-Agonía",
    "+Maligned": "+Maligno",
    "-Despair": "-Desesperación",
    "+Frenzy": "+Frenesí",
    "-Frenzy": "-Frenesí",
    "Stalking %d/%d +%d": "Acechando %d/%d +%d",
    "#CRIMSON##Source# leeches life from #Target#!": "¡#CRIMSON##Source# drena vida de #Target#!",
    "#Source# deflects the projectile from #Target# %s": "#Source# desvía el proyectil de #Target# %s",
    "#STEEL_BLUE#Casting %s.": "#STEEL_BLUE#Lanzando %s.",
    "-Smeared": "-Manchado",
    "-Suffocating": "-Asfixiante",
    "-Smearing": "-Manchando",
    "#Target# prepares %s!": "¡#Target# prepara %s!",
    "-Hunter": "-Cazador",
    "-Maimed": "-Lisiado",
    "%d Combo": "Combo %d",
    "-Off-guard": "-Descuidado",
    "-Ravage": "-Devastar",
    "-Mucus": "-Mucosidad",
    "+Garrote": "+Estrangulamiento",
    "-Garrote": "-Estrangulamiento",
    "-Sedated": "-Sedado",
    "-Escape": "-Escape",
    "-Sentinel": "-Centinela",
    "-Pitch": "-Lanzamiento",
    "-Maim": "-Lisiar",
    "-Snipe": "-Francotiro",
    "+Eldoral": "+Eldoral",
    "-Eldoral": "-Eldoral",
    "#LIGHT_BLUE#Unarmed:#LAST#": "#LIGHT_BLUE#Sin armas:#LAST#",
    "#DARK_GREEN##Source# shares damage with %s oozes!": "#DARK_GREEN#¡#Source# comparte daño con %s limos!",
    "#LIGHT_GREEN#%s": "#LIGHT_GREEN#%s",
}


def translate_all():
    count = 0

    for f in sorted(BASE.rglob("*.lua")):
        content = f.read_text("utf-8")
        lines = content.split("\n")
        new_lines = list(lines)
        changed = False

        for i, line in enumerate(lines):
            stripped = line.strip()
            m = T_PATTERN.match(stripped)
            if not m:
                continue

            orig, trans = m.group(1), m.group(2)

            if orig != trans:
                continue
            if not orig.strip():
                continue

            if orig in TRANSLATIONS:
                new_trans = TRANSLATIONS[orig]
                if new_trans != orig:
                    indent = line[: len(line) - len(line.lstrip())]
                    new_trans.replace("\\", "\\\\").replace('"', '\\"')
                    # El string puede tener % que no se escapan
                    new_lines[i] = f'{indent}t("{orig}", "{new_trans}", "_t")'
                    changed = True
                    count += 1

        if changed:
            f.write_text("\n".join(new_lines), "utf-8")

    print(f"\nTotal traducidas: {count}")
    return count


if __name__ == "__main__":
    print("=" * 60)
    print("FASE 1: Stat templates")
    print("=" * 60)
    s1 = translate_stat_templates()

    print("\n" + "=" * 60)
    print("FASE 2: Todas las traducciones manuales")
    print("=" * 60)
    s2 = translate_all()

    print(f"\n\nRESUMEN: {s1 + s2} traducciones aplicadas")
