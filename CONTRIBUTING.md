# Guía para contribuir a ToME4-es

## Primeros pasos

1. **Haz un fork** del repositorio
2. **Clona** tu fork:
   ```bash
   git clone https://github.com/TU_USUARIO/tome4-es.git
   cd tome4-es
   ```

## Cómo elegir una sección

Las traducciones están organizadas en archivos independientes dentro de `translations/es/mod-tome-split/`:

```
data/
├── achievements/       🏆 Logros (~300 cadenas)
├── birth/              👶 Razas y clases (~900 cadenas)
├── chats/              💬 Diálogos con NPCs (~990 cadenas)
├── general/objects/    🎯 Objetos y equipo (~3.700 cadenas)
├── general/npcs/       👥 Nombres de criaturas (~830 cadenas)
├── lore/               📜 Textos de lore (~290 cadenas)
├── quests/             📋 Misiones (~490 cadenas)
├── talents/            ⚔️ Talentos (~3.450 cadenas)
├── timed_effects/      ⏳ Efectos temporales (~2.700 cadenas)
└── zones/              🗺️ Zonas y mapas (~2.050 cadenas)
```

Elige la que más te guste del juego. Cada archivo es pequeño e independiente.

## Cómo traducir

### Formato

```lua
-- Sin traducir (inglés repetido 2 veces):
t("The Arena", "The Arena", "achievement name")

-- Traducido (cambiar el 2º parámetro):
t("The Arena", "La Arena", "achievement name")
```

### Reglas

1. ✅ Cambia solo el **segundo parámetro** (entre comillas)
2. ✅ Mantén los placeholders: `%s`, `%d`, `%02d`, etc.
3. ✅ Mantén los códigos de color: `#GOLD#`, `#LIGHT_RED#`, `#DARK_SEA_GREEN#`
4. ❌ No traduzcas nombres propios de personajes importantes ni términos técnicos

## Flujo de trabajo

```bash
# 1. Elige y edita una sección
#    Ejemplo: editar logros de la Arena
nano translations/es/mod-tome-split/data/achievements/arena.lua

# 2. Reconstruye el addon (auto-mergea + construye)
python3 scripts/build_addon.py

# 3. Verifica tu progreso
python3 scripts/count_translations.py

# 4. Prueba en el juego (opcional)
#    Copia tome-spanish/ a la carpeta de addons del juego

# 5. Commit y pull request
git add -A
git commit -m "feat: traducidas X cadenas de <sección>"
git push
```

### Si traduces engine.lua o mod-boot.lua

Estos archivos NO están divididos en secciones. Edítalos directamente:

```bash
nano translations/es/engine.lua      # UI y keybinds (637 cadenas)
nano translations/es/mod-boot.lua    # Razas, clases (266 cadenas)
```

### Después de sincronizar con la Translation Toolbox

Si el juego se actualiza y regeneras los archivos:

```bash
# 1. Copiar los nuevos archivos del juego
cp -r ~/.t-engine/4.0/tome/user-i18n/es/ translations/
cp -r ~/.t-engine/4.0/tome/user-i18n/extracted-text/ translations/

# 2. Re-dividir mod-tome.lua en secciones
python3 scripts/split_sections.py

# 3. Reconstruir addon
python3 scripts/build_addon.py
```

## Convenciones de traducción

### Términos comunes

| Inglés      | Español      | Notas |
| ----------- | ------------ | ----- |
| level       | nivel        |       |
| damage      | daño         |       |
| health      | salud / vida |       |
| mana        | maná         |       |
| stamina     | resistencia  |       |
| talent      | talento      |       |
| race        | raza         |       |
| class       | clase        |       |
| dungeon     | mazmorra     |       |
| quest       | misión       |       |
| achievement | logro        |       |
| player      | jugador      |       |
| enemy       | enemigo      |       |
| weapon      | arma         |       |
| armor       | armadura     |       |
| shield      | escudo       |       |

### Estilo

- **Tú** en lugar de **usted** (el juego usa trato directo)
- Mantén la longitud similar a la original para no romper la UI
- Usa un tono coherente con la fantasía épica del juego
- Para nombres de lugares y facciones, prioriza la ambientación sobre la traducción literal

## Reportar problemas

Si encuentras errores en la traducción o textos sin traducir:

1. Abre un [Issue](https://github.com/Ricard1974/tome4-es/issues)
2. Indica la versión del addon y del juego
3. Incluye captura de pantalla si es posible
4. Adjunta el archivo `te4_log.txt` si hay errores

## Recursos

- [Wiki de traducción de ToME4](https://te4.org/wiki/Translation)
- [Discord oficial](https://discord.gg/tales-of-majeyal) — canal #translation
- [Addon de traducción al chino](https://github.com/yutio888/tome-chn) — referencia de estructura

---

¡Gracias por ayudar a traducir ToME4 al español! 🎉
