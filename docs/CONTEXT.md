# CONTEXT — ToME4 Spanish Translation (tome4-es)

> Archivo de contexto para agentes IA.
> Si retomas este proyecto tras un corte, empieza aquí.

---

## 1. ¿Qué es esto?

Traducción al español (de España) de **Tales of Maj'Eyal 1.7.6**.
Un addon que se instala en `game/addons/` del juego.

**Archivos resultantes:**
- `tome-spanish.teaa` — addon principal (1.6 MB, 22.657 cadenas)
- `boot-spanish.teaa` — menú principal (15 KB, incluido dentro del principal en el build)

**Repo**: https://github.com/Ricard1974/tome4-es  
**Licencia**: GPL v3+

---

## 2. Estructura del proyecto

```
tome4-es/
├── agent/                     # Pipeline de traducción con IA
│   ├── translator.py          #   Traductor (LibreTranslate + placeholders)
│   ├── translate_all.py       #   Orquestador de traducción
│   ├── translate_ui.py        #   Traductor de interfaz (engine, addons)
│   ├── processors.py          #   Procesadores post-traducción
│   └── terms.py               #   Diccionario EN→ES (1.454 líneas)
│
├── scripts/                   # Scripts de construcción y herramientas
│   ├── build_addon.py         #   [CLAVE] Construye el addon .teaa
│   ├── merge_sections.py      #   Mergea split sections → mod-tome.lua
│   ├── split_sections.py      #   Divide mod-tome.lua en secciones
│   ├── extract_strings.py     #   Extrae cadenas únicas a JSON
│   ├── count_translations.py  #   Cuenta estadísticas de traducción
│   ├── verify_translations.py #   Verificador de calidad
│   ├── fix_quality.py         #   Correcciones automáticas de calidad
│   ├── fix_format_specifiers.py#  Restaura %d/%s perdidos
│   ├── fix_spanglish.py       #   Corrige spanglish
│   └── translate_*.py         #   Scripts de traducción específicos (36 total)
│
├── translations/es/           # [CLAVE] Archivos fuente de traducción
│   ├── mod-tome.lua           #   ~21.486 entradas (el gordo)
│   ├── mod-tome-split/        #   Secciones divididas (merge manual)
│   ├── engine.lua             #   673 entradas (engine)
│   ├── mod-boot.lua           #   284 entradas (menú principal)
│   ├── tome-addon-dev.lua     #   107 entradas
│   ├── tome-items-vault.lua   #   69 entradas
│   ├── tome-remote-designer.lua#  4 entradas
│   ├── mod-example.lua        #   46 (no usados)
│   └── mod-example_realtime.lua#  45 (no usados)
│
├── tome-spanish/              # Addon construido (directorio)
│   ├── data/locales/es.lua    #   Locale principal mergado
│   ├── data/locales/engine/   #   Locale de engine
│   ├── hooks/load.lua         #   Hook que registra español
│   ├── init.lua               #   Metadatos del addon
│   └── superload/             #   (no usado — vacío)
│
├── boot-spanish/              # Addon del menú principal
│   ├── init.lua
│   └── data/locales/es.lua
│
├── docs/
│   ├── CONTEXT.md             # Este archivo
│   └── comparacion-locales.md # Comparativa con otros idiomas
│
├── sync-addon.sh              # Sincroniza WSL → Windows
└── build-and-sync.sh          # Build + sync en un paso
```

---

## 3. Pipeline de traducción (flujo completo)

