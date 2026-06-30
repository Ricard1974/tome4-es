------------------------------------------------
section "tome-addon-dev/init.lua"


-- new text
--[==[
t("ToME Addon's Development Tools", "Herramientas de Desarrollo de Addons de ToME", "init.lua long_name")
t("Provides tools to develop and publish addons.", "Proporciona herramientas para desarrollar y publicar addons.", "init.lua description")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/ArrangeText.lua"


-- new text
--[==[
t([[[ERROR] format string error near '%s' of string %s
]], [[[ERROR] error de formato cerca de '%s' de la cadena %s
]], "tformat")
t([[[WARNING]Mismatched tformat string:
        Source: %s %s
        Target: %s %s (args=%s)
]], [[[AVISO]Cadena tformat no coincide:
        Origen: %s %s
        Destino: %s %s (args=%s)
]], "log")
t([[[WARNING]Mismatched translation for %s(%s): 
Last occurance: %s (from section %s)
Current occurance: %s (from section %s)
]], [[[AVISO]Traduccion no coincide para %s(%s): 
Ultima aparicion: %s (seccion %s)
Aparicion actual: %s (seccion %s)
]], "log")
t("Success", "Exito", "_t")
t([[Translation text checked.
Logs written to %s]], [[Texto de traduccion verificado.
Logs escritos en %s]], "tformat")
t("\
-- new text\
", "\
-- texto nuevo\
", "_t")
t("\
-- untranslated text\
", "\
-- texto sin traducir\
", "_t")
t("\
-- old translated text\
", "\
-- texto antiguo traducido\
", "_t")
t([[Translation text rearranged.
Logs written to %s]], [[Texto de traduccion reorganizado.
Logs escritos en %s]], "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/Extractor.lua"


-- new text
--[==[
t("Luafish parse error on file %s: %s", "Error de analisis Luafish en archivo %s: %s", "log")
t("error reading file %s", "error al leer archivo %s", "log")
t("Error writing file %s", "Error al escribir archivo %s", "log")
t("MD5 matched for part %s, skipped.", "MD5 coincide para parte %s, omitida.", "log")
t("Extracting text", "Extrayendo texto", "_t")
t("Processing source code of %s", "Procesando codigo fuente de %s", "tformat")
t("Success", "Exito", "_t")
t("Translation text extracted.", "Texto de traduccion extraido.", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/FSHelper.lua"


-- new text
--[==[
t("Error %s", "Error: %s", "log")
t("Calculating MD5", "Calculando MD5", "_t")
t("Calculating MD5 for %s", "Calculando MD5 para %s", "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/AddonDeveloper.lua"


-- new text
--[==[
t("Addon Developer", "Desarrollador de Addons", "_t")
t([[- Your profile has been enabled for addon uploading, you can go to #{italic}##LIGHT_BLUE#https://te4.org/addons/tome#LAST##{normal}# and upload your addon.
]], [[- Tu perfil ha sido habilitado para subir addons, puedes ir a #{italic}##LIGHT_BLUE#https://te4.org/addons/tome#LAST##{normal}# y subir tu addon.
]], "_t")
t("Archive for %s", "Archivo para %s", "tformat")
t([[Addon archive created:
- Addon file: #LIGHT_GREEN#%s#LAST# in folder #{bold}#%s#{normal}#
- Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard)
%s
]], [[Archivo de addon creado:
- Fichero del addon: #LIGHT_GREEN#%s#LAST# en carpeta #{bold}#%s#{normal}#
- MD5 del addon: #LIGHT_BLUE#%s#LAST# (copiado al portapapeles)
%s
]], "_t")
t("Registering new addon", "Registrando nuevo addon", "_t")
t("Addon init.lua must contain a tags table, i.e: tags={'foo', 'bar'}", "El init.lua del addon debe contener una tabla tags, ej: tags={'foo', 'bar'}", "_t")
t("Addon init.lua must contain a description field", "El init.lua del addon debe contener un campo description", "_t")
t("Addon: %s", "Addon: %s", "tformat")
t("Addon #LIGHT_GREEN#%s#LAST# registered. You may now upload a version for it.", "Addon #LIGHT_GREEN#%s#LAST# registrado. Ahora puedes subir una version.", "tformat")
t("Addon #LIGHT_RED#%s#LAST# not registered: %s", "Addon #LIGHT_RED#%s#LAST# no registrado: %s", "tformat")
t("unknown reason", "motivo desconocido", "_t")
t("Uploading addon", "Subiendo addon", "_t")
t("Addon #LIGHT_GREEN#%s#LAST# uploaded, players may now play with it!", "Addon #LIGHT_GREEN#%s#LAST# subido, los jugadores ya pueden usarlo!", "tformat")
t("Addon #LIGHT_RED#%s#LAST# not upload: %s", "Addon #LIGHT_RED#%s#LAST# no subido: %s", "tformat")
t("Connecting to server", "Conectando al servidor", "_t")
t("Steam Workshop: %s", "Steam Workshop: %s", "tformat")
t("Update error: %s", "Error de actualizacion: %s", "tformat")
t("unknown", "desconocido", "_t")
t("Uploading addon to Steam Workshop", "Subiendo addon a Steam Workshop", "_t")
t("There was an error uploading the addon.", "Hubo un error al subir el addon.", "_t")
t([[Addon succesfully uploaded to the Workshop.
You need to accept Steam Workshop Agreement in your Steam Client before the addon is visible to the community.]], [[Addon subido correctamente al Workshop.
Debes aceptar el Acuerdo de Steam Workshop en tu Cliente Steam antes de que el addon sea visible para la comunidad.]], "_t")
t("Go to Workshop", "Ir al Workshop", "_t")
t("Later", "Ahora no", "_t")
t("Addon succesfully uploaded to the Workshop.", "Addon subido correctamente al Workshop.", "_t")
t("Uploading addon preview to Steam Workshop", "Subiendo preview del addon a Steam Workshop", "_t")
t("There was an error uploading the addon preview.", "Hubo un error al subir la preview del addon.", "_t")
t("Addon update & preview succesfully uploaded to the Workshop.", "Actualizacion y preview del addon subidas correctamente al Workshop.", "_t")
t("Addon update succesfully uploaded to the Workshop.", "Actualizacion del addon subida correctamente al Workshop.", "_t")
t("Choose an addon for MD5", "Elige un addon para MD5", "_t")
t("MD5 for %s", "MD5 para %s", "tformat")
t([[Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard).
However you should'nt need that anymore, you can upload your addon directly from here.]], [[MD5 del addon: #LIGHT_BLUE#%s#LAST# (copiado al portapapeles).
Aunque ya no deberias necesitarlo, puedes subir tu addon directamente desde aqui.]], "tformat")
t("Choose an addon to archive", "Elige un addon para archivar", "_t")
t("Choose an addon to register", "Elige un addon para registrar", "_t")
t("Choose an addon to publish", "Elige un addon para publicar", "_t")
t("Name for this addon's release", "Nombre para esta version del addon", "_t")
t("Name", "Nombre", "_t")
t("Choose an addon to publish to Steam Workshop (needs to have been published to te4.org first)", "Elige un addon para publicar en Steam Workshop (debe haberse publicado en te4.org primero)", "_t")
t("Addon preview", "Preview del addon", "_t")
t([[Addons on Steam Workshop need a "preview" image for the listing.
The game has generated a default one, however it is best if you make a custom one and place it in the folder #LIGHT_GREEN#%s#LAST# named #LIGHT_BLUE#%s#LAST# (512x512 is a good size for it)
You can still upload now and place it later.]], [[Los addons en Steam Workshop necesitan una imagen de "preview" para el listado.
El juego ha generado una por defecto, pero es mejor si creas una personalizada y la colocas en la carpeta #LIGHT_GREEN#%s#LAST# con el nombre #LIGHT_BLUE#%s#LAST# (512x512 es un buen tamano)
Puedes subirla ahora y colocarla despues.]], "_t")
t("Upload now", "Subir ahora", "_t")
t("Wait", "Esperar", "_t")
t("Generate Addon's MD5", "Generar MD5 del Addon", "_t")
t("Register new Addon", "Registrar nuevo Addon", "_t")
t("Publish Addon to te4.org", "Publicar Addon en te4.org", "_t")
t("Publish Addon to Steam Workshop", "Publicar Addon en Steam Workshop", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ChooseTranslationParts.lua"


-- new text
--[==[
t("DEBUG -- Choose game parts", "DEBUG -- Elegir partes del juego", "_t")
t([[Choose game parts you want to translated.
Unchecked parts will not be scanned, rearranged or released.
Your configuration will be lost after closing the game.
]], [[Elige las partes del juego que quieres traducir.
Las partes no marcadas no se escanearan, reorganizaran ni publicaran.
Tu configuracion se perdera al cerrar el juego.
]], "_t")
t("Checked", "Marcado", "_t")
t("Short name", "Nombre corto", "_t")
t("Long Name", "Nombre largo", "_t")
t("Flip All", "Invertir todo", "_t")
t("Finish", "Finalizar", "_t")
t("enabled", "activado", "_t")
t("disabled", "desactivado", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/DebugMain.lua"


-- new text
--[==[
t("Addon Developer", "Desarrollador de Addons", "_t")
t("Translation Tool", "Herramienta de Traduccion", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ExampleAddonMaker.lua"


-- new text
--[==[
t("DEBUG -- Create Translation Addon", "DEBUG -- Crear Addon de Traduccion", "_t")
t("", "", "_t")
t("#LIGHT_GREEN#Locale Code:#LAST# ", "#LIGHT_GREEN#Codigo de idioma:#LAST# ", "_t")
t("#LIGHT_GREEN#Language Name:#LAST# ", "#LIGHT_GREEN#Nombre del idioma:#LAST# ", "_t")
t("Finish", "Finalizar", "_t")
t("Cancel", "Cancelar", "_t")
t("Failure", "Fallo", "_t")
t("Addon %s already exists", "El addon %s ya existe", "tformat")
t([[Fail when copying file to /addons/%s:
%s]], [[Fallo al copiar archivo a /addons/%s:
%s]], "tformat")
t([[Addon %s successfully created
Newly created addon is stored in %s]], [[Addon %s creado correctamente
El nuevo addon se ha guardado en %s]], "tformat")
t("Success", "Exito", "_t")
t("\
ToME4 is about to relaunch and change locale to %s, proceed?", "\
ToME4 se va a reiniciar y cambiar el idioma a %s, continuar?", "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ReleaseTranslation.lua"


-- new text
--[==[
t("Choose addon", "Elige addon", "_t")
t("Choose the addon you want to copy translation file to.", "Elige el addon al que copiar el archivo de traduccion.", "_t")
t("Failure", "Fallo", "_t")
t([[Fail when copying file to %s:
%s]], [[Fallo al copiar archivo a %s:
%s]], "tformat")
t("Success", "Exito", "_t")
t([[Translation text copied to %s
Logs written to %s]], [[Texto de traduccion copiado a %s
Logs escritos en %s]], "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TalentFinder.lua"


-- new text
--[==[
t("Search: ", "Buscar: ", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TranslationTool.lua"


-- new text
--[==[
t("Translation Toolkit", "Kit de Traduccion", "_t")
t("Change locale", "Cambiar idioma", "_t")
t("Enter locale code", "Introduce codigo de idioma", "_t")
t("Change working locale (current: %s)", "Cambiar idioma de trabajo (actual: %s)", "tformat")
t("Create translation addon", "Crear addon de traduccion", "_t")
t("Extract text index", "Extraer indice de texto", "_t")
t("Rearrange translation files", "Reorganizar archivos de traduccion", "_t")
t("Check translation files", "Verificar archivos de traduccion", "_t")
t("Release translation as addon", "Publicar traduccion como addon", "_t")
t("Choose which part to translate", "Elige que parte traducir", "_t")
--]==]


