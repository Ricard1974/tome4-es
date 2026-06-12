# Spanish Translation for Tales of Maj'Eyal (ToME4)

Traducción completa al español (de España) de **Tales of Maj'Eyal 1.7.6**.

## Características

- ✅ **~22.000 strings traducidos** — interfaz, talentos, objetos, diálogos, lore
- ✅ **Descripciones de talentos traducidas** — las traducciones más completas disponibles, ningún otro idioma las incluye
- ✅ **Menú principal en español** — incluye `boot-spanish.teaa`
- ✅ **Activación automática** — el español se selecciona desde Options → Language
- ✅ **Idioma: español de España** — nada de modismos latinoamericanos

## Notas técnicas

### Claves con saltos de línea (`[[...]]` en el código fuente)

Las descripciones de talentos en ToME4 se definen con bloques literales `[[...]]` que
contienen **newlines reales** (0x0A) y **tabs reales** (0x09). El pipeline de traducción
original escapaba estas secuencias como `\\n\\t\\t` (backslash literal + n/t), lo que
provocaba que `_t()` no encontrara la clave al buscar un newline real (0x0A) y encontrara
`\n` (0x5C+0x6E). El resultado era que las **descripciones se mostraban en inglés**.

**Solución**: Se añadió `unescape_lua()` en `scripts/build_addon.py` que convierte los
escapes Lua (`\n` → newline real, `\t` → tab real) **antes** de que `lua_escape()` los
vuelva a escapar correctamente. Ahora las ~1.960 descripciones de talentos se muestran
en español sin errores.

Este problema afectaba a todas las traducciones existentes (chino, japonés, coreano,
portugués) — ninguna incluye descripciones de talentos por la misma razón técnica.

## Archivos

| Archivo             | Descripción                                             |
| ------------------- | ------------------------------------------------------- |
| `tome-spanish.teaa` | Addon principal — traducción del juego                  |
| `boot-spanish.teaa` | Addon del menú principal (pantalla de título, opciones) |

Ambos archivos están disponibles en la página de [Releases](https://github.com/Ricard1974/tome4-es/releases).

## Instalación

1. Descarga **`tome-spanish.teaa`** y **`boot-spanish.teaa`** desde [Releases](https://github.com/Ricard1974/tome4-es/releases) o te4.org
2. Copia **ambos archivos** a la carpeta `game/addons/` de tu instalación de ToME4
3. Abre el juego
4. Ve a **Options → Language** y selecciona **"Español (Spanish)"**
5. ¡A jugar!

### Compilar desde el código fuente

```bash
git clone https://github.com/Ricard1974/tome4-es.git
cd tome4-es
python3 scripts/build_addon.py --package
```

Los archivos `tome-spanish.teaa` y `boot-spanish.teaa` se generarán en la raíz del proyecto.

## Compatibilidad

- **Versión del juego**: 1.7.6
- **Plataformas**: Windows, Linux, Mac
- **Modo offline**: sí
- **Perfil online**: sí

## Créditos

- **Traducción**: Ricard1974
- **Herramientas**: Translation Toolbox (te4.org), LibreTranslate
- **Repositorio**: https://github.com/Ricard1974/tome4-es

## Licencia

Este proyecto se distribuye bajo los mismos términos que Tales of Maj'Eyal
(GPL v3 o posterior). Ver el archivo `COPYING` para más detalles.
