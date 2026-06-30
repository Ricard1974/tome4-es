#!/usr/bin/env python3
"""
Traduce menús principales y pantalla de personaje.
Cubre todo lo que ve el jugador en los menús principales y la ficha de personaje.
"""

from pathlib import Path

BOOT_LOCALE = (
    Path(__file__).parent.parent / "boot-spanish" / "data" / "locales" / "es.lua"
)
CHAR_SHEET = (
    Path(__file__).parent.parent
    / "translations"
    / "es"
    / "mod-tome-split"
    / "mod"
    / "dialogs"
    / "CharacterSheet.lua"
)
ENGINE_LOCALE = Path(__file__).parent.parent / "translations" / "es" / "engine.lua"

# =============================================================================
# TRADUCCIONES PARA MENÚS PRINCIPALES (boot-spanish)
# =============================================================================
BOOT_TRANSLATIONS = {
    "Language Selection": "Selección de idioma",
    "Donate": "Donar",
    "Thank you for your support!": "¡Gracias por tu apoyo!",
    "Support the development of Tales of Maj'Eyal": "Apoya el desarrollo de Tales of Maj'Eyal",
    "You can choose to donate any amount you wish.": "Puedes donar la cantidad que desees.",
    "Online Store": "Tienda Online",
    "The Online Store": "La Tienda Online",
    "Play!": "¡Jugar!",
    "Playing": "Jugando",
    "Logging in...": "Iniciando sesión...",
    "Profile logged in!": "¡Perfil conectado!",
    "Your online profile is now active. Have fun!": "Tu perfil online está activo. ¡Diviértete!",
    "Login failed!": "¡Error al iniciar sesión!",
    "Check your login and password or try again in a few moments.": "Comprueba tu usuario y contraseña o inténtalo de nuevo.",
    "Registering...": "Registrando...",
    "Registering on https://te4.org/, please wait...": "Registrando en https://te4.org/, espera...",
    "Logged in!": "¡Sesión iniciada!",
    "Profile created!": "¡Perfil creado!",
    "Profile creation failed!": "¡Error al crear perfil!",
    "Try again in a few moments, or try online at https://te4.org/": "Inténtalo de nuevo o prueba online en https://te4.org/",
    "Welcome to Tales of Maj'Eyal": "Bienvenido a Tales of Maj'Eyal",
    "Register now!": "¡Regístrate ahora!",
    "Login existing account": "Iniciar sesión",
    "Maybe later": "Quizás más tarde",
    "Disable all online features": "Desactivar funciones online",
    "Disable all connectivity": "Desactivar toda conectividad",
    "Disable all!": "¡Desactivar todo!",
    "Logging in your account, please wait...": "Iniciando sesión, espera...",
    "Login with Steam": "Iniciar sesión con Steam",
    "Steam User Account": "Cuenta de Steam",
    "Steam client not found.": "Cliente Steam no encontrado.",
    "Nothing to update": "Nada que actualizar",
    "Update All": "Actualizar todo",
    "Reboot": "Reiniciar",
    "Update all game modules": "Actualizar todos los módulos",
    "Show all versions": "Mostrar todas las versiones",
    "Show older versions": "Mostrar versiones antiguas",
    "View High Scores": "Ver puntuaciones",
    "Create": "Crear",
    "Update": "Actualizar",
    "Checking for updates...": "Buscando actualizaciones...",
    "Update available": "Actualización disponible",
    "Downloading...": "Descargando...",
    "Update complete": "Actualización completa",
    "Restart now": "Reiniciar ahora",
    "Restart later": "Reiniciar después",
    "Component": "Componente",
    "Credits": "Créditos",
    "Addon installation successful. New addons are only active for new characters.": "Addon instalado correctamente. Solo funciona para personajes nuevos.",
    "Online profile": "Perfil online",
    "Offline mode": "Modo offline",
    "Connecting...": "Conectando...",
    "Connected": "Conectado",
    "Disconnected": "Desconectado",
    "Logged in": "Conectado",
    "Log out": "Cerrar sesión",
    "Do you want to log out?": "¿Quieres cerrar sesión?",
    "You are logged in": "Has iniciado sesión",
    "Player Profile": "Perfil del jugador",
    "Privacy Policy (opens in browser)": "Política de privacidad (se abre en el navegador)",
    "You can get new addons at #LIGHT_BLUE##{underline}#Te4.org Addons#{normal}#": "Puedes conseguir addons en #LIGHT_BLUE##{underline}#Te4.org Addons#{normal}#",
    "You can get new addons on #LIGHT_BLUE##{underline}#Steam Workshop#{normal}#": "Puedes conseguir addons en #LIGHT_BLUE##{underline}#Steam Workshop#{normal}#",
    "LEVEL UP!": "¡SUBIR DE NIVEL!",
    "Addon Version": "Versión del addon",
    "Game Version": "Versión del juego",
    "Game Module": "Módulo del juego",
    "Show incompatible": "Mostrar incompatibles",
    "None": "Ninguno",
    "Steam Options": "Opciones de Steam",
    "Purge Cloud Saves": "Purgar guardado en la nube",
    "Cloud Saves": "Guardado en la nube",
    "All data purged from the cloud.": "Todos los datos purgados de la nube.",
    "Confirm purge?": "¿Confirmar purga?",
    "Tales of Maj'Eyal": "Tales of Maj'Eyal",
    "Main Campaign": "Campaña principal",
    "Arena": "Arena",
    "Infinite Dungeon": "Mazmorra infinita",
    "Welcome to T-Engine and the Tales of Maj'Eyal": "Bienvenido a T-Engine y Tales of Maj'Eyal",
}