```
1. agent/translator.py
   → Traduce cadenas vía LibreTranslate (localhost:5000)
   → Protege placeholders: §PH0§, §CL0§, §GV0§, §FS0§
   → Correcciones post: "usted"→"tú", términos de juego

2. agent/translate_all.py
   → Orquesta la traducción masiva
   → Usa diccionario EN→ES (terms.py) + reglas de patrones
   → Escribe en translations/es/mod-tome.lua

3. scripts/merge_sections.py
   → Mergea mod-tome-split/ → mod-tome.lua
   → Ordena secciones por categoría (birth, data, etc.)

4. scripts/build_addon.py
   → Lee translations/es/*.lua
   → Construye tome-spanish/ (directorio)
   → Extrae t() calls con formato: t("clave","valor","tipo")
   → Soporta TAMBIÉN t([["clave"]], [["valor"]], "tipo") (corchetes)
   → Con --package: genera tome-spanish.teaa (zip)
   → Incluye boot-spanish.teaa dentro del .teaa

5. scripts/fix_quality.py
   → Correcciones post-build:
     - Tags de color rotas (#LIGHT GREEN# → #LIGHT_GREEN#)
     - Variables #Source#/#Target# faltantes
     - Espacios dobles alrededor de placeholders
     - Palabras duplicadas
     - Términos spanglish
```

---

## 4. Formato de las traducciones

Cada entrada en los archivos .lua sigue el formato de Translation Toolbox:

```lua
--[[ Sección: data/general/nodes/forest.lua ]]
t("original", "traducción", "tipo")
```

**Tipos comunes:** `"description"`, `"name"`, `"text"`, `"dialog"`, `"lore"`, `"chat"`

**Strings multilínea** (descripciones de talentos):
```lua
t("original line 1\n\toriginal line 2", "traducción línea 1\n\ttraducción línea 2", "description")
```

**Corchetes largos** (minoría, ~54 entradas):
```lua
t([["clave"]], [["valor"]], "tipo")
```

---

## 5. Estado actual

| Métrica | Valor |
|---------|-------|
| Total `t()` calls | **22.647** |
| `tformat` (con formato) | 2.685 |
| `tformat` con `\n` (talentos) | **1.293** (🔥 únicos) |
| `_t` tag | 10.034 |
| Engine | 673 entradas |
| Tamaño locale | 3.173 KB |
| Sin traducir (real) | ~849 (nombres propios, IDs internos) |
| Spanglish detectado | 0 (corregido) |
| `#####` corruptas | 0 |

**Calidad**: ~3.600 correcciones automáticas aplicadas. Ningún otro idioma tiene
descripciones de talentos traducidas (el extractor oficial no las captura).

---

## 6. Logros técnicos clave

1. **Descripciones de talentos en español**: Ningún otro idioma (chino, japonés,
   coreano, portugués) las tiene. El extractor oficial `Translation Toolbox` no
   captura strings dentro de `info(self, t)` en `data/talents/*.lua`.

2. **Escapes Lua corregidos**: Las descripciones multilínea usan `\n\t\t` real.
   El build script tiene `unescape_lua()` que convierte `\\n` → newline real.

3. **Build script mejorado**: Ahora extrae `t([[clave]], [[valor]], "tipo")`
   además de `t("clave", "valor", "tipo")`. Antes perdía ~54 entradas.

4. **Protección de placeholders v2**: LibreTranslate no modifica `%d`, `%s`,
   `#LIGHT_GREEN#`, `#Source#`, etc. Único locale que lo implementa.

5. **Escaneo de código fuente**: Se escaneó `tome-1.7.6.team` (1.782 .lua)
   buscando `_()` sin entrada `t()`. Se añadieron 15 strings faltantes.

6. **Traducción de interfaz**: engine.lua (673), mod-boot.lua (284),
   addon-dev (107), items-vault (69), remote-designer (4) — todos traducidos.

---

## 7. Dependencias técnicas

| Componente | Propósito |
|------------|-----------|
| **LibreTranslate** (Docker) | API de traducción en localhost:5000 |
| **Python 3.10+** | Todo el pipeline |
| **setuptools** | Build system (pyproject.toml) |
| **ruff** | Linter (dev) |
| **Git** | Control de versiones |
| **WSL** | Entorno de desarrollo (Windows + Linux) |
| **ToME4 1.7.6 GOG** | Juego destino en C:\games\t-engine4-windows-1.7.6\ |
| **Translation Toolbox** | Extracción oficial de cadenas (solo referencia) |

