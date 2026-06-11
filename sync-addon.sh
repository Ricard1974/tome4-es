#!/bin/bash
# sync-addon.sh - Sincroniza el addon de WSL a Windows

WSL_ADDON="$HOME/proyectos/tome4-es/tome-spanish"
WIN_ADDONS="/mnt/c/Games/ToME4/game/addons"
WIN_ADDON="$WIN_ADDONS/tome-spanish"

if [ ! -d "$WSL_ADDON" ]; then
    echo "❌ Error: Addon no encontrado en $WSL_ADDON"
    exit 1
fi

if [ ! -d "$WIN_ADDONS" ]; then
    echo "❌ Error: Ruta de Windows no encontrada: $WIN_ADDONS"
    echo "   ¿Instalaste ToME4 en C:\\Games\\ToME4\\?"
    exit 1
fi

echo "🗑️  Limpiando addon anterior..."
rm -rf "$WIN_ADDON"

echo "📦 Copiando addon a Windows..."
cp -r "$WSL_ADDON" "$WIN_ADDON"

if [ -d "$WIN_ADDON" ]; then
    echo "✅ Addon sincronizado correctamente"
    echo "   Ubicación: $WIN_ADDON"
    echo ""
    echo "📋 Próximos pasos:"
    echo "   1. Ejecuta el juego en Windows"
    echo "   2. Ve a Addons y activa 'Spanish Translation for ToME'"
    echo "   3. Entra al juego para ver las traducciones"
else
    echo "❌ Error: No se pudo copiar el addon"
    exit 1
fi
