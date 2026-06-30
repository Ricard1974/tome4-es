# Comparativa de locales de ToME4

## Metodología

Archivos analizados:

| Idioma             | Código    | Origen                         | Archivo                    |
| ------------------ | --------- | ------------------------------ | -------------------------- |
| Chino simplificado | `zh_hans` | Integrado en `tome-1.7.6.team` | `data/locales/zh_hans.lua` |
| Chino tradicional  | `zh_hant` | Integrado en `tome-1.7.6.team` | `data/locales/zh_hant.lua` |
| Japonés            | `ja_JP`   | Integrado en `tome-1.7.6.team` | `data/locales/ja_JP.lua`   |
| Coreano            | `ko_KR`   | Integrado en `tome-1.7.6.team` | `data/locales/ko_KR.lua`   |
| Portugués BR       | `pt_BR`   | Addon externo (v119, jun 2026) | `data/locales/pt_BR.lua`   |
| Español            | `es`      | **Nuestro addon**              | `data/locales/es.lua`      |

El addon portugués incluye también traducciones de addons externos
(tome-items-vault, etc.) por eso su número de entradas es mayor.

## Tabla comparativa

| Métrica               |     Chino |   Japonés |   Coreano | Portugués |      **Español** |
| --------------------- | --------: | --------: | --------: | --------: | ---------------: |
| Total `t()` calls     |    21.868 |    22.409 |    21.898 |    30.628 |       **22.647** |
| `tformat` (total)     |     2.794 |     2.826 |     2.825 |     3.812 |        **2.685** |
| `tformat` con `\n`    |     **0** |     **0** |     **0** |     **0** |     **🔥 1.293** |
| `tformat` con `[[ ]]` |     1.149 |     1.170 |     1.162 |     1.594 |            **0** |
| `_t` tag (total)      |     9.910 |    10.358 |     9.902 |    14.373 |       **10.034** |
| `_t` con `[[ ]]`      |       929 |       782 |       962 |     1.268 |            **0** |
| `tooltip` tag         |         0 |         0 |         0 |         0 |            **0** |
| Tamaño archivo locale |  2.817 KB |  3.024 KB |  3.168 KB |  6.289 KB |    **3.173 KB** |
| Engine locale         | integrado | integrado | integrado |         — |  **673 entradas** |

## Características del addon

| Característica              |    Chino     | Japonés | Coreano | Portugués  | **Español**  |
| --------------------------- | :----------: | :-----: | :-----: | :--------: | :----------: |
| Descripciones de talentos   |      ❌      |   ❌    |   ❌    |     ❌     | **🔥 1.960** |
| En el `.team` del juego     |      ✅      |   ✅    |   ✅    |     ❌     |      ❌      |
| Hook manual `loadLocale`    |      ❌      |   ❌    |   ❌    |     ❌     |      ✅      |
| `superload` CharacterSheet  |      ❌      |   ❌    |   ❌    | ✅ (79 KB) |      ❌      |
| `superload` Inventory       |      ❌      |   ❌    |   ❌    |     ✅     |      ❌      |
| `superload` EquipDoll       |      ❌      |   ❌    |   ❌    |     ✅     |      ❌      |
| `overload` font package     |      ❌      |   ❌    |   ❌    |     ✅     |      ❌      |
| `overload` keybinds         |      ❌      |   ❌    |   ❌    |     ✅     |      ❌      |
| `boot` addon menú principal | ✅ (interno) |   ✅    |   ✅    |     ✅     |      ✅      |
| `tooltip` tag               |      ❌      |   ❌    |   ❌    |     ❌     |      ❌      |
| Protección de placeholders  |      ❌      |   ❌    |   ❌    |     ❌     |  **✅ v2**   |
 | Corrección de calidad       |      ❌      |   ❌    |   ❌    |     ❌     |  **✅ 3.499**|

## Observaciones clave

### 1. Descripciones de talentos: un caso único

**Ningún otro idioma traduce las descripciones multilínea de talentos.**
Los 1.960 `tformat` con `\n` que tenemos son completamente inéditos.

Los `tformat` con `[[ ]]` multilínea que tienen chino, japonés, coreano
y portugués corresponden a textos de otra naturaleza (diálogos de PNJ,
lore de objetos, mensajes de nivel, descripciones de logros), NO a
tooltips de talentos del juego (`data/talents/*.lua`).

### 2. Estilo de codificación

- **Chino, japonés, coreano, portugués**: usan `[[ ... ]]` (brackets
  largos de Lua) para strings multilínea.
