#!/usr/bin/env python3
"""
Traduce el 100% de engine.lua.
Script definitivo que cubre todas las cadenas restantes.

Uso: python3 scripts/translate_engine_final.py
"""

import re
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
ENGINE_FILE = TRANS_DIR / "engine.lua"

# =============================================================================
# DICCIONARIO COMPLETO DE ENGINE.LUA
# =============================================================================
DICT = {
    # === Hotkeys (1-12 para todas las páginas) ===
    **{f"Seven Hotkey {i}": f"Tecla rápida séptima {i}" for i in range(1, 13)},
    "Previous Hotkey Page": "Página anterior de teclas",
    "Next Hotkey Page": "Página siguiente de teclas",
    "Quick switch to Hotkey Page 2": "Ir a página de teclas 2",
    "Quick switch to Hotkey Page 3": "Ir a página de teclas 3",
    "Toggle list of seen creatures": "Alternar lista de criaturas vistas",
    "Show message log": "Mostrar registro de mensajes",
    "Take a screenshot": "Capturar pantalla",
    "Show map": "Mostrar mapa",
    "Scroll map mode": "Modo desplazamiento de mapa",
    "Show inventory": "Mostrar inventario",
    "Show equipment": "Mostrar equipo",
    "Pickup items": "Recoger objetos",
    "Drop items": "Soltar objetos",
    "Wield/wear items": "Empuñar/vestir objetos",
    "Takeoff items": "Quitar objetos",
    "Use items": "Usar objetos",
    "Quick switch weapons set": "Cambiar rápido de armas",
    # === Movimiento ===
    "Move left": "Mover izquierda",
    "Move right": "Mover derecha",
    "Move up": "Mover arriba",
    "Move down": "Mover abajo",
    "Move diagonally left and up": "Mover diagonal izquierda arriba",
    "Move diagonally right and up": "Mover diagonal derecha arriba",
    "Move diagonally left and down": "Mover diagonal izquierda abajo",
    "Move diagonally right and down": "Mover diagonal derecha abajo",
    "Stay for a turn": "Esperar un turno",
    "Run": "Correr",
    "Run left": "Correr izquierda",
    "Run right": "Correr derecha",
    "Run up": "Correr arriba",
    "Run down": "Correr abajo",
    "Run diagonally left and up": "Correr diagonal izquierda arriba",
    "Run diagonally right and up": "Correr diagonal derecha arriba",
    "Run diagonally left and down": "Correr diagonal izquierda abajo",
    "Run diagonally right and down": "Correr diagonal derecha abajo",
    "movement": "movimiento",
    "Move left (WASD directions)": "Mover izquierda (direcciones WASD)",
    "Move right (WASD directions)": "Mover derecha (direcciones WASD)",
    "Move up (WASD directions)": "Mover arriba (direcciones WASD)",
    "Move down (WASD directions)": "Mover abajo (direcciones WASD)",
    # === Compras y objetos ===
    "List purchasable": "Listar comprable",
    "Use purchased": "Usar comprado",
    "(%d items in cart, %s)": "(%d objetos en carrito, %s)",
    # === Creación de personaje ===
    "Enter your character's name": "Introduce el nombre de tu personaje",
    "Random": "Aleatorio",
    "Quick Birth": "Creación rápida",
    "Do you want to recreate the same character?": "¿Quieres recrear el mismo personaje?",
    "Recreate": "Recrear",
    "New character": "Nuevo personaje",
    "Randomly selected %s.": "Seleccionado aleatoriamente: %s.",
    # === UI general ===
    "???": "???",
    "Lua Console": "Consola Lua",
    "Screenshot taken!": "¡Captura realizada!",
    "Message Log": "Registro de mensajes",
    "Test": "Prueba",
    "Beta Addons Disabled": "Addons beta desactivados",
    "#{italic}##PINK#Addons developers can still test their addons by enabling developer mode.#{normal}#": "#{italic}##PINK#Los desarrolladores pueden probar sus addons activando el modo desarrollador.#{normal}#",
    "Requires:": "Requiere:",
    "no online profile active": "sin perfil online activo",
    "cheat mode active": "modo trampas activo",
    "savefile tainted": "partida corrupta",
    "bad game version": "versión incorrecta",
    "bad game addon version": "versión de addon incorrecta",
    "nothing to update": "nada que actualizar",
    "unknown error": "error desconocido",
    "Registering character": "Registrando personaje",
    "Character is being registered on https://te4.org/": "Registrando personaje en https://te4.org/",
    "Retrieving data from the server": "Recuperando datos del servidor",
    "Retrieving...": "Recuperando...",
    # === Format strings con colores ===
    "#LIGHT_BLUE#%s#WHITE# is one of the top five played races": "#LIGHT_BLUE#%s#WHITE# es una de las cinco razas más jugadas",
    "#LIGHT_BLUE#%s#WHITE# is one of the top five played classes": "#LIGHT_BLUE#%s#WHITE# es una de las cinco clases más jugadas",
    "#CRIMSON#%s#WHITE# is one of the top ten killers": "#CRIMSON#%s#WHITE# es uno de los diez más letales",
    "#LIGHT_BLUE#%s#WHITE# is one of the top ten race/class combo": "#LIGHT_BLUE#%s#WHITE# es una de las diez combinaciones raza/clase más populares",
    "There are currently %d people playing online": "Hay %d personas jugando online",
    "The character's vault has registered a total of #RED#%d#WHITE# character's deaths": "La bóveda de personajes ha registrado un total de #RED#%d#WHITE# muertes",
    "The character's vault has registered a total of #LIGHT_BLUE#%d#WHITE# winners for the current version": "La bóveda ha registrado un total de #LIGHT_BLUE#%d#WHITE# ganadores en esta versión",
    "The latest donator is #LIGHT_GREEN#%s#WHITE#. Many thanks to all donators, you are keeping this game alive!": "El último donante es #LIGHT_GREEN#%s#WHITE#. Gracias a todos los donantes, ¡mantenéis este juego vivo!",
    "File: %s": "Archivo: %s",
    "Testing arg one %d and two %d": "Probando arg uno %d y dos %d",
    "%s (level %d)": "%s (nivel %d)",
    "Level %d": "Nivel %d",
    "Talent %s (level %d)": "Talento %s (nivel %d)",
    "Talent %s": "Talento %s",
    "Character Creation: %s": "Creación de personaje: %s",
    "%s (%d)#WHITE#; distance [%s]": "%s (%d)#WHITE#; distancia [%s]",
    # === Logs ===
    "#ORCHID#__[%d]%s improved talented AI picked talent[att:%d, turn %s]: %s": "#ORCHID#__[%d]%s IA mejorada eligió talento[ataq:%d, turno %s]: %s",
    "#SLATE#__%s[%d] improved talented AI No talents available [att:%d, turn %s]": "#SLATE#__%s[%d] IA mejorada sin talentos disponibles [ataq:%d, turno %s]",
    "#YELLOW#Error report sent, thank you.": "#YELLOW#Informe de error enviado, gracias.",
    "#LIGHT_RED#Keyboard input temporarily disabled.": "#LIGHT_RED#Entrada de teclado desactivada temporalmente.",
    "#LIGHT_RED#Mouse input temporarily disabled.": "#LIGHT_RED#Entrada de ratón desactivada temporalmente.",
    "#LIGHT_RED#Online profile disabled(switching to offline profile) due to %s.": "#LIGHT_RED#Perfil online desactivado(cambiando a offline) por %s.",
    "#YELLOW#Connection to online server established.": "#YELLOW#Conexión al servidor establecida.",
    "#YELLOW#Connection to online server lost, trying to reconnect.": "#YELLOW#Conexión al servidor perdida, reconectando.",
    # === Vistas de criaturas ===
    "#GREEN#%s#WHITE# appears to be neutral": "#GREEN#%s#WHITE# parece neutral",
    "#GREEN#%s#WHITE# appears to be friendly": "#GREEN#%s#WHITE# parece amistoso",
    "#LIGHT_RED#%s#WHITE# appears to be hostile": "#LIGHT_RED#%s#WHITE# parece hostil",
    "#YELLOW#%s#WHITE# appears to be a bit paranoid": "#YELLOW#%s#WHITE# parece un poco paranoico",
    # === LogSeen ===
    "#{bold}#%s killed %s!#{normal}#": "#{bold}#%s mató a %s!#{normal}#",
    "%s uses %s.": "%s usa %s.",
    "%s activates %s.": "%s activa %s.",
    "%s deactivates %s.": "%s desactiva %s.",
    "%s hits %s.": "%s golpea a %s.",
    "%s hits %s for %d damage.": "%s golpea a %s por %d de daño.",
    "%s casts %s.": "%s lanza %s.",
    "%s fires %s at %s.": "%s dispara %s a %s.",
    "%s performs a critical strike!": "¡%s realiza un golpe crítico!",
    "%s is knocked back!": "¡%s es derribado!",
    "%s is stunned!": "¡%s está aturdido!",
    "%s is frozen!": "¡%s está congelado!",
    "%s is on fire!": "¡%s está en llamas!",
    "%s is poisoned!": "¡%s está envenenado!",
    "%s is dazed!": "¡%s está atontado!",
    "%s is blinded!": "¡%s está cegado!",
    "%s is silenced!": "¡%s está silenciado!",
    "%s is confused!": "¡%s está confundido!",
    "%s is slowed!": "¡%s está ralentizado!",
    "%s is pinned!": "¡%s está inmovilizado!",
    "%s is disarmed!": "¡%s está desarmado!",
    "%s is debilitated!": "¡%s está debilitado!",
    "%s resists!": "¡%s resiste!",
    "%s is immune.": "%s es inmune.",
    "%s has died.": "%s ha muerto.",
    "%s has been slain.": "%s ha sido aniquilado.",
    "%s levels up!": "¡%s sube de nivel!",
    "%s teleports.": "%s se teletransporta.",
    "%s appears.": "%s aparece.",
    "%s disappears.": "%s desaparece.",
    "%s enters the level.": "%s entra al nivel.",
    "Missing!": "¡Falta!",
    "Unknown!": "¡Desconocido!",
    "active": "activo",
    "completed": "completado",
    "done": "hecho",
    "failed": "fallido",
    # === Guardado/Carga ===
    "Saving world": "Guardando mundo",
    "Please wait while saving the world...": "Espera mientras se guarda el mundo...",
    "Saving game": "Guardando partida",
    "Please wait while saving the game...": "Espera mientras se guarda la partida...",
    "Saving zone": "Guardando zona",
    "Please wait while saving the zone...": "Espera mientras se guarda la zona...",
    "Saving level": "Guardando nivel",
    "Please wait while saving the level...": "Espera mientras se guarda el nivel...",
    "Saving entity": "Guardando entidad",
    "Please wait while saving the entity...": "Espera mientras se guarda la entidad...",
    "Loading world": "Cargando mundo",
    "Please wait while loading the world...": "Espera mientras se carga el mundo...",
    "Loading game": "Cargando partida",
    "Please wait while loading the game...": "Espera mientras se carga la partida...",
    "Loading zone": "Cargando zona",
    "Please wait while loading the zone...": "Espera mientras se carga la zona...",
    "Loading level": "Cargando nivel",
    "Please wait while loading the level...": "Espera mientras se carga el nivel...",
    "Loading entity": "Cargando entidad",
    "Please wait while loading the entity...": "Espera mientras se carga la entidad...",
    "Saving done.": "Guardado completado.",
    "Saving...": "Guardando...",
    "Please wait while saving...": "Espera mientras se guarda...",
    "Generating level": "Generando nivel",
    "Please wait while generating the level... ": "Espera mientras se genera el nivel... ",
    "Please wait while loading the level... ": "Espera mientras se carga el nivel... ",
    # === Tienda ===
    "Store: %s": "Tienda: %s",
    "Buy": "Comprar",
    "Buy %d %s": "Comprar %d %s",
    "Sell": "Vender",
    "Sell %d %s": "Vender %d %s",
    "Cost: %d": "Coste: %d",
    "You have: %d": "Tienes: %d",
    "Insufficient gold": "Oro insuficiente",
    "You do not have enough gold.": "No tienes suficiente oro.",
    # === Trampas ===
    "%s fails to disarm a trap (%s).": "%s falla al desarmar una trampa (%s).",
    "%s disarms a trap (%s).": "%s desarma una trampa (%s).",
    "%s triggers a trap (%s)!": "¡%s activa una trampa (%s)!",
    # === Chat ===
    "#{italic}#Joined channel#{normal}#": "#{italic}#Canal unido#{normal}#",
    "#{italic}#Left channel#{normal}#": "#{italic}#Canal abandonado#{normal}#",
    "#{italic}##FIREBRICK#has joined the channel#{normal}#": "#{italic}##FIREBRICK#se ha unido al canal#{normal}#",
    "#{italic}##FIREBRICK#has left the channel#{normal}#": "#{italic}##FIREBRICK#ha abandonado el canal#{normal}#",
    "#CRIMSON#You are not subscribed to any channel, you can change that in the game options.#LAST#": "#CRIMSON#No estás suscrito a ningún canal, puedes cambiarlo en opciones.#LAST#",
    "Ignoring all new messages from %s.": "Ignorando todos los mensajes nuevos de %s.",
    "Thank you!": "¡Gracias!",
    "Requesting...": "Solicitando...",
    "Requesting user info...": "Solicitando información de usuario...",
    "Error": "Error",
    "The server does not know about this player.": "El servidor no conoce a este jugador.",
    # === Opciones de audio ===
    "Audio Options": "Opciones de audio",
    "Enable audio": "Activar audio",
    "Music: ": "Música: ",
    "Sound: ": "Sonido: ",
    "Effects: ": "Efectos: ",
    "Ambient: ": "Ambiente: ",
    "Volume: ": "Volumen: ",
    # === Opciones de video ===
    "Display Mode": "Modo de pantalla",
    "VSync": "VSync",
    "Texture Quality": "Calidad de texturas",
    "Shadow Quality": "Calidad de sombras",
    "Shader Quality": "Calidad de shaders",
    "Post Processing": "Postprocesado",
    "Low": "Bajo",
    "Medium": "Medio",
    "High": "Alto",
    "Ultra": "Ultra",
    # === Opciones de juego ===
    "Mouse Options": "Opciones de ratón",
    "Keyboard Options": "Opciones de teclado",
    "Tooltip Options": "Opciones de tooltips",
    "Chat Options": "Opciones de chat",
    "UI Options": "Opciones de interfaz",
    "Accessibility Options": "Opciones de accesibilidad",
    "Misc Options": "Opciones varias",
    # === Estados de teclas ===
    "You can not use this talent while silenced.": "No puedes usar este talento mientras estés silenciado.",
    "You can not use this talent while blinded.": "No puedes usar este talento mientras estés cegado.",
    "You can not use this talent while confused.": "No puedes usar este talento mientras estés confundido.",
    "You can not use this talent while stunned.": "No puedes usar este talento mientras estés aturdido.",
    # === entity name ===
    "mankind": "humanidad",
    # === Errores varios ===
    "__[%d]%s#ORANGE# ACTION FAILED:  %s, %s": "__[%d]%s#ORANGE# ACCIÓN FALLIDA: %s, %s",
}


