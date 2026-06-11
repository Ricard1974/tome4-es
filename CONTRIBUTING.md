# Guía para contribuir a ToME4-es

## Primeros pasos

1. **Haz un fork** del repositorio
2. **Clona** tu fork:
   ```bash
   git clone https://github.com/TU_USUARIO/tome4-es.git
   cd tome4-es
   ```
3. **Sincroniza** con la Translation Toolbox (si tienes el juego):
   - Abre ToME4 con el addon de desarrollo activado
   - Ctrl+A → Translation Tool → Extract text index
   - Ctrl+A → Translation Tool → Rearrange translation files
   - Copia los archivos actualizados:
     ```bash
     cp -r ~/.t-engine/4.0/tome/user-i18n/es/ translations/
     cp -r ~/.t-engine/4.0/tome/user-i18n/extracted-text/ translations/
     ```

## Cómo traducir

### Formato

Los archivos de traducción usan el formato oficial de la Translation Toolbox:

```lua
t("texto original en inglés", "traducción al español", "tipo_de_cadena")
```

### Reglas

1. **Mantén los placeholders** como `%s`, `%d`, `%02d`, etc.
2. **Mantén los códigos de color** como `#GOLD#`, `#LIGHT_RED#`, `#DARK_SEA_GREEN#`
3. **Mantén las secuencias de escape** como `\n`, `\"`
4. **No traduzcas**:
   - Nombres propios de personajes (salvo que tengan traducción conocida)
   - Nombres de habilidades mecánicas (aunque se pueden adaptar)
   - Códigos y marcadores técnicos

### Ejemplo

```lua
-- Sin traducir
t("The Arena", "The Arena", "achievement name")
t("Unlocked Arena mode.", "Unlocked Arena mode.", "_t")

-- Traducido
t("The Arena", "La Arena", "achievement name")
t("Unlocked Arena mode.", "Modo Arena desbloqueado.", "_t")
```

### Archivos prioritarios

Recomendamos empezar por este orden:

1. **engine.lua** → Interfaz de usuario, teclas (637 cadenas)
2. **mod-boot.lua** → Razas, clases, tipos de daño (266 cadenas)
3. **mod-tome.lua** → Logros, objetos, talentos, misiones, lore (19.521 cadenas)
4. **tome-items-vault.lua** → Bóveda de objetos (64 cadenas)
5. **tome-addon-dev.lua** → Herramientas de desarrollo (92 cadenas)

## Flujo de trabajo

```bash
# 1. Traduce en el archivo correspondiente
# 2. Verifica tu progreso
python3 scripts/count_translations.py

# 3. Construye el addon
python3 scripts/build_addon.py

# 4. Prueba en el juego (opcional)
# Copia tome-spanish/ a la carpeta de addons del juego
# Activa el addon y comprueba que las traducciones funcionan

# 5. Haz commit y pull request
git add .
git commit -m "feat: traducidas X cadenas de <archivo>"
git push
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
