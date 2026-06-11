# ToME4-es 🇪🇸

Traducción al español de **Tales of Maj'Eyal (ToME4)**.

Addon oficial de traducción para el mejor roguelike de la actualidad.

## Estado actual

| Componente                                         | Cadenas    | Traducidas | %      |
| -------------------------------------------------- | ---------- | ---------- | ------ |
| Engine (UI, keybinds)                              | 637        | 0          | 0%     |
| Módulo principal (logros, objetos, talentos, lore) | 19.521     | 0          | 0%     |
| Boot (raza, clase, daños)                          | 266        | 0          | 0%     |
| Otros (addons, ejemplos)                           | 258        | 0          | 0%     |
| **TOTAL**                                          | **20.682** | **0**      | **0%** |

📊 Estado actualizado: [Último reporte](https://github.com/Ricard1974/tome4-es/actions)

## Instalación

### Requisitos

- **ToME4 1.7.6** (descarga gratuita en [te4.org](https://te4.org/download))
- Addon de desarrollo (viene incluido con el juego: `tome-addon-dev.teaa`)

### Método 1: Desde Steam Workshop (recomendado)

**[Enlace a Steam Workshop — próximamente]**

### Método 2: Instalación manual

1. Descarga el addon desde [Releases](https://github.com/Ricard1974/tome4-es/releases)
2. Descomprime `tome-spanish` en la carpeta de addons del juego:
   - **Linux**: `~/.steam/steam/SteamApps/common/TalesMajEyal/game/addons/`
   - **Windows**: `C:\Program Files (x86)\Steam\SteamApps\common\TalesMajEyal\game\addons\`
   - **macOS**: `~/Library/Application Support/Steam/SteamApps/common/TalesMajEyal/game/addons/`
3. Activa el addon en el menú de addons del juego
4. Selecciona español en las opciones de idioma

### Método 3: Usando la Translation Toolbox (para traductores)

```bash
# 1. Clona el repositorio en la carpeta de addons
cd /ruta/al/juego/game/addons/
git clone https://github.com/Ricard1974/tome4-es.git

# 2. Activa el modo desarrollador en el juego (Options → Developer mode → Yes)
# 3. Dentro del juego: Ctrl+A → Translation Tool → Change working locale → es
# 4. Usa "Rearrange translation files" para actualizar
# 5. Usa "Release translation as addon" para empaquetar
```

## Cómo contribuir

### Para traductores

1. Edita los archivos en `translations/es/`
2. Cambia el segundo parámetro de `t()` por la traducción:

   ```lua
   -- Original (sin traducir)
   t("The Arena", "The Arena", "achievement name")

   -- Traducido
   t("The Arena", "La Arena", "achievement name")
   ```

3. Ejecuta el script de conteo para ver tu progreso:
   ```bash
   python3 scripts/count_translations.py
   ```
4. Abre un Pull Request con tus cambios

### Para desarrolladores

```bash
# Construir el addon desde las traducciones
python3 scripts/build_addon.py

# Empaquetar como .teaa para distribución
python3 scripts/build_addon.py --package
```

## Archivos de traducción

| Archivo                                | Contenido                                                       |
| -------------------------------------- | --------------------------------------------------------------- |
| `translations/es/mod-tome.lua`         | Módulo principal (logros, objetos, talentos, misiones, lore...) |
| `translations/es/engine.lua`           | Motor del juego (interfaz, teclas, UI)                          |
| `translations/es/mod-boot.lua`         | Arranque (razas, clases, tipos de daño)                         |
| `translations/es/tome-items-vault.lua` | Bóveda de objetos                                               |
| `translations/es/tome-addon-dev.lua`   | Herramientas de desarrollo                                      |

## Estructura del proyecto

```
tome4-es/
├── tome-spanish/              # Addon para ToME4
│   ├── init.lua               # Metadatos del addon
│   ├── data/locales/          # Archivos de locale
│   │   ├── es.lua             # Traducciones del módulo principal
│   │   └── engine/es.lua      # Traducciones del engine
│   └── README.md
├── translations/              # Archivos fuente de traducción
│   ├── es/                    # Traducciones al español
│   └── extracted-text/        # Textos extraídos del juego (referencia)
├── scripts/                   # Scripts de utilidad
│   ├── count_translations.py  # Contador de progreso
│   └── build_addon.py         # Constructor del addon
├── CONTRIBUTING.md            # Guía para contribuir
└── README.md                  # Este archivo
```

## Licencia

GNU General Public License v3.0 (igual que ToME4).

## Enlaces

- [Web oficial de ToME4](https://te4.org)
- [Wiki de traducción](https://te4.org/wiki/Translation)
- [Discord oficial](https://discord.gg/tales-of-majeyal) (canal #translation)
- [Addon de traducción al chino (referencia)](https://github.com/yutio888/tome-chn)

---

**ToME4** © 2009-2024 Nicolas Casalini "DarkGod" — [te4.org](https://te4.org)
