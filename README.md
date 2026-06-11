# ToME4-es 🇪🇸

Traducción al español de **Tales of Maj'Eyal (ToME4)**.

Addon oficial de traducción para el mejor roguelike de la actualidad.

## Estado actual

| Componente                                         | Cadenas    | Traducidas | %      |
| -------------------------------------------------- | ---------- | ---------- | ------ |
| Engine (UI, keybinds)                              | 637        | 117        | 18.4%  |
| Módulo principal (logros, objetos, talentos, lore) | 19.531     | 83         | 0.4%   |
| Boot (raza, clase, daños)                          | 266        | 0          | 0%     |
| Otros (addons, ejemplos)                           | 248        | 0          | 0%     |
| **TOTAL**                                          | **20.682** | **200**    | **1%** |

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

### 📋 Elige una sección para traducir

```
translations/es/mod-tome-split/
├── data/
│   ├── achievements/       🏆 Logros (~300 cadenas)
│   ├── birth/              👶 Razas y clases (~900 cadenas)
│   ├── chats/              💬 Diálogos con NPCs (~990 cadenas)
│   ├── general/objects/    🎯 Objetos y equipo (~3.700 cadenas)
│   ├── general/npcs/       👥 Nombres de criaturas (~830 cadenas)
│   ├── lore/               📜 Textos de lore (~290 cadenas)
│   ├── quests/             📋 Misiones (~490 cadenas)
│   ├── talents/            ⚔️ Talentos (~3.450 cadenas)
│   ├── timed_effects/      ⏳ Efectos temporales (~2.700 cadenas)
│   └── zones/              🗺️ Zonas y mapas (~2.050 cadenas)
```

Elige la que más te guste o la que mejor conozcas del juego.

### 🖊️ Cómo traducir

Cada archivo contiene llamadas `t()` con este formato:

```lua
-- Sin traducir (inglés repetido 2 veces):
t("The Arena", "The Arena", "achievement name")

-- Traducido (cambiar el 2º parámetro):
t("The Arena", "La Arena", "achievement name")
```

**Reglas:**

- ✅ Cambia solo el **segundo parámetro** (entre comillas)
- ✅ Mantén los códigos de color: `#GOLD#`, `#LIGHT_RED#`, etc.
- ✅ Mantén los placeholders: `%s`, `%d`, `%02d`, etc.
- ❌ No traduzcas nombres de personajes importantes ni términos técnicos

### 🔄 Flujo completo

```bash
# 1. Clonar el repo
git clone https://github.com/Ricard1974/tome4-es.git
cd tome4-es

# 2. Elegir y editar una sección
#    Por ejemplo, logros:
nano translations/es/mod-tome-split/data/achievements/arena.lua

# 3. Reconstruir el addon (auto-mergea + construye)
python3 scripts/build_addon.py

# 4. Ver progreso
python3 scripts/count_translations.py

# 5. Commit y push
git add -A
git commit -m "feat: traducidas XX cadenas de <sección>"
git push

# 6. Abrir Pull Request en GitHub
```

### 📦 Para desarrolladores

```bash
# Construir el addon
python3 scripts/build_addon.py

# Empaquetar como .teaa para distribución
python3 scripts/build_addon.py --package

# Dividir mod-tome.lua en secciones (si se regeneró)
python3 scripts/split_sections.py

# Mergear secciones de vuelta a mod-tome.lua
python3 scripts/merge_sections.py
```

## Estructura del proyecto

```
tome4-es/
├── tome-spanish/                  # Addon para ToME4
│   ├── init.lua                   # Metadatos del addon
│   ├── data/locales/              # Archivos de locale
│   │   ├── es.lua                 # Traducciones del módulo principal
│   │   └── engine/es.lua          # Traducciones del engine
│   └── README.md
├── translations/                  # Archivos fuente de traducción
│   ├── es/                        # Traducciones al español
│   │   ├── engine.lua             # Engine (UI, keybinds) — 637 cadenas
│   │   ├── mod-boot.lua           # Boot (razas, clases) — 265 cadenas
│   │   ├── mod-tome.lua           # Módulo principal (AUTOGENERADO)
│   │   ├── mod-tome-split/        # 📂 SECCIONES DIVIDIDAS (editar aquí)
│   │   │   ├── data/
│   │   │   │   ├── achievements/
│   │   │   │   ├── birth/
│   │   │   │   ├── talents/
│   │   │   │   ├── lore/
│   │   │   │   ├── quests/
│   │   │   │   ├── chats/
│   │   │   │   ├── general/
│   │   │   │   │   ├── objects/
│   │   │   │   │   ├── npcs/
│   │   │   │   │   └── ...
│   │   │   │   ├── zones/
│   │   │   │   └── ...
│   │   │   ├── mod/
│   │   │   │   ├── class/
│   │   │   │   └── dialogs/
│   │   │   └── ... (1.208 archivos en total)
│   │   ├── tome-addon-dev.lua      # Addon de desarrollo — 92 cadenas
│   │   └── tome-items-vault.lua    # Bóveda de objetos — 64 cadenas
│   └── extracted-text/             # Textos extraídos del juego (referencia)
├── scripts/                        # Scripts de utilidad
│   ├── count_translations.py       # Contador de progreso
│   ├── build_addon.py              # Constructor del addon (auto-mergea si procede)
│   ├── merge_sections.py           # Mergea archivos divididos → mod-tome.lua
│   ├── split_sections.py           # Divide mod-tome.lua en archivos individuales
│   ├── translate_safe.py           # Traducciones seguras del diccionario
│   └── extract_strings.py          # Extrae cadenas únicas para análisis
├── CONTRIBUTING.md                 # Guía para contribuir
└── README.md                       # Este archivo
```

### Flujo de trabajo recomendado

```
1️⃣  Editar archivos en translations/es/mod-tome-split/data/...
    (cada sección es un archivo independiente)

2️⃣  Mergear los cambios:
    python3 scripts/build_addon.py
    (esto auto-mergea y construye el addon)

3️⃣  Ver progreso:
    python3 scripts/count_translations.py

4️⃣  Probar en el juego:
    Copiar tome-spanish/ a game/addons/
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
