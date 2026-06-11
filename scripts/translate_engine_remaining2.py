#!/usr/bin/env python3
"""
Completa engine.lua con todas las cadenas de UI restantes.

Uso: python3 scripts/translate_engine_remaining2.py
"""

import re
from pathlib import Path

ENGINE = Path(__file__).parent.parent / "translations" / "es" / "engine.lua"

DICT = {
    "(progress will be saved)": "(el progreso se guardará)",
    "[spoilers]": "[spoilers]",
    "(*) Take all": "(*) Tomar todo",
    "- Talent category known": "- Categoría de talento conocida",
    "-- Unknown --": "-- Desconocido --",
    "???": "???",
    "Accept": "Aceptar",
    "Achievement": "Logro",
    "Addon installed!": "¡Addon instalado!",
    "All achieved": "Todo conseguido",
    "All data purged from the cloud.": "Todos los datos purgados de la nube.",
    "Are you sure you want to target yourself?": "¿Seguro que quieres apuntarte a ti mismo?",
    "Available": "Disponible",
    "Bind alternate key": "Asignar tecla alternativa",
    "Bind key": "Asignar tecla",
    "Cart": "Carrito",
    "Cart is empty!": "¡El carrito está vacío!",
    "Category": "Categoría",
    "Close All": "Cerrar todo",
    "Confirm addon install/update": "Confirmar instalación/actualización de addon",
    "Confirm module install/update": "Confirmar instalación/actualización de módulo",
    "Confirm purge?": "¿Confirmar purga?",
    "Connecting to Steam": "Conectando a Steam",
    "Connecting to server": "Conectando al servidor",
    "Copy URL": "Copiar URL",
    "Currently playing: ": "Jugando actualmente: ",
    "Display resolution.": "Resolución de pantalla.",
    "Download: ": "Descarga: ",
    "Enc.": "Enc.",
    "Enter a quantity.": "Introduce una cantidad.",
    "Filter:": "Filtro:",
    "General": "General",
    "Generate": "Generar",
    "Global": "Global",
    "Homepage": "Página web",
    "Hotkey Page 2": "Página de teclas 2",
    "Hotkey Page 3": "Página de teclas 3",
    "ID: ": "ID: ",
    "If you do not have any free hotkey pages you must first empty one": "Si no tienes páginas de teclas libres, vacía una primero",
    "Incompatible": "Incompatible",
    "Insert": "Insertar",
    "Install": "Instalar",
    "Installed": "Instalado",
    "Interface": "Interfaz",
    "Invalid": "Inválido",
    "Item": "Objeto",
    "Key": "Tecla",
    "Language": "Idioma",
    "Last login: ": "Último inicio: ",
    "Last login: Offline": "Último inicio: Offline",
    "Load order: ": "Orden de carga: ",
    "Loading": "Cargando",
    "Location: ": "Localización: ",
    "Log in": "Iniciar sesión",
    "Log out": "Cerrar sesión",
    "Login": "Inicio de sesión",
    "Logout": "Cerrar sesión",
    "Mail": "Correo",
    "Message of the Day": "Mensaje del día",
    "Module": "Módulo",
    "News": "Noticias",
    "Next": "Siguiente",
    "No hotkeys to assign": "No hay teclas que asignar",
    "No unassigned hotkeys available": "No hay teclas sin asignar disponibles",
    "Not available": "No disponible",
    "Off": "No",
    "Offline": "Offline",
    "Ok": "Aceptar",
    "On": "Sí",
    "Online": "Online",
    "Open": "Abrir",
    "Online license": "Licencia online",
    "Page": "Página",
    "Password": "Contraseña",
    "Play": "Jugar",
    "Player:": "Jugador:",
    "Please wait": "Espera por favor",
    "Previous": "Anterior",
    "Profile created": "Perfil creado",
    "Purge Cloud Saves": "Purgar guardado en la nube",
    "Quantity:": "Cantidad:",
    "Ready": "Listo",
    "Received": "Recibido",
    "Register": "Registrarse",
    "Reject": "Rechazar",
    "Remove": "Eliminar",
    "Required": "Requerido",
    "Save": "Guardar",
    "Saving": "Guardando",
    "Search games": "Buscar partidas",
    "Search:": "Buscar:",
    "Select user": "Seleccionar usuario",
    "Sent": "Enviado",
    "Server": "Servidor",
    "Show information": "Mostrar información",
    "Show passwords": "Mostrar contraseñas",
    "Size": "Tamaño",
    "Source": "Fuente",
    "Status: %s": "Estado: %s",
    "Switch to Page %d": "Cambiar a página %d",
    "Target:": "Objetivo:",
    "The addon was installed into the game folder; you may need to restart the game.": "El addon se instaló en la carpeta del juego; puede que necesites reiniciar.",
    "The module was installed into the game folder; you may need to restart the game.": "El módulo se instaló en la carpeta del juego; puede que necesites reiniciar.",
    "The password must be more than 5 characters long.": "La contraseña debe tener más de 5 caracteres.",
    "This will irreversibly delete all your information from the online system and disable all current keys and cloud functions!": "¡Esto borrará irreversiblemente tu información del sistema online y desactivará todas las claves y funciones en la nube!",
    "Total:": "Total:",
    "Total: %d": "Total: %d",
    "Uninstall": "Desinstalar",
    "Unit": "Unidad",
    "Unknown Achievement: %s": "Logro desconocido: %s",
    "Unknown": "Desconocido",
    "Up to date": "Actualizado",
    "Update All": "Actualizar todo",
    "Update": "Actualizar",
    "Updated": "Actualizado",
    "Uploading...": "Subiendo...",
    "Uploading: %d%%": "Subiendo: %d%%",
    "Username": "Usuario",
    "Version:": "Versión:",
    "View": "Ver",
    "Visit site": "Visitar sitio",
    "Warning!": "¡Aviso!",
    "Weight: %0.2f": "Peso: %0.2f",
    "Your purchase is being confirmed, please wait a few seconds.": "Tu compra se está confirmando, espera unos segundos.",
    "low": "bajo",
    "max": "máx",
    "min": "mín",
    "nothing": "nada",
    "off": "no",
    "old": "antiguo",
    "on": "sí",
    "standard": "estándar",
    "Buy": "Comprar",
    "Sell": "Vender",
    "Store": "Tienda",
    "You have: %d": "Tienes: %d",
    "Cost: %d": "Coste: %d",
    "Chat": "Chat",
}


def main():
    with open(ENGINE, "r", encoding="utf-8") as f:
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

    with open(ENGINE, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    print(f"✅ engine.lua: +{count} traducciones")


if __name__ == "__main__":
    main()
