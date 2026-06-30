#!/usr/bin/env python3
"""
Traduce todos los archivos de diálogo (pantallas del juego).
Cubre CharacterSheet, GameOptions, LevelupDialog, Birther, etc.

Uso: python3 scripts/translate_dialogs.py
"""

import re
from pathlib import Path

DIALOG_DIR = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "mod"
    / "dialogs"
)

# Diccionario general para diálogos
DICT = {
    # === CharacterSheet (pantalla de personaje) ===
    "Character Sheet": "Ficha del personaje",
    "Stats": "Atributos",
    "Resistances": "Resistencias",
    "Damage": "Daño",
    "Defense": "Defensa",
    "Armor": "Armadura",
    "Health": "Salud",
    "Mana": "Maná",
    "Stamina": "Resistencia",
    "Equilibrium": "Equilibrio",
    "Positive energy": "Energía positiva",
    "Negative energy": "Energía negativa",
    "Paradox": "Paradoja",
    "Vim": "Vim",
    "Souls": "Almas",
    "Steam": "Vapor",
    "Psi": "Psique",
    "Hate": "Odio",
    "Level": "Nivel",
    "Experience": "Experiencia",
    "Exp needed for next level": "Exp necesaria para siguiente nivel",
    "Strength": "Fuerza",
    "Dexterity": "Destreza",
    "Constitution": "Constitución",
    "Magic": "Magia",
    "Willpower": "Voluntad",
    "Cunning": "Astucia",
    "Class": "Clase",
    "Race": "Raza",
    "Gender": "Género",
    "Age": "Edad",
    "Weight": "Peso",
    "Height": "Altura",
    "Size": "Tamaño",
    "Life": "Vida",
    "Accuracy": "Precisión",
    "Power": "Poder",
    "Spellpower": "Poder de hechizo",
    "Mindpower": "Poder mental",
    "Crit chance": "Prob. crítica",
    "Crit mult": "Mult. crítico",
    "Speed": "Velocidad",
    "Movement speed": "Velocidad de movimiento",
    "Attack speed": "Vel. de ataque",
    "Spell speed": "Vel. de hechizo",
    "Global speed": "Velocidad global",
    "Teleport": "Teletransporte",
    "Immunities": "Inmunidades",
    "Blindness immunity": "Inmunidad a ceguera",
    "Confusion immunity": "Inmunidad a confusión",
    "Fear immunity": "Inmunidad a miedo",
    "Poison immunity": "Inmunidad a veneno",
    "Disease immunity": "Inmunidad a enfermedad",
    "Stun immunity": "Inmunidad a aturdimiento",
    "Knockback immunity": "Inmunidad a derribo",
    "Death immunity": "Inmunidad a muerte",
    "Talent": "Talento",
    "Talents": "Talentos",
    "Description": "Descripción",
    "Effects": "Efectos",
    "Range": "Alcance",
    "Radius": "Radio",
    "Duration": "Duración",
    "Cooldown": "Enfriamiento",
    "Cost": "Coste",
    "Sustain": "Sostenido",
    "Use mode": "Modo de uso",
    "Activate": "Activar",
    "Sustain": "Sostener",
    "Passive": "Pasivo",
    # === GameOptions (opciones del juego) ===
    "Game Options": "Opciones del juego",
    "Video": "Vídeo",
    "Audio": "Audio",
    "Gameplay": "Jugabilidad",
    "Interface": "Interfaz",
    "Keybindings": "Teclas",
    "Chat": "Chat",
    "Accessibility": "Accesibilidad",
    "Misc": "Varios",
    "Volume": "Volumen",
    "Master": "General",
    "Music": "Música",
    "Sound": "Sonido",
    "Ambient": "Ambiente",
    "Language": "Idioma",
    "Font": "Fuente",
    "Font size": "Tamaño de fuente",
    "UI Scale": "Escala de UI",
    "Tooltip delay": "Retardo de tooltips",
    "Show tooltips": "Mostrar tooltips",
    "Always center on player": "Centrar siempre en jugador",
    "Show minimap": "Mostrar minimapa",
    "Show FPS": "Mostrar FPS",
    "Show clock": "Mostrar reloj",
    "Auto explore": "Autoexplorar",
    "Auto rest": "Autodescansar",
    "Auto pickup": "Auto-recoger",
    "Auto save": "Autoguardar",
    "Difficulty": "Dificultad",
    "Permadeath": "Muerte permanente",
    "Campaign": "Campaña",
    "Resolution": "Resolución",
    "Fullscreen": "Pantalla completa",
    "Windowed": "Ventana",
    "Borderless": "Sin bordes",
    "VSync": "VSync",
    "Shaders": "Shaders",
    "Particles": "Partículas",
    "Antialiasing": "Antialiasing",
    "Texture quality": "Calidad de texturas",
    "Shadow quality": "Calidad de sombras",
    "Default": "Por defecto",
    "Custom": "Personalizado",
    "Reset to defaults": "Restablecer valores",
    "Apply": "Aplicar",
    "Cancel": "Cancelar",
    # === LevelupDialog (subir de nivel) ===
    "Level up!": "¡Subir de nivel!",
    "Level up": "Subir de nivel",
    "Choose a talent to level up": "Elige un talento para subir",
    "Learn a new talent": "Aprender un talento nuevo",
    "Improve a stat": "Mejorar un atributo",
    "Increase": "Aumentar",
    "Points remaining": "Puntos restantes",
    "Class talents": "Talentos de clase",
    "Generic talents": "Talentos genéricos",
    "Stat points": "Puntos de atributo",
    "Class points": "Puntos de clase",
    "Generic points": "Puntos genéricos",
    "Prodigies": "Prodigios",
    "Prodigy points": "Puntos de prodigio",
    "Unlock": "Desbloquear",
    "Locked": "Bloqueado",
    "Requirements": "Requisitos",
    "Not enough stat points": "No hay suficientes puntos de atributo",
    "Not enough class points": "No hay suficientes puntos de clase",
    "Not enough generic points": "No hay suficientes puntos genéricos",
    "Confirm": "Confirmar",
    "Max level reached": "Nivel máximo alcanzado",
    # === Birther (creación de personaje) ===
    "New Character": "Nuevo personaje",
    "Create": "Crear",
    "Random": "Aleatorio",
    "Quick birth": "Creación rápida",
    "Back": "Atrás",
    "Next": "Siguiente",
    "Previous": "Anterior",
    "Finish": "Finalizar",
    "Choose your race": "Elige tu raza",
    "Choose your class": "Elige tu clase",
    "Customize your character": "Personaliza tu personaje",
    "Enter a name for your character": "Escribe un nombre para tu personaje",
    "Name": "Nombre",
    "Male": "Masculino",
    "Female": "Femenino",
    "Random name": "Nombre aleatorio",
    "Starting equipment": "Equipo inicial",
    "Starting talents": "Talentos iniciales",
    "Life per level": "Vida por nivel",
    "Experience penalty": "Penalización de experiencia",
    "Race talents": "Talentos raciales",
    # === DeathDialog (pantalla de muerte) ===
    "You have died!": "¡Has muerto!",
    "You have been killed by %s.": "Has muerto a manos de %s.",
    "You were killed by %s.": "Fuiste asesinado por %s.",
    "Death": "Muerte",
    "Respawn": "Reaparecer",
    "Load last save": "Cargar último guardado",
    "Load game": "Cargar partida",
    "Main menu": "Menú principal",
    "Quit": "Salir",
    "Play again": "Jugar de nuevo",
    # === MapMenu (mapa) ===
    "Map": "Mapa",
    "World Map": "Mapa del mundo",
    "Area Map": "Mapa de la zona",
    "Zoom in": "Acercar",
    "Zoom out": "Alejar",
    "Center on player": "Centrar en jugador",
    "Show all": "Mostrar todo",
    "Hide": "Ocultar",
    "Levels": "Niveles",
    "Show level %d": "Mostrar nivel %d",
    # === UseTalents (usar talentos) ===
    "Use Talent": "Usar talento",
    "Select a target": "Selecciona un objetivo",
    "Target": "Objetivo",
    "Self": "Uno mismo",
    "Enemies": "Enemigos",
    "Friends": "Aliados",
    "All": "Todos",
    # === GraphicMode ===
    "Graphic Mode": "Modo gráfico",
    "Tiles": "Tiles",
    "ASCII": "ASCII",
    "Switch to": "Cambiar a",
    "Current mode": "Modo actual",
    # === Donation ===
    "Donate": "Donar",
    "Thank you for your support!": "¡Gracias por tu apoyo!",
    "Support the game": "Apoyar el juego",
    "Donator benefits": "Beneficios de donante",
    "Close": "Cerrar",
}


def translate_file(fpath):
    """Traduce un archivo de diálogo."""
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
    print("  TRADUCIENDO DIÁLOGOS (pantallas del juego)")
    print("=" * 60)

    if not DIALOG_DIR.exists():
        print(f"  ERROR: {DIALOG_DIR} no encontrado")
        return

    total = 0
    files_done = 0

    for fpath in sorted(DIALOG_DIR.glob("*.lua")):
        count = translate_file(fpath)
        if count > 0:
            print(f"  ✅ {fpath.name}: {count} traducciones")
            total += count
            files_done += 1

    if files_done == 0:
        print(f"  No se encontraron archivos para traducir en {DIALOG_DIR}")
        # Intentar también en subdirectorios
        for subdir in ["debug", "elements", "orders", "shimmer", "talents"]:
            subpath = DIALOG_DIR / subdir
            if subpath.exists():
                for fpath in sorted(subpath.glob("*.lua")):
                    count = translate_file(fpath)
                    if count > 0:
                        print(f"  ✅ {subdir}/{fpath.name}: {count} traducciones")
                        total += count
                        files_done += 1

    print(f"\n  📊 Total: {total} traducciones en {files_done} archivos")
    print()


if __name__ == "__main__":
    main()
