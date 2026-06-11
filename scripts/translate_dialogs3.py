#!/usr/bin/env python3
"""Traduce CharacterSheet, GameOptions, LevelupDialog y UseTalents."""

import re
from pathlib import Path

BASE = Path(__file__).parent.parent
DIALOGS = BASE / "translations" / "es" / "mod-tome-split" / "mod" / "dialogs"

DICT = {
    # ====== CHARACTER SHEET ======
    "[G]eneral": "[G]eneral",
    "range %2d": "alcance %2d",
    "vs ": "vs ",
    "File: %s": "Archivo: %s",
    "die:%+d": "muerte:%+d",
    "%+.0f max": "%+.0f max",
    "%sAll ": "%sTodo ",  # Partial, but better
    "Current Feedback gain is %0.1f%% of damage taken.": "Ganancia de Feedback actual es %0.1f%% del dano recibido.",
    "#LIGHT_BLUE#Saves:": "#LIGHT_BLUE#Salvaciones:",  # Already in dict but check exact
    # Ordinal format strings - keep as-is since they're format specifiers
    # These will stay in English ordinal format as they're technical
    # ====== GAME OPTIONS ======
    "UI": "UI",
    "Online": "Online",
    "Metal": "Metal",
    "Simple": "Simple",
    "Normal": "Normal",
    "#GOLD##{bold}#Always show lore popup#WHITE##{normal}#": "#GOLD##{bold}#Mostrar popup de lore#WHITE##{normal}#",
    "Toggles between a normal or flagpost tactical bars.#WHITE#": "Alterna entre barras tacticas normales o de bandera.#WHITE#",
    "#GOLD##{bold}#Flagpost tactical bars#WHITE##{normal}#": "#GOLD##{bold}#Barras de bandera#WHITE##{normal}#",
    "#GOLD##{bold}#Healthbars position#WHITE##{normal}#": "#GOLD##{bold}#Posicion de barras de vida#WHITE##{normal}#",
    "Toggles advanced weapon statistics display.#WHITE#": "Muestra estadisticas avanzadas de armas.#WHITE#",
    "#GOLD##{bold}#Advanced Weapon Statistics#WHITE##{normal}#": "#GOLD##{bold}#Estadisticas avanzadas#WHITE##{normal}#",
    "#GOLD##{bold}#Display mouse gesture trails#WHITE##{normal}#": "#GOLD##{bold}#Estelas de gestos#WHITE##{normal}#",
    "#GOLD##{bold}#Enable WASD movement keys#WHITE##{normal}#": "#GOLD##{bold}#Teclas WASD#WHITE##{normal}#",
    "#GOLD##{bold}#Weather effects#WHITE##{normal}#": "#GOLD##{bold}#Efectos climaticos#WHITE##{normal}#",
    "#GOLD##{bold}#Day/night light cycle#WHITE##{normal}#": "#GOLD##{bold}#Ciclo dia/noche#WHITE##{normal}#",
    "#GOLD##{bold}#Use mouse to move#WHITE##{normal}#": "#GOLD##{bold}#Mover con raton#WHITE##{normal}#",
    "#GOLD##{bold}#Quick melee targeting#WHITE##{normal}#": "#GOLD##{bold}#Apuntado rapido C.C.#WHITE##{normal}#",
    "#GOLD##{bold}#Mouse targeting#WHITE##{normal}#": "#GOLD##{bold}#Apuntado con raton#WHITE##{normal}#",
    "#GOLD##{bold}#Auto-accept target#WHITE##{normal}#": "#GOLD##{bold}#Auto-aceptar objetivo#WHITE##{normal}#",
    "Always rest to full before auto-exploring.#WHITE#": "Descansar siempre al maximo antes de autoexplorar.#WHITE#",
    "#GOLD##{bold}#Show quests in tooltips#WHITE##{normal}#": "#GOLD##{bold}#Misiones en tooltips#WHITE##{normal}#",
    "#GOLD##{bold}#Count of each monster in telepathy#WHITE##{normal}#": "#GOLD##{bold}#Conteo de monstruos#WHITE##{normal}#",
    "#GOLD##{bold}#Auto accept rename#WHITE##{normal}#": "#GOLD##{bold}#Auto-aceptar renombrar#WHITE##{normal}#",
    "#GOLD##{bold}#Auto use insignias of learning#WHITE##{normal}#": "#GOLD##{bold}#Auto-usar insignias#WHITE##{normal}#",
    "#GOLD##{bold}#Display mode for chat tabs#WHITE##{normal}#": "#GOLD##{bold}#Pestanas de chat#WHITE##{normal}#",
    "#GOLD##{bold}#Tactical overlay#WHITE##{normal}#": "#GOLD##{bold}#Superposicion tactica#WHITE##{normal}#",
    "#GOLD##{bold}#Life Lost Warning#WHITE##{normal}#": "#GOLD##{bold}#Aviso de poca vida#WHITE##{normal}#",
    "#GOLD##{bold}#Show hotkey names#WHITE##{normal}#": "#GOLD##{bold}#Mostrar nombres teclas#WHITE##{normal}#",
    "#GOLD##{bold}#Display map grid lines#WHITE##{normal}#": "#GOLD##{bold}#Lineas de cuadricula#WHITE##{normal}#",
    "#GOLD##{bold}#Icons status effects#WHITE##{normal}#": "#GOLD##{bold}#Iconos de efectos#WHITE##{normal}#",
    "#GOLD##{bold}#Log fade time#WHITE##{normal}#": "#GOLD##{bold}#Tiempo de fade#WHITE##{normal}#",
    "#GOLD##{bold}#Duration of flying text#WHITE##{normal}#": "#GOLD##{bold}#Texto flotante#WHITE##{normal}#",
    "#GOLD##{bold}#Graphic Mode#WHITE##{normal}#": "#GOLD##{bold}#Modo grafico#WHITE##{normal}#",
    "#GOLD##{bold}#Smooth creatures movement#WHITE##{normal}#": "#GOLD##{bold}#Movimiento suave#WHITE##{normal}#",
    "#GOLD##{bold}#Big Quest Popups#WHITE##{normal}#": "#GOLD##{bold}#Popups de misiones#WHITE##{normal}#",
    "#GOLD##{bold}#Visual hotkeys feedback#WHITE##{normal}#": "#GOLD##{bold}#Feedback visual teclas#WHITE##{normal}#",
    # ====== LEVELUP DIALOG ======
    "You do not know this category!": "No conoces esta categoria!",
    "You cannot unlearn this category because of: %s": "No puedes olvidar por: %s",
    "You can use a category point to unlock a new inscription slot (up to 5 slots).": "Puedes usar 1 punto para desbloquear un espacio de inscripcion (max 5).",
    "You have learnt all the inscription slots you could.": "Ya tienes todos los espacios de inscripcion.",
    "You can learn %d new slot(s). Do you wish to buy one with one category point?": "Puedes aprender %d espacio(s). ?Comprar con 1 punto de categoria?",
    "Category points: %s": "Puntos de categoria: %s",
    "You can still learn %d new slot(s) but you need a category point.": "Aun puedes aprender %d espacio(s), pero necesitas 1 punto.",
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
    "Object": "Objeto",
    "Sustaining": "Sosteniendo",
    "Use Talents: %s": "Usar talentos: %s",
    "Status": "Estado",
    "Hotkey": "Tecla rapida",
    "Mouse Click": "Click de raton",
    "Hotkey %s assigned": "Tecla %s asignada",
    "%s assigned to hotkey %s": "%s asignado a tecla %s",
    "Unbind": "Desasignar",
    "Bind to left mouse click (on a target)": "Asignar a click izquierdo (objetivo)",
    "Bind to middle mouse click (on a target)": "Asignar a click medio (objetivo)",
    "Link in chat": "Enlazar en chat",
    "Range: %d": "Alcance: %d",
    "Uses: %d": "Usos: %d",
    "Radius": "Radio",
    "Power": "Poder",
}


def translate_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    count = 0
    for orig, trans in sorted(DICT.items(), key=lambda x: -len(x[0])):
        old = f't("{orig}", "{orig}",'
        new = f't("{orig}", "{trans}",'
        if old in content:
            content = content.replace(old, new)
            count += 1
    if count > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO DIALOGOS FALTANTES")
    print("=" * 60)
    total = 0
    for fname in [
        "CharacterSheet.lua",
        "GameOptions.lua",
        "LevelupDialog.lua",
        "UseTalents.lua",
    ]:
        fpath = DIALOGS / fname
        if fpath.exists():
            c = translate_file(fpath)
            print(f"  {fname}: +{c}")
            total += c
    print(f"\n  Total: {total}")


if __name__ == "__main__":
    main()
