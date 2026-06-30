#!/usr/bin/env python3
"""
Última pasada: traduce todo lo que queda en engine.lua.
Lee las cadenas restantes y las traduce sistemáticamente.

Uso: python3 scripts/translate_engine_remaining.py
"""

import re
from pathlib import Path

TRANS_DIR = Path(__file__).parent.parent / "translations" / "es"
ENGINE_FILE = TRANS_DIR / "engine.lua"

# =============================================================================
# TRADUCCIONES MASIVAS
# =============================================================================
MASS_TRANSLATIONS = {
    # === Estado ===
    "???": "???",
    "No": "No",
    "Error": "Error",
    # === Canales de chat ===
    "Chat channels": "Canales de chat",
    "Global": "Global",
    "English": "Inglés",
    "Local": "Local",
    "Channel": "Canal",
    "Join Channel": "Unirse al canal",
    "Leave Channel": "Abandonar canal",
    "Create Channel": "Crear canal",
    "Channel Name": "Nombre del canal",
    "Channel Password": "Contraseña del canal",
    "Join": "Unirse",
    "Send": "Enviar",
    "Chat: %s": "Chat: %s",
    "You have joined channel %s.": "Te has unido al canal %s.",
    "You have left channel %s.": "Has abandonado el canal %s.",
    "You are now known as %s.": "Ahora te conocen como %s.",
    "You are now known as an unknown entity.": "Ahora eres una entidad desconocida.",
    "You have been kicked from channel %s.": "Has sido expulsado del canal %s.",
    "Channel %s does not exist.": "El canal %s no existe.",
    "Channel %s already exists.": "El canal %s ya existe.",
    "Wrong password for channel %s.": "Contraseña incorrecta para el canal %s.",
    "You are not a member of channel %s.": "No eres miembro del canal %s.",
    "Channel %s is full.": "El canal %s está lleno.",
    "You have been banned from channel %s.": "Has sido baneado del canal %s.",
    "You have been unbanned from channel %s.": "Has sido desbaneado del canal %s.",
    "User %s has been banned from channel %s.": "El usuario %s ha sido baneado del canal %s.",
    "User %s has been unbanned from channel %s.": "El usuario %s ha sido desbaneado del canal %s.",
    "User %s has been kicked from channel %s.": "El usuario %s ha sido expulsado del canal %s.",
    "You have been muted on channel %s.": "Has sido silenciado en el canal %s.",
    "You have been unmuted on channel %s.": "Has sido desilenciado en el canal %s.",
    "User %s has been muted on channel %s.": "El usuario %s ha sido silenciado en el canal %s.",
    "User %s has been unmuted on channel %s.": "El usuario %s ha sido desilenciado en el canal %s.",
    "You set the topic of channel %s to: %s": "Has establecido el tema del canal %s a: %s",
    "The topic of channel %s is: %s": "El tema del canal %s es: %s",
    "There is no topic set for channel %s.": "No hay tema establecido para el canal %s.",
    "Topic": "Tema",
    "Set Topic": "Establecer tema",
    "Members": "Miembros",
    "Mode": "Modo",
    "Operator": "Operador",
    "Voice": "Voz",
    "Ban": "Banear",
    "Unban": "Desbanear",
    "Kick": "Expulsar",
    "Mute": "Silenciar",
    "Unmute": "Desilenciar",
    "Whois": "Quién es",
    "Who is %s?": "¿Quién es %s?",
    "%s is %s": "%s es %s",
    "User %s is not online.": "El usuario %s no está online.",
    "User %s is online.": "El usuario %s está online.",
    "User %s is away.": "El usuario %s está ausente.",
    "User %s is idle.": "El usuario %s está inactivo.",
    # === Format strings ===
    "Really stop ignoring: %s": "¿Dejar de ignorar: %s?",
    "Continue? %s": "¿Continuar? %s",
    "Download: %s": "Descarga: %s",
    "Must be between %i and %i characters.": "Debe tener entre %i y %i caracteres.",
    "Press a key (escape to cancel, backspace to remove) for: %s": "Pulsa una tecla (escape=cancelar, retroceso=quitar) para: %s",
    "Key: %s": "Tecla: %s",
    "You can not assign that key.": "No puedes asignar esa tecla.",
    "This key is already used by: %s": "Esta tecla ya la usa: %s",
    "The following keybindings are missing: %s": "Faltan las siguientes teclas: %s",
    "Confirm": "Confirmar",
    "Are you sure?": "¿Estás seguro?",
    "This action can not be undone.": "Esta acción no se puede deshacer.",
    "All keys will be reset to defaults.": "Todas las teclas se restaurarán por defecto.",
    "Reset all keys": "Restaurar todas las teclas",
    # === Logs (vistos por el jugador) ===
    "%s picks up (%s.): %s%s.": "%s recoge (%s.): %s%s.",
    "%s has no room for: %s.": "%s no tiene sitio para: %s.",
    "There is nothing to pick up here.": "No hay nada que recoger aquí.",
    "There is nothing to drop.": "No hay nada que soltar.",
    "%s drops on the floor: %s.": "%s suelta en el suelo: %s.",
    "%s wears: %s.": "%s se equipa: %s.",
    "%s takes off: %s.": "%s se quita: %s.",
    "%s uses: %s.": "%s usa: %s.",
    "You have learned a new talent: %s!": "¡Has aprendido un nuevo talento: %s!",
    "You have levelled up!": "¡Has subido de nivel!",
    "You have died!": "¡Has muerto!",
    "You have been killed by %s.": "Has sido asesinado por %s.",
    "You are now level %d.": "Ahora eres nivel %d.",
    # === Logs (sistema) ===
    "File location copied to clipboard.": "Ubicación del archivo copiada al portapapeles.",
    "[CHEAT] teleport to %dx%d": "[TRAMPA] teletransporte a %dx%d",
    "%s starts...": "%s comienza...",
    "%s for %d turns (stop reason: %s).": "%s durante %d turnos (motivo de parada: %s).",
    "%s for %d turns.": "%s durante %d turnos.",
    # === LogPlayer ===
    "%s is still on cooldown for %d turns.": "%s sigue en enfriamiento por %d turnos.",
    "%s is still recharging.": "%s sigue recargándose.",
    "%s can not be used anymore.": "%s ya no se puede usar.",
    "You don't see how to get there...": "No ves cómo llegar allí...",
    # === Entity name ===
    "unknown": "desconocido",
    # === Misc adicionales ===
    "Nothing to do": "Nada que hacer",
    "Waiting...": "Esperando...",
    "Activating...": "Activando...",
    "Deactivating...": "Desactivando...",
    "Working...": "Trabajando...",
    "Cancelling...": "Cancelando...",
    "You can not go there.": "No puedes ir allí.",
    "You must have a target.": "Debes tener un objetivo.",
    "Invalid target.": "Objetivo inválido.",
    "Out of range.": "Fuera de alcance.",
    "You can not see your target.": "No puedes ver a tu objetivo.",
    "You can not see there.": "No puedes ver allí.",
    "There is nothing in that direction.": "No hay nada en esa dirección.",
    "There is a wall in the way.": "Hay un muro en medio.",
    "You can not move there.": "No puedes moverte allí.",
    "You can not go that way.": "No puedes ir por ahí.",
    # === Inventario y objetos ===
    "Inventory: %s": "Inventario: %s",
    "Equipment: %s": "Equipo: %s",
    "Object: %s": "Objeto: %s",
    "Use: %s": "Usar: %s",
    "Destroy: %s": "Destruir: %s",
    "Drop: %s": "Soltar: %s",
    "Examine: %s": "Examinar: %s",
    "Number of objects: %d": "Número de objetos: %d",
    "Total weight: %0.2f": "Peso total: %0.2f",
    "Carrying capacity: %0.2f": "Capacidad de carga: %0.2f",
    "You are overburdened!": "¡Estas sobrecargado!",
    "You can not carry any more.": "No puedes cargar más.",
}


def translate_all():
    """Aplica MASS_TRANSLATIONS a engine.lua."""
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

            if original in MASS_TRANSLATIONS:
                trans = MASS_TRANSLATIONS[original]
                safe = trans.replace('"', '\\"')
                new_lines.append(f'{indent}t("{original}", "{safe}", "{type_}")')
                count += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(ENGINE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    return count


def main():
    print("=" * 60)
    print("  ÚLTIMA PASADA — ENGINE.LUA")
    print("=" * 60)

    count = translate_all()
    print(f"\n  ✅ {count} cadenas traducidas")

    # Mostrar cuántas quedan
    with open(ENGINE_FILE) as f:
        content = f.read()
    len(re.findall(r't\("[^"]*",\s*"([^"]*)",', content))
    untranslated = 0
    for line in content.split("\n"):
        m = re.match(r't\("([^"]*)",\s*"([^"]*)",', line)
        if m and m.group(1) == m.group(2):
            untranslated += 1

    print(f"  📊 Quedan {untranslated} sin traducir")
    print()


if __name__ == "__main__":
    main()