def translate_engine_final():
    """Traduce todas las cadenas restantes de engine.lua."""
    with open(ENGINE_FILE, "r", encoding="utf-8") as f:
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
            current_trans = m.group(3)
            type_ = m.group(4)

            if original != current_trans:
                new_lines.append(line)
                continue

            if original in DICT:
                translation = DICT[original]
                safe_trans = translation.replace('"', '\\"')
                new_line = f'{indent}t("{original}", "{safe_trans}", "{type_}")'
                new_lines.append(new_line)
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    return count


def main():
    print("=" * 60)
    print("  TRADUCCIÓN FINAL DE ENGINE.LUA")
    print("=" * 60)

    if not ENGINE_FILE.exists():
        print(f"  ERROR: {ENGINE_FILE} no encontrado")
        return

    before = len(
        re.findall(r't\("[^"]*",\s*"[^"]*",\s*"[^"]*"\)', open(ENGINE_FILE).read())
    )
    count = translate_engine_final()

    # Contar cuántas quedan
    with open(ENGINE_FILE) as f:
        remaining = len(re.findall(r't\("[^"]*",\s*"[^"]*",\s*"[^"]*"\)', f.read()))

    print(f"\n  ✅ {count} cadenas traducidas")
    print(f"  📊 Antes: {before} | Después: {remaining} | Quedan: {remaining - count}")
    print()


if __name__ == "__main__":
    main()