---

## 8. Comandos frecuentes

```bash
# Construir addon (directorio)
python3 scripts/build_addon.py

# Construir y empaquetar .teaa
python3 scripts/build_addon.py --package

# Mergear secciones divididas
python3 scripts/merge_sections.py

# Verificar calidad
python3 scripts/verify_translations.py

# Verificar calidad (solo resumen)
python3 scripts/verify_translations.py --summary

# Contar estadísticas
python3 scripts/count_translations.py

# Sincronizar a Windows
./sync-addon.sh

# Build + sync
./build-and-sync.sh
```

---

## 9. Decisiones de arquitectura (ADR implícitas)

1. **Formato `"..."` con escapes, no `[[ ]]`** — El pipeline Python produce escapes
   `\n\t`. Los demás idiomas usan `[[ ]]`. No hay diferencia funcional.

2. **Hook manual `loadLocale`** — El addon llama a `loadLocale` y `setLocale`
   en el hook `ToME:load`. Los idiomas oficiales (integrados en .team) no
   necesitan esto.

3. **Sin superloads** — A diferencia del portugués (que tiene superloads
   de 79 KB para CharacterSheet), nosotros solo usamos hooks ligeros.

4. **boot-spanish incluido en el .teaa principal** — El build empaqueta
   `boot-spanish.teaa` dentro de `tome-spanish.teaa` para instalación única.

5. **Español de España** — Nada de modismos latinoamericanos ni argentinos.

---

## 10. Problemas conocidos / limitaciones

1. **Translation Toolbox no captura talentos** — El extractor oficial no puede
   extraer strings de `info(self, t)` en `data/talents/*.lua`. No hay solución
   conocida; nosotros los traducimos manualmente.

2. **LibreTranslate modifica placeholders** — A pesar de la protección v2,
   ocasionalmente aparecen espacios dobles alrededor de `%s`/`%d`. Se corrigen
   automáticamente en post-proceso.

3. **Engine locale separado** — El engine va en `data/locales/engine/es.lua`.
   Los idiomas oficiales lo tienen integrado en su archivo único. Esto es
   porque el engine no tiene `t()` entries en su código; usa `_()` directo.

4. **Split sections** — El directorio `mod-tome-split/` está actualmente vacío
   (todo mergeado). Si se divide de nuevo, ejecutar `scripts/split_sections.py`

5. **Addon externo:** `tome-remote-designer` no se ha probado en juego (solo
   4 entradas traducidas). Puede que falten strings no capturados.

---

## 11. Skills sugeridos para el agente

Si retomas este proyecto, carga estos skills:

- `handoff` — Para compactar sesiones largas entre agentes
- `python-testing-patterns` — Para pytest sobre los scripts de build
- `context-compression` — Para resúmenes intermedios

---

## 12. Historial de commits recientes (resumen)

| Commit | Descripción |
|--------|-------------|
| `8919199` | Depuración completa de errores en traducciones |
| `2bc292c` | Traducidas 96 cadenas de interfaz + 27 correcciones manuales |
| `9fab2cd` | Licencia GPL v2+ |
| `69d6efb` | Fix escapes `\n\t` en descripciones de talentos |
| `d5295e2` | Traducción masiva de talentos (~1.960) + comparativa |
| `6baba3c` | 67 format specifiers corregidos |
| `1520f32` | Superload y hooks protegidos contra crashes |
| `3283121` | 186 `%%` reparados en mod-tome.lua |
| `7c12e7f` | 2.247 placeholders `%s`/`%d` reparados |
| `97f7b24` | Traducción completa 91.8% (18.950/20.641) |

---

*Última actualización: julio 2026*
*Agente: build (DeepSeek V4 Flash)*
