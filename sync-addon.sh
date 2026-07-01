#!/bin/bash
# sync-addon.sh - Sincroniza el addon de WSL a Windows

# Ruta correcta para ToME 1.7.6 (GOG en Windows)
WSL_DIR="$HOME/proyectos/tome4-es"
# Para Steam: /mnt/c/Program Files (x86)/Steam/steamapps/common/Tales of Maj'Eyal/game/addons
# Para GOG (instalación típica en C:\games\t-engine4-windows-1.7.6\)
WIN_ADDONS="/mnt/c/games/t-engine4-windows-1.7.6/game/addons"

if [ ! -d "$WIN_ADDONS" ]; then
    echo "❌ Error: Carpeta de addons no encontrada: $WIN_ADDONS"
    echo "   Verifica la ruta de instalación de ToME4 en Windows"
    exit 1
fi

echo "🗑️  Limpiando addon anterior (directorio + .teaa)..."
rm -rf "$WIN_ADDONS/tome-spanish" 2>/dev/null
rm -f "$WIN_ADDONS/tome-spanish.teaa"

echo "📦 Copiando addon (.teaa)..."
cp "$WSL_DIR/tome-spanish.teaa" "$WIN_ADDONS/tome-spanish.teaa"

if [ -f "$WIN_ADDONS/tome-spanish.teaa" ]; then
    echo "✅ Addon sincronizado correctamente"
    echo "   📦 $WIN_ADDONS/tome-spanish.teaa"
    echo ""
    echo "📋 Próximos pasos:"
    echo "   1. Ejecuta el juego en Windows"
    echo "   2. Ve a Addons y activa 'Spanish Translation for ToME'"
    echo "   3. Entra al juego para ver las traducciones"
else
    echo "❌ Error: No se pudo copiar el addon"
    exit 1
fi
