#!/usr/bin/env python3
"""
Traduce todos los diálogos de pantalla restantes.
Cubre: CharacterSheet, GameOptions, LevelupDialog, UseTalents,
Birther, DeathDialog, MapMenu, Donation y más.
"""

import re
from pathlib import Path

DIALOGS = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "mod"
    / "dialogs"
)

DICT = {
    # ====== CHARACTER SHEET ======
    "#LIGHT_BLUE#Physical:": "#LIGHT_BLUE#Fisico:",
    "#LIGHT_BLUE#Magical:": "#LIGHT_BLUE#Magico:",
    "#LIGHT_BLUE#Mental:": "#LIGHT_BLUE#Mental:",
    "#LIGHT_BLUE#Damage Modifiers:": "#LIGHT_BLUE#Modif. de dano:",
    "vs ": "vs ",
    "Heavy armor": "Armadura pesada",
    "Massive armor": "Armadura masiva",
    "Light armor": "Armadura ligera",
    "#LIGHT_BLUE#Saves:": "#LIGHT_BLUE#Salvaciones:",
    "Absolute": "Absoluto",
    "Speed Res": "Res. velocidad",
    "#LIGHT_BLUE#Flat resistances:": "#LIGHT_BLUE#Res. planas:",
    "#LIGHT_BLUE#Damage when hit:": "#LIGHT_BLUE#Dano al recibir:",
    "Inscriptions": "Inscripciones",
    "Item_Talents": "Tal. de objeto",
    "Instant": "Instantaneo",
    "Activated": "Activado",
    "Sustained": "Sostenido",
    "Character dump complete": "Volcado completo",
    "Sex  : ": "Sexo: ",
    "big": "grande",
    "bigger": "mas grande",
    "huge": "enorme",
    "massive": "masivo",
    "small": "pequeno",
    "tiny": "diminuto",
    "Sex": "Sexo",
    "Subtype": "Subtipo",
    "Rank": "Rango",
    "unique": "unico",
    "boss": "jefe",
    "elite": "elite",
    "rare": "raro",
    "#ORANGE#Physical Status": "#ORANGE#Estado fisico",
    "#ORANGE#Mental Status": "#ORANGE#Estado mental",
    "#ORANGE#Magical Status": "#ORANGE#Estado magico",
    "#LIGHT_BLUE#Vision:": "#LIGHT_BLUE#Vision:",
    "#LIGHT_BLUE#Speeds:": "#LIGHT_BLUE#Velocidades:",
    "#LIGHT_BLUE#Resources:": "#LIGHT_BLUE#Recursos:",
    "#LIGHT_BLUE#Current effects:": "#LIGHT_BLUE#Efectos actuales:",
    # ====== GAME OPTIONS ======
    "#GOLD##{bold}#Creatures movement speed#WHITE##{normal}#": "#GOLD##{bold}#Vel. criaturas#WHITE##{normal}#",
    "#GOLD##{bold}#Bold font for selected items#WHITE##{normal}#": "#GOLD##{bold}#Negrita en seleccion#WHITE##{normal}#",
    "#GOLD##{bold}#Show key bindings in tooltips#WHITE##{normal}#": "#GOLD##{bold}#Teclas en tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Show quests in tooltips#WHITE##{normal}#": "#GOLD##{bold}#Misiones en tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Display floating text for damage/healing#WHITE##{normal}#": "#GOLD##{bold}#Texto flotante#WHITE##{normal}#",
    "#GOLD##{bold}#Size of tooltip background#WHITE##{normal}#": "#GOLD##{bold}#Fondo tooltip#WHITE##{normal}#",
    "#GOLD##{bold}#Options tree auto collapse#WHITE##{normal}#": "#GOLD##{bold}#Auto-colapsar#WHITE##{normal}#",
    "#GOLD##{bold}#Combat log format#WHITE##{normal}#": "#GOLD##{bold}#Formato registro#WHITE##{normal}#",
    "#GOLD##{bold}#Always show chat#WHITE##{normal}#": "#GOLD##{bold}#Chat siempre visible#WHITE##{normal}#",
    "#GOLD##{bold}#Show donators only#WHITE##{normal}#": "#GOLD##{bold}#Solo donantes#WHITE##{normal}#",
    "#GOLD##{bold}#Chat timestamp#WHITE##{normal}#": "#GOLD##{bold}#Marca temporal#WHITE##{normal}#",
    "#GOLD##{bold}#Small screen layout#WHITE##{normal}#": "#GOLD##{bold}#Pantalla pequena#WHITE##{normal}#",
    "#GOLD##{bold}#Auto hide unused hotkeys#WHITE##{normal}#": "#GOLD##{bold}#Ocultar teclas no usadas#WHITE##{normal}#",
    "#GOLD##{bold}#Auto hide hotkey page buttons#WHITE##{normal}#": "#GOLD##{bold}#Ocultar paginas#WHITE##{normal}#",
    "#GOLD##{bold}#Tactical map style#WHITE##{normal}#": "#GOLD##{bold}#Mapa tactico#WHITE##{normal}#",
    "#GOLD##{bold}#Display mouse information#WHITE##{normal}#": "#GOLD##{bold}#Info. raton#WHITE##{normal}#",
    "#GOLD##{bold}#Display tooltip at mouse position#WHITE##{normal}#": "#GOLD##{bold}#Tooltip en raton#WHITE##{normal}#",
    "#GOLD##{bold}#Tactical map display#WHITE##{normal}#": "#GOLD##{bold}#Mapa tactico#WHITE##{normal}#",
    # ====== LEVELUP DIALOG ======
    "You do not know this category!": "No conoces esta categoria!",
    "You cannot unlearn this category because of: %s": "No puedes olvidar por: %s",
    "You can use a category point to unlock a new inscription slot (up to 5 slots).": "Puedes usar 1 punto para desbloquear un espacio de inscripcion (max 5).",
    "You have learnt all the inscription slots you could.": "Ya tienes todos los espacios de inscripcion.",
    "You can learn %d new slot(s). Do you wish to buy one with one category point?": "Puedes aprender %d espacio(s). ?Comprar uno con 1 punto de categoria?",
    "Category points: %s": "Puntos de categoria: %s",
    "You can still learn %d new slot(s) but you need a category point.": "Aun puedes aprender %d espacio(s), pero necesitas 1 punto de categoria.",
    "Stats: %s": "Atributos: %s",
    "Class points: %s": "Puntos de clase: %s",
    "Generic points: %s": "Puntos genericos: %s",
    "Hide unlearnt categories": "Ocultar categorias no aprendidas",
    "Current value: ": "Valor actual: ",
    "Base value: ": "Valor base: ",
    "Stat gives:": "El atributo da:",
    "Inscriptions": "Inscripciones",
    # ====== USE TALENTS ======
    "Active": "Activo",
    "%s turns": "%s turnos",
    "Unavailable": "No disponible",
    "Sustaining": "Sosteniendo",
    "Use Talents: %s": "Usar talentos: %s",
    "Hotkey": "Tecla rapida",
    "Mouse Click": "Click de raton",
    "Unbind": "Desasignar",
    "Bind to left mouse click (on a target)": "Asignar a click izquierdo (en objetivo)",
    "Bind to middle mouse click (on a target)": "Asignar a click medio (en objetivo)",
    "Link in chat": "Enlazar en chat",
    "Range: %d": "Alcance: %d",
    "Uses: %d": "Usos: %d",
    "Radius": "Radio",
    "Power": "Poder",
    # ====== BIRTHER ======
    "Character Creation": "Creacion de personaje",
    "Random!": "Aleatorio!",
    "Reroll": "Rehacer",
    "Refund": "Reembolsar",
    "Points left": "Puntos restantes",
    "Confirm and continue": "Confirmar y continuar",
    "Go back": "Volver atras",
    "Your character": "Tu personaje",
    "Summary": "Resumen",
    "Equipment": "Equipo",
    "Description": "Descripcion",
    "Stats": "Atributos",
    "Talents": "Talentos",
    "Load premade": "Cargar predisenado",
    "Custom tile": "Tile personalizado",
    "Customize": "Personalizar",
    "Extra Options": "Opciones extra",
    "Name: ": "Nombre: ",
    "Campaign: ": "Campa" + chr(241) + "a: ",  # Campaña
    "Difficulty: ": "Dificultad: ",
    "Permadeath: ": "Muerte permanente: ",
    "Pick one optional birth def": "Elige un defecto de nacimiento opcional",
    "No birth descriptors": "Sin descriptores de nacimiento",
    "Select a birth descriptor": "Selecciona un descriptor",
    "Birth descriptor: %s": "Descriptor: %s",
    "Adventure": "Aventura",
    "Roguelike": "Roguelike",
    "Exploration": "Exploracion",
    # ====== DEATH DIALOG ======
    "You have died!": "Has muerto!",
    "Main Menu": "Menu principal",
    # ====== MAP MENU ======
    "Actions": "Acciones",
    "Change level": "Cambiar nivel",
    "Pickup item": "Recoger objeto",
    "Move to": "Mover a",
    "Control": "Controlar",
    "Give order": "Dar orden",
    "Target player": "Apuntar a jugador",
}


def translate_all():
    count = 0
    for fpath in sorted(DIALOGS.glob("*.lua")):
        fc = 0
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        for orig, trans in sorted(DICT.items(), key=lambda x: -len(x[0])):
            old = f't("{orig}", "{orig}",'
            new = f't("{orig}", "{trans}",'
            if old in content:
                content = content.replace(old, new)
                fc += 1

        if fc > 0:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  {fpath.name}: +{fc}")
            count += fc

    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO TODOS LOS DIALOGOS")
    print("=" * 60)
    total = translate_all()
    print(f"\n  Total: {total} traducciones")


if __name__ == "__main__":
    main()