- **Nosotros**: usamos `"..."` con escapes `\\n\\t\\t`. Ambos formatos
  producen la misma string en memoria, es solo una diferencia estilística.

### 3. Mecanismo de carga

- **Chino, japonés, coreano**: están dentro del `.team` del juego,
  se cargan automáticamente por `engine/Module.lua` línea 968.
  No necesitan hooks.
- **Portugués**: addon externo. **No llama a `loadLocale` ni `setLocale`**
  en su hook. Confía en que el sistema de montaje de addons y la carga
  automática de locales funciona. Usa `hooks/load.lua` y `hooks/load2.lua`
  (el segundo es idéntico, posiblemente para garantizar orden de carga).
- **Nosotros**: llamamos manualmente a `loadLocale` y `setLocale` en
  el hook `ToME:load`. Esto funciona pero difiere del enfoque de los demás.

### 4. Superloads

El portugués tiene un `superload/mod/dialogs/CharacterSheet.lua` de
**79 KB** que sobreescribe el diálogo de hoja de personaje completo,
con funciones de ordenación de talentos, formato UTF-8, y tooltips
personalizados. Esto es significativo porque indica que para conseguir
traducciones completas y correctas puede ser necesario modificar la
renderización, no solo el archivo de locale.

### 5. Traducción de interfaz de usuario

Se tradujeron todos los archivos de interfaz de addons externos:
- **Items Vault**: 67 cadenas (100%) — orbe, transferencias, errores, lista
- **Addon Developer**: 103 cadenas (97%) — subida, Steam Workshop, herramientas de traducción
- **Remote Designer**: 4 cadenas (100%) — activar/desactivar
- **Engine**: 673 cadenas (95%) — diálogos, opciones, mensajes del sistema
- **Mod-boot**: 284 cadenas (97%) — menú principal, addons, perfil

Tras escaneo del código fuente del juego, se añadieron **15 strings faltantes** (efectos de estado y mensajes de combate que el extractor i18n original no capturó). Quedan ~849 de `mod-tome.lua` que son nombres propios, IDs internos y formatos — casi todos iguales en ambos idiomas y sin necesidad de traducción.

### 7. Estilo `[[ ]]` vs `"..."`

Los demás idiomas usan `[[ ... ]]` (brackets largos de Lua) para strings
multilínea; nosotros usamos `"..."` con escapes `\\n\\t\\t` porque
nuestro pipeline de generación está en Python y `lua_escape()` produce
ese formato.

**No hay diferencia práctica**: ambas notaciones producen el mismo
string en memoria. Cambiar a `[[ ]]` sería solo cosmético y no aporta
ningún beneficio funcional. Pendiente como mejora estética menor.

### 6. Limitación del Translation Toolbox y del build script

La herramienta oficial de extracción de textos (`Translation Toolbox`)
**no extrae** los strings de dentro de funciones `info(self, t)` en
`data/talents/*.lua` porque el patrón utilizado es:

```lua
return ([[texto]]):tformat(args)
```

El extractor busca `t()` calls en archivos de datos, no dentro de
código Lua incrustado en funciones. Esta es la razón por la que ningún
idioma tiene descripciones de talentos traducidas.

Además, el build script original solo extraía `t("clave", "valor", "tipo")`
con comillas dobles, ignorando 54 entradas activas que usaban `t([[clave]], [[valor]], "tipo")`
con corchetes largos (principalmente en `engine.lua` y `mod-boot.lua`).
**El build script se actualizó** para extraer ambos formatos, añadiendo
esas 54 entradas al addon final.

### 8. Protección de placeholders y corrección de calidad

**Somos el único locale que implementa protección de placeholders**
frente a LibreTranslate. Los problemas encontrados y sus soluciones:

| Problema | Ocurrencias | Causa | Solución |
|----------|:-----------:|-------|----------|
| Tags de color rotas `#LIGHT GREEN#` | 540 | Regex `#[A-Za-z0-9]+#` no incluía `_` | Ampliado a `#[A-Z_]+#` + `#[a-f0-9]{6}#` |
| Variables `#Source#` perdidas | 83 | Confundidas con tags de color | Nuevo grupo `#[A-Z][a-z]+#` protegido como `§GV§` |
| `%s` con espacios dobles | 1.596 | LT añade espacios alrededor | `restore_placeholders()` limpia con regex |
| Traducciones erróneas (ej: "guerras" por "wares") | 31 | LT alucina con homófonos | Diccionario `SPECIFIC_FIXES` español→español |
| Palabras duplicadas | 10 | LT repite palabras | Función `fix_duplicated_words()` |