# =============================================================================
# TRADUCCIONES PARA PANTALLA DE PERSONAJE
# =============================================================================
CHAR_SHEET_TRANSLATIONS = {
    "[G]eneral": "[G]eneral",
    "#LIGHT_BLUE#Physical:": "#LIGHT_BLUE#Físico:",
    "#LIGHT_BLUE#Magical:": "#LIGHT_BLUE#Mágico:",
    "#LIGHT_BLUE#Mental:": "#LIGHT_BLUE#Mental:",
    "#LIGHT_BLUE#Damage Modifiers:": "#LIGHT_BLUE#Modificadores de daño:",
    "vs ": "vs ",
    "Heavy armor": "Armadura pesada",
    "Massive armor": "Armadura masiva",
    "Light armor": "Armadura ligera",
    "#LIGHT_BLUE#Saves:": "#LIGHT_BLUE#Salvaciones:",
    "Absolute": "Absoluto",
    "Speed Res": "Resistencia de velocidad",
    "#LIGHT_BLUE#Flat resistances:": "#LIGHT_BLUE#Resistencias planas:",
    "#LIGHT_BLUE#Damage when hit:": "#LIGHT_BLUE#Daño al recibir golpe:",
    "Inscriptions": "Inscripciones",
    "Item_Talents": "Talentos de objeto",
    "Instant": "Instantáneo",
    "Activated": "Activado",
    "Sustained": "Sostenido",
    "Character dump complete": "Volcado de personaje completado",
    "Character Sheet": "Ficha del personaje",
    "#GOLD#All Status     ": "#GOLD#Todos los estados",
    ":STR": ":FUE",
    ":DEX": ":DES",
    ":CON": ":CON",
    ":MAG": ":MAG",
    ":WIL": ":VOL",
    ":CUN": ":AST",
    "STR": "FUE",
    "DEX": "DES",
    "CON": "CON",
    "MAG": "MAG",
    "WIL": "VOL",
    "CUN": "AST",
    "Physical": "Físico",
    "Magical": "Mágico",
    "Mental": "Mental",
    "All": "Todo",
    "none": "ninguno",
    "Nothing": "Nada",
    "Increases": "Aumenta",
    "Decreases": "Reduce",
    "Weapon": "Arma",
    "Armor": "Armadura",
    "Defense": "Defensa",
    "Accuracy": "Precisión",
    "Damage": "Daño",
    "Range": "Alcance",
    "Speed": "Velocidad",
    "Power": "Poder",
    "#RED#Displaying %s set for %s (equipment NOT switched)": "#RED#Mostrando conjunto %s para %s (equipo NO cambiado)",
    "Health": "Salud",
    "Mana": "Maná",
    "Stamina": "Resistencia",
    "Equilibrium": "Equilibrio",
    "Vim": "Vim",
    "Positive": "Positiva",
    "Negative": "Negativa",
    "Paradox": "Paradoja",
    "Steam": "Vapor",
    "Level": "Nivel",
    "Experience": "Experiencia",
    "Life": "Vida",
    "Class": "Clase",
    "Race": "Raza",
    "Gender": "Género",
    "Male": "Masculino",
    "Female": "Femenino",
    "Size": "Tamaño",
    "big": "grande",
    "bigger": "más grande",
    "huge": "enorme",
    "massive": "masivo",
    "small": "pequeño",
    "tiny": "diminuto",
    "Sex": "Sexo",
    "Type": "Tipo",
    "Subtype": "Subtipo",
    "Rank": "Rango",
    "Normal": "Normal",
    "unique": "único",
    "boss": "jefe",
    "rare": "raro",
    "elite": "élite",
}


def translate_file(filepath, translations):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for orig, trans in translations.items():
        old = f't("{orig}", "{orig}",'
        new = f't("{orig}", "{trans}",'
        if old in content:
            content = content.replace(old, new)
            count += 1
        else:
            # Intentar con escape de comillas
            old2 = f't("{orig}", "{orig}",'
            if old2 in content:
                content = content.replace(old2, new)
                count += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return count


def main():
    print("=" * 60)
    print("  TRADUCIENDO MENÚS Y PANTALLA DE PERSONAJE")
    print("=" * 60)

    total = 0

    # 1. Boot module (menú principal)
    if BOOT_LOCALE.exists():
        c = translate_file(BOOT_LOCALE, BOOT_TRANSLATIONS)
        print(f"  ✅ boot-spanish/locales/es.lua: +{c}")
        total += c
    else:
        print(f"  ⚠ No encontrado: {BOOT_LOCALE}")

    # 2. Character sheet
    if CHAR_SHEET.exists():
        c = translate_file(CHAR_SHEET, CHAR_SHEET_TRANSLATIONS)
        print(f"  ✅ CharacterSheet.lua: +{c}")
        total += c
    else:
        print(f"  ⚠ No encontrado: {CHAR_SHEET}")

    # 3. También engine.lua para algunos términos de menú que faltan
    if ENGINE_LOCALE.exists():
        c = translate_file(
            ENGINE_LOCALE,
            {
                "Purge Cloud Saves": "Purgar guardado en la nube",
                "Cloud Saves": "Guardado en la nube",
                "All data purged from the cloud.": "Todos los datos purgados de la nube.",
                "Confirm purge?": "¿Confirmar purga?",
                "Donate": "Donar",
                "Thank you for your support!": "¡Gracias por tu apoyo!",
                "Steam Options": "Opciones de Steam",
                "Nothing to update": "Nada que actualizar",
                "Update": "Actualizar",
                "Reboot": "Reiniciar",
            },
        )
        print(f"  ✅ engine.lua: +{c}")
        total += c

    print(f"\n  📊 Total: {total} traducciones")
    print()


if __name__ == "__main__":
    main()
