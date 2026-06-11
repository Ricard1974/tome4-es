#!/bin/bash
# build-and-sync.sh - Construye el addon y lo sincroniza con Windows

echo "🔨 Construyendo addon..."
cd ~/proyectos/tome4-es
python3 scripts/build_addon.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🔄 Sincronizando con Windows..."
    ./sync-addon.sh
else
    echo "❌ Error al construir el addon"
    exit 1
fi
