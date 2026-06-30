------------------------------------------------
-- section "mod-boot/data/birth/descriptors.lua"


-- new text
t("base", "base", "birth descriptor name")
t("Destroyer", "Destructor", "birth descriptor name")
t("Acid-maniac", "Ácido-maníaco", "birth descriptor name")


------------------------------------------------
-- section "mod-boot/data/damage_types.lua"


-- new text
t("Kill!", "¡Matar!", "_t")


------------------------------------------------
-- section "mod-boot/data/general/grids/basic.lua"


-- new text
t("floor", "suelo", "entity type")
t("floor", "suelo", "entity subtype")
t("floor", "suelo", "entity name")
t("wall", "muro", "entity type")
t("wall", "muro", "entity name")
t("door", "puerta", "entity name")
t("open door", "puerta abierta", "entity name")


------------------------------------------------
-- section "mod-boot/data/general/grids/forest.lua"


-- new text
t("floor", "suelo", "entity type")
t("grass", "hierba", "entity subtype")
t("grass", "hierba", "entity name")
t("wall", "muro", "entity type")
t("tree", "árbol", "entity name")
t("flower", "flor", "entity name")


------------------------------------------------
-- section "mod-boot/data/general/grids/underground.lua"


-- new text
t("wall", "muro", "entity type")
t("underground", "subterráneo", "entity subtype")
t("crystals", "cristales", "entity name")
t("floor", "suelo", "entity type")
t("floor", "suelo", "entity name")


------------------------------------------------
-- section "mod-boot/data/general/grids/water.lua"


-- new text
t("floor", "suelo", "entity type")
t("water", "agua", "entity subtype")
t("deep water", "agua profunda", "entity name")


------------------------------------------------
-- section "mod-boot/data/general/npcs/canine.lua"


-- new text
t("animal", "animal", "entity type")
t("canine", "canino", "entity subtype")
t("wolf", "lobo", "entity name")
t("Lean, mean, and shaggy, it stares at you with hungry eyes.", "Magro, hirsuto y fiero, te mira con ojos hambrientos.", "_t")
t("white wolf", "lobo blanco", "entity name")
t("A large and muscled wolf from the northern wastes. Its breath is cold and icy and its fur coated in frost.", "Un lobo grande y musculoso de los paramos del norte. Su aliento es frio y helado y su pelaje cubierto de escarcha.", "_t")
t("warg", "huargo", "entity name")
t("It is a large wolf with eyes full of cunning.", "Es un lobo grande con ojos llenos de astucia.", "_t")
t("fox", "zorro", "entity name")
t("The quick brown fox jumps over the lazy dog.", "El rápido zorro marrón salta sobre el perro perezoso.", "_t")


------------------------------------------------
-- section "mod-boot/data/general/npcs/skeleton.lua"


-- new text
t("undead", "no-muerto", "entity type")
t("skeleton", "esqueleto", "entity subtype")
t("degenerated skeleton warrior", "guerrero esqueleto degenerado", "entity name")
t("skeleton warrior", "guerrero esqueleto", "entity name")
t("skeleton mage", "mago esqueleto", "entity name")
t("armoured skeleton warrior", "guerrero esqueleto acorazado", "entity name")


------------------------------------------------
-- section "mod-boot/data/general/npcs/troll.lua"


-- new text
t("giant", "gigante", "entity type")
t("troll", "trol", "entity subtype")
t("forest troll", "trol del bosque", "entity name")
t("Green-skinned and ugly, this massive humanoid glares at you, clenching wart-covered green fists.", "De piel verde y horrible, este enorme humanoide te mira fijamente, apretando sus punos verdes verrugosos.", "_t")
t("stone troll", "trol de piedra", "entity name")
t("A giant troll with scabrous black skin. With a shudder, you notice the belt of dwarf skulls around his massive waist.", "Un trol gigante de piel negra y escamosa. Con un escalofrio notas el cinturon de craneos enanos alrededor de su cintura.", "_t")
t("cave troll", "trol de cueva", "entity name")
t("This huge troll wields a massive spear and has a disturbingly intelligent look in its piggy eyes.", "Este enorme trol empuna una lanza masiva y tiene una mirada inquietantemente inteligente en sus ojillos.", "_t")
t("mountain troll", "trol de montaña", "entity name")
t("A large and athletic troll with an extremely tough and warty hide.", "Un trol grande y atlético de piel extremadamente dura y verrugosa.", "_t")
t("mountain troll thunderer", "trol montañés atronador", "entity name")


------------------------------------------------
-- section "mod-boot/data/talents.lua"


-- new text
t("misc", "varios", "talent category")
t("Kick", "Patada", "talent name")
t("Acid Spray", "Rociada ácida", "talent name")
t("Manathrust", "Empuje de maná", "talent name")
t("Flame", "Llama", "talent name")
t("Fireflash", "Destello ígneo", "talent name")
t("Lightning", "Relámpago", "talent name")
t("Sunshield", "Escudo solar", "talent name")
t("Flameshock", "Descarga ígnea", "talent name")


------------------------------------------------
-- section "mod-boot/data/timed_effects.lua"


-- new text
t("Burning from acid", "Quemadura por ácido", "_t")
t("#Target# is covered in acid!", "¡#Target# está cubierto de ácido!", "_t")
t("+Acid", "+Ácido", "_t")
t("#Target# is free from the acid.", "#Target# está libre del ácido.", "_t")
t("-Acid", "-Ácido", "_t")
t("Sunshield", "Escudo solar", "_t")


------------------------------------------------
-- section "mod-boot/data/zones/dungeon/zone.lua"


-- new text
t("Forest", "Bosque", "_t")


------------------------------------------------
-- section "mod-boot/mod/class/Game.lua"


-- new text
t("Welcome to T-Engine and the Tales of Maj'Eyal", "Bienvenido a T-Engine y Tales of Maj'Eyal", "_t")
t([[#GOLD#"Tales of Maj'Eyal"#WHITE# is the main game, you can also install more addons or modules by going to https://te4.org/

When inside a module remember you can press Escape to bring up a menu to change keybindings, resolution and other module specific options.

Remember that in most roguelikes death is usually permanent so be careful!

Now go and have some fun!]], [[#GOLD#"Tales of Maj'Eyal"#WHITE# is the main game, you can also install more addons or modules by going to https://te4.org/

When inside a module remember you can press Escape to bring up a menu to change keybindings, resolution and other module specific options.

Remember that in most roguelikes death is usually permanent so be careful!

Now go and have some fun!]], "_t")
t("Upgrade to 1.0.5", "Actualizar a 1.0.5", "_t")
t([[The way the engine manages saving has been reworked for v1.0.5.

The background saves should no longer lag horribly and as such it is highly recommended that you use the option. The upgrade turned it on for you.

For the same reason the save per level option should not be used unless you have severe memory problems. The upgrade turned it off for you.
]], [[The way the engine manages saving has been reworked for v1.0.5.

The background saves should no longer lag horribly and as such it is highly recommended that you use the option. The upgrade turned it on for you.

For the same reason the save per level option should not be used unless you have severe memory problems. The upgrade turned it off for you.
]], "_t")
t("Safe Mode", "Modo seguro", "_t")
t([[Oops! Either you activated safe mode manually or the game detected it did not start correctly last time and thus you are in #LIGHT_GREEN#safe mode#WHITE#.
Safe Mode disabled all graphical options and sets a low FPS. It is not advisable to play this way (as it will be very painful and ugly).

Please go to the Video Options and try enabling/disabling options and then restarting until you do not get this message.
A usual problem is shaders and thus should be your first target to disable.]], [[Oops! Either you activated safe mode manually or the game detected it did not start correctly last time and thus you are in #LIGHT_GREEN#safe mode#WHITE#.
Safe Mode disabled all graphical options and sets a low FPS. It is not advisable to play this way (as it will be very painful and ugly).

Please go to the Video Options and try enabling/disabling options and then restarting until you do not get this message.
A usual problem is shaders and thus should be your first target to disable.]], "_t")
t("Message", "Mensaje", "_t")
t("Duplicate Addon", "Addon duplicado", "_t")
t([[Oops! It seems like you have the same addon/dlc installed twice.
This is unsupported and would make many things explode. Please remove one of the copies.

Addon name: #YELLOW#%s#LAST#

Check out the following folder on your computer:
%s
%s
]], [[Oops! It seems like you have the same addon/dlc installed twice.
This is unsupported and would make many things explode. Please remove one of the copies.

Addon name: #YELLOW#%s#LAST#

Check out the following folder on your computer:
%s
%s
]], "_t")
t("Updating addon: #LIGHT_GREEN#%s", "Actualizando addon: #LIGHT_GREEN#%s", "tformat")
t("Quit", "Salir", "_t")
t("Really exit T-Engine/ToME?", "¿Salir de T-Engine/ToME?", "_t")
t("Continue", "Continuar", "_t")
t([[Welcome to #LIGHT_GREEN#Tales of Maj'Eyal#LAST#!

Before you can start dying in many innovative ways we need to ask you about online play.

This is a #{bold}#single player game#{normal}# but it also features many online features to enhance your gameplay and connect you to the community:
* Play from several computers without having to copy unlocks and achievements.
* Talk ingame to other fellow players, ask for advice, share your most memorable moments...
* Keep track of your kill count, deaths, most played classes...
* Cool statistics for to help sharpen your gameplay style
* Install official expansions and third-party addons directly from the game, hassle-free
* Access your purchaser / donator bonuses if you have bought the game or donated on https://te4.org/
* Help the game developers balance and refine the game

You will also have a user page on #LIGHT_BLUE#https://te4.org/#LAST# to show off to your friends.
This is all optional, you are not forced to use this feature at all, but the developer would thank you if you did as it will make balancing easier.]], [[Welcome to #LIGHT_GREEN#Tales of Maj'Eyal#LAST#!

Before you can start dying in many innovative ways we need to ask you about online play.

This is a #{bold}#single player game#{normal}# but it also features many online features to enhance your gameplay and connect you to the community:
* Play from several computers without having to copy unlocks and achievements.
* Talk ingame to other fellow players, ask for advice, share your most memorable moments...
* Keep track of your kill count, deaths, most played classes...
* Cool statistics for to help sharpen your gameplay style
* Install official expansions and third-party addons directly from the game, hassle-free
* Access your purchaser / donator bonuses if you have bought the game or donated on https://te4.org/
* Help the game developers balance and refine the game

You will also have a user page on #LIGHT_BLUE#https://te4.org/#LAST# to show off to your friends.
This is all optional, you are not forced to use this feature at all, but the developer would thank you if you did as it will make balancing easier.]], "_t")
t("Logging in...", "Iniciando sesión...", "_t")
t("Please wait...", "Espera por favor...", "_t")
t("Profile logged in!", "¡Perfil conectado!", "_t")
t("Your online profile is now active. Have fun!", "Tu perfil online está activo. ¡Diviértete!", "_t")
t("Login failed!", "¡Error al iniciar sesión!", "_t")
t("Check your login and password or try again in in a few moments.", "Comprueba tu usuario y contraseña o inténtalo de nuevo en unos momentos.", "_t")
t("Registering...", "Registrando...", "_t")
t("Registering on https://te4.org/, please wait...", "Registrando en https://te4.org/, espera...", "_t")
t("Logged in!", "¡Sesión iniciada!", "_t")
t("Profile created!", "¡Perfil creado!", "_t")
t("Profile creation failed!", "¡Error al crear perfil!", "_t")
t("Creation failed: %s (you may also register on https://te4.org/)", "Error al crear: %s (también puedes registrarte en https://te4.org/)", "tformat")
t("Try again in in a few moments, or try online at https://te4.org/", "Inténtalo de nuevo en unos momentos, o prueba online en https://te4.org/", "_t")


------------------------------------------------
-- section "mod-boot/mod/class/Player.lua"


-- new text
t("%s available", "%s disponible", "tformat")
t("#00ff00#Talent %s is ready to use.", "#00ff00#Talento %s listo para usar.", "log")
t("LEVEL UP!", "¡SUBIR DE NIVEL!", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/Addons.lua"


-- new text
t("Configure Addons", "Configurar addons", "_t")
t("You can get new addons at #LIGHT_BLUE##{underline}#Te4.org Addons#{normal}#", "Puedes conseguir nuevos addons en #LIGHT_BLUE##{underline}#Te4.org Addons#{normal}#", "_t")
t(" and #LIGHT_BLUE##{underline}#Te4.org DLCs#{normal}#", " y #LIGHT_BLUE##{underline}#Te4.org DLCs#{normal}#", "_t")
t("You can get new addons on #LIGHT_BLUE##{underline}#Steam Workshop#{normal}#", "Puedes conseguir addons en #LIGHT_BLUE##{underline}#Steam Workshop#{normal}#", "_t")
t(", #LIGHT_BLUE##{underline}#Te4.org Addons#{normal}#", ", #LIGHT_BLUE##{underline}#Addons de Te4.org#{normal}#", "_t")
t("Show incompatible", "Mostrar incompatibles", "_t")
t("Auto-update on start", "Actualizar automáticamente al inicio", "_t")
t("Game Module", "Módulo del juego", "_t")
t("Version", "Versión", "_t")
t("Addon", "Addon", "_t")
t("Active", "Activo", "_t")
t("#GREY#Developer tool", "#GREY#Herramienta de desarrollo", "_t")
t("#LIGHT_RED#Donator Status: Disabled", "#LIGHT_RED#Estado de donante: Desactivado", "_t")
t("#LIGHT_GREEN#Manual: Active", "#LIGHT_GREEN#Manual: Activo", "_t")
t("#LIGHT_RED#Manual: Disabled", "#LIGHT_RED#Manual: Desactivado", "_t")
t("#LIGHT_GREEN#Auto: Active", "#LIGHT_GREEN#Auto: Activo", "_t")
t("#LIGHT_RED#Auto: Incompatible", "#LIGHT_RED#Auto: Incompatible", "_t")
t("Addon Version", "Versión del addon", "_t")
t("Game Version", "Versión del juego", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/Credits.lua"


-- new text
t("Project Lead", "Director del proyecto", "_t")
t("Lead Coder", "Programador principal", "_t")
t("World Builders", "Constructores del mundo", "_t")
t("Graphic Artists", "Artistas gráficos", "_t")
t("Expert Shaders Design", "Diseño experto de shaders", "_t")
t("Soundtracks", "Banda sonora", "_t")
t("Sound Designer", "Diseñador de sonido", "_t")
t("Lore Creation and Writing", "Creación y escritura del lore", "_t")
t("Code Heroes", "Héroes del código", "_t")
t("Community Managers", "Gestores de la comunidad", "_t")
t("Text Editors", "Editores de texto", "_t")
t("Chinese Translation Lead", "Líder de traducción al chino", "_t")
t("Chinese Translators", "Traductores al chino", "_t")
t("Korean Translation", "Traducción al coreano", "_t")
t("Japanese Translation", "Traducción al japonés", "_t")
t("The Community", "La comunidad", "_t")
t("Others", "Otros", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/FirstRun.lua"


-- new text
t("Welcome to Tales of Maj'Eyal", "Bienvenido a Tales of Maj'Eyal", "_t")
t("Register now!", "¡Regístrate ahora!", "_t")
t("Login existing account", "Iniciar sesión existente", "_t")
t("Maybe later", "Quizás más tarde", "_t")
t("#RED#Disable all online features", "#RED#Desactivar funciones online", "_t")
t("Disable all connectivity", "Desactivar toda conectividad", "_t")
t([[You are about to disable all connectivity to the network.
This includes, but is not limited to:
- Player profiles: You will not be able to login, register
- Characters vault: You will not be able to upload any character to the online vault to show your glory
- Item's Vault: You will not be able to access the online item's vault, this includes both storing and retrieving items.
- Ingame chat: The ingame chat requires to connect to the server to talk to other players, this will not be possible.
- Purchaser / Donator benefits: The base game being free, the only way to give donators their bonuses fairly is to check their online profile. This will thus be disabled.
- Easy addons downloading & installation: You will not be able to see ingame the list of available addons, nor to one-click install them. You may still do so manually.
- Version checks: Addons will not be checked for new versions.
- Discord: If you are a Discord user, Rich Presence integration will also be disabled by this setting.
- Ingame game news: The main menu will stop showing you info about new updates to the game.

#{bold}##CRIMSON#This is an extremely restrictive setting. It is recommended you only activate it if you have no other choice as it will remove many fun and acclaimed features.#{normal}#

If you disable this option you can always re-activate it in the Online category of the Game Options menu later on.]], [[You are about to disable all connectivity to the network.
This includes, but is not limited to:
- Player profiles: You will not be able to login, register
- Characters vault: You will not be able to upload any character to the online vault to show your glory
- Item's Vault: You will not be able to access the online item's vault, this includes both storing and retrieving items.
- Ingame chat: The ingame chat requires to connect to the server to talk to other players, this will not be possible.
- Purchaser / Donator benefits: The base game being free, the only way to give donators their bonuses fairly is to check their online profile. This will thus be disabled.
- Easy addons downloading & installation: You will not be able to see ingame the list of available addons, nor to one-click install them. You may still do so manually.
- Version checks: Addons will not be checked for new versions.
- Discord: If you are a Discord user, Rich Presence integration will also be disabled by this setting.
- Ingame game news: The main menu will stop showing you info about new updates to the game.

#{bold}##CRIMSON#This is an extremely restrictive setting. It is recommended you only activate it if you have no other choice as it will remove many fun and acclaimed features.#{normal}#

If you disable this option you can always re-activate it in the Online category of the Game Options menu later on.]], "_t")
t("Cancel", "Cancelar", "_t")
t("#RED#Disable all!", "#RED#¡Desactivar todo!", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/LoadGame.lua"


-- new text
t("Load Game", "Cargar partida", "_t")
t("Show older versions", "Mostrar versiones antiguas", "_t")
t("Ignore unloadable addons", "Ignorar addons no cargables", "_t")
t("  Play!  ", "  ¡Jugar!  ", "_t")
t("Delete", "Eliminar", "_t")
t([[#{bold}##GOLD#%s: %s#WHITE##{normal}#
Game version: %d.%d.%d
Requires addons: %s

%s]], [[#{bold}##GOLD#%s: %s#WHITE##{normal}#
Game version: %d.%d.%d
Requires addons: %s

%s]], "tformat")
t("You can simply grab an older version of the game from where you downloaded it.", "Puedes descargar una versión anterior desde donde descargaste el juego.", "_t")
t("You can downgrade the version by selecting it in the Steam's \"Beta\" properties of the game.", "Puedes bajar la versión seleccionándola en las propiedades \"Beta\" del juego en Steam.", "_t")
t("Original game version not found", "Versión original no encontrada", "_t")
t([[This savefile was created with game version %s. You can try loading it with the current version if you wish but it is recommended you play it with the old version to ensure compatibility
%s]], [[This savefile was created with game version %s. You can try loading it with the current version if you wish but it is recommended you play it with the old version to ensure compatibility
%s]], "tformat")
t("Cancel", "Cancelar", "_t")
t("Run with newer version", "Ejecutar con versión reciente", "_t")
t("Developer Mode", "Modo desarrollador", "_t")
t("#LIGHT_RED#WARNING: #LAST#Loading a savefile while in developer mode will permanently invalidate it. Proceed?", "#LIGHT_RED#AVISO: #LAST#Cargar una partida en modo desarrollador la invalidara permanentemente. ?Proceder?", "_t")
t("Load anyway", "Cargar de todas formas", "_t")
t("Delete savefile", "Eliminar partida", "_t")
t("Really delete #{bold}##GOLD#%s#WHITE##{normal}#", "¿Eliminar #{bold}##GOLD#%s#WHITE##{normal}#?", "tformat")
t("Old game data", "Datos antiguos", "_t")
t("No data available for this game version.", "No hay datos para esta versión.", "_t")
t("Downloading old game data: #LIGHT_GREEN#", "Descargando datos antiguos: #LIGHT_GREEN#", "_t")
t("Old game data for %s correctly installed. You can now play.", "Datos antiguos para %s instalados. Ya puedes jugar.", "tformat")
t("Failed to install.", "Error al instalar.", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/MainMenu.lua"


-- new text
t("Main Menu", "Menú principal", "_t")
t("New Game", "Nueva partida", "_t")
t("Load Game", "Cargar partida", "_t")
t("Addons", "Addons", "_t")
t("Options", "Opciones", "_t")
t("Game Options", "Opciones del juego", "_t")
t("Credits", "Créditos", "_t")
t("Exit", "Salir", "_t")
t("Reboot", "Reiniciar", "_t")
t("Disable animated background", "Desactivar fondo animado", "_t")
t("#{bold}##B9E100#T-Engine4 version: %d.%d.%d", "#{bold}##B9E100#Versión T-Engine4: %d.%d.%d", "tformat")
t([[#{bold}##GOLD#Ashes of Urh'Rok - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#Many in Maj'Eyal have heard of "demons", sadistic creatures who appear seemingly from nowhere, leaving a trail of suffering and destruction wherever they go.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#New class:#WHITE# Doombringers. These avatars of demonic destruction charge into battle with massive two-handed weapons, cutting swaths of firey devastation through hordes of opponents. Armed with flame magic and demonic strength, they delight in fighting against overwhelming odds
#LIGHT_UMBER#New class:#WHITE# Demonologists. Bearing a shield and the magic of the Spellblaze itself, these melee-fighting casters can grow demonic seeds from their fallen enemies. Imbue these seeds onto your items to gain a wide array of new talents and passive benefits, and summon the demons within them to fight!
#LIGHT_UMBER#New race:#WHITE# Doomelves. Shalore who've taken to the demonic alterations especially well, corrupting their typical abilities into a darker form.
#LIGHT_UMBER#New artifacts, lore, zones, events...#WHITE# For your demonic delight!

]], [[#{bold}##GOLD#Ashes of Urh'Rok - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#Many in Maj'Eyal have heard of "demons", sadistic creatures who appear seemingly from nowhere, leaving a trail of suffering and destruction wherever they go.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#New class:#WHITE# Doombringers. These avatars of demonic destruction charge into battle with massive two-handed weapons, cutting swaths of firey devastation through hordes of opponents. Armed with flame magic and demonic strength, they delight in fighting against overwhelming odds
#LIGHT_UMBER#New class:#WHITE# Demonologists. Bearing a shield and the magic of the Spellblaze itself, these melee-fighting casters can grow demonic seeds from their fallen enemies. Imbue these seeds onto your items to gain a wide array of new talents and passive benefits, and summon the demons within them to fight!
#LIGHT_UMBER#New race:#WHITE# Doomelves. Shalore who've taken to the demonic alterations especially well, corrupting their typical abilities into a darker form.
#LIGHT_UMBER#New artifacts, lore, zones, events...#WHITE# For your demonic delight!

]], "_t")
t("#LIGHT_GREEN#Installed", "#LIGHT_GREEN#Instalado", "_t")
t("#YELLOW#Not installed - Click to download / purchase", "#YELLOW#No instalado - Click para descargar/comprar", "_t")
t([[#{bold}##GOLD#Embers of Rage - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#One year has passed since the one the Orcs call the "Scourge from the West" came and single-handedly crushed the Orc Prides of Grushnak, Vor, Gorbat, and Rak'Shor.  The Allied Kingdoms, now linked by farportal to their distant, long-lost Sunwall allies, have helped them conquer most of Var'Eyal.  The few remnants of the ravaged Prides are caged...  but one Pride remains.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#A whole new campaign:#WHITE# Set one year after the events of the main game, the final destiny of the Orc Prides is up to you. Discover the Far East like you never knew it. 
#LIGHT_UMBER#New classes:#WHITE# Sawbutchers, Gunslingers, Psyshots, Annihilators and Technomanchers. Harness the power of steam to power deadly contraptions to lay waste to all those that oppose the Pride!  
#LIGHT_UMBER#New races:#WHITE# Orcs, Yetis, Whitehooves. Discover the orcs and their unlikely 'allies' as you try to save your Pride from the disasters caused by the one you call 'The Scourge from the West'.
#LIGHT_UMBER#Tinker system:#WHITE# Augment your items with powerful crafted tinkers. Attach rockets to your boots, gripping systems to your gloves and many more.
#LIGHT_UMBER#Salves:#WHITE# Bound to the tinker system, create powerful medical salves to inject into your skin, replacing the infusions§runes system.
#LIGHT_UMBER#A ton#WHITE# of artifacts, lore, zones, events... 

]], [[#{bold}##GOLD#Embers of Rage - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#One year has passed since the one the Orcs call the "Scourge from the West" came and single-handedly crushed the Orc Prides of Grushnak, Vor, Gorbat, and Rak'Shor.  The Allied Kingdoms, now linked by farportal to their distant, long-lost Sunwall allies, have helped them conquer most of Var'Eyal.  The few remnants of the ravaged Prides are caged...  but one Pride remains.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#A whole new campaign:#WHITE# Set one year after the events of the main game, the final destiny of the Orc Prides is up to you. Discover the Far East like you never knew it. 
#LIGHT_UMBER#New classes:#WHITE# Sawbutchers, Gunslingers, Psyshots, Annihilators and Technomanchers. Harness the power of steam to power deadly contraptions to lay waste to all those that oppose the Pride!  
#LIGHT_UMBER#New races:#WHITE# Orcs, Yetis, Whitehooves. Discover the orcs and their unlikely 'allies' as you try to save your Pride from the disasters caused by the one you call 'The Scourge from the West'.
#LIGHT_UMBER#Tinker system:#WHITE# Augment your items with powerful crafted tinkers. Attach rockets to your boots, gripping systems to your gloves and many more.
#LIGHT_UMBER#Salves:#WHITE# Bound to the tinker system, create powerful medical salves to inject into your skin, replacing the infusions§runes system.
#LIGHT_UMBER#A ton#WHITE# of artifacts, lore, zones, events... 

]], "_t")
t([[#{bold}##GOLD#Forgotten Cults - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#Not all adventurers seek fortune, not all that defend the world have good deeds in mind. Lately the number of sightings of horrors have grown tremendously. People wander off the beaten paths only to be found years later, horribly mutated and partly insane, if they are found at all. It is becoming evident something is stirring deep below Maj'Eyal. That something is you.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#New class:#WHITE# Writhing Ones. Give in to the corrupting forces and turn yourself gradually into an horror, summon horrors to do your bidding, shed your skin and melt your face to assault your foes. With your arm already turned into a tentacle, what creature can stop you?
#LIGHT_UMBER#New class:#WHITE# Cultists of Entropy. Using its insanity and control of entropic forces to unravel the normal laws of physic this caster class can turn healing into attacks and call upon the forces of the void to reduce its foes to dust.
#LIGHT_UMBER#New race:#WHITE# Drems. A corrupt subrace of dwarves, that somehow managed to keep a shred of sanity to not fully devolve into mindless horrors. They can enter a frenzy and even learn to summon horrors.
#LIGHT_UMBER#New race:#WHITE# Krogs. Ogres transformed by the very thing that should kill them. Their powerful attacks can stun their foes and they are so strong they can dual wield any one handed weapons.
#LIGHT_UMBER#Many new zones:#WHITE# Explore the Scourge Pits, fight your way out of a giant worm (don't ask how you get *in*), discover the wonders of the Occult Egress and many more strange and tentacle-filled zones!
#LIGHT_UMBER#New horrors:#WHITE# You liked radiant horrors? You'll love searing horrors! And Nethergames. And Entropic Shards. And ... more
#LIGHT_UMBER#Sick of your own head:#WHITE#  Replace it with a nice cozy horror!
#LIGHT_UMBER#A ton#WHITE# of artifacts, lore, events... 

]], [[#{bold}##GOLD#Forgotten Cults - Expansion#LAST##{normal}#
#{italic}##ANTIQUE_WHITE#Not all adventurers seek fortune, not all that defend the world have good deeds in mind. Lately the number of sightings of horrors have grown tremendously. People wander off the beaten paths only to be found years later, horribly mutated and partly insane, if they are found at all. It is becoming evident something is stirring deep below Maj'Eyal. That something is you.#{normal}##LAST#

#{bold}#Features#{normal}#:
#LIGHT_UMBER#New class:#WHITE# Writhing Ones. Give in to the corrupting forces and turn yourself gradually into an horror, summon horrors to do your bidding, shed your skin and melt your face to assault your foes. With your arm already turned into a tentacle, what creature can stop you?
#LIGHT_UMBER#New class:#WHITE# Cultists of Entropy. Using its insanity and control of entropic forces to unravel the normal laws of physic this caster class can turn healing into attacks and call upon the forces of the void to reduce its foes to dust.
#LIGHT_UMBER#New race:#WHITE# Drems. A corrupt subrace of dwarves, that somehow managed to keep a shred of sanity to not fully devolve into mindless horrors. They can enter a frenzy and even learn to summon horrors.
#LIGHT_UMBER#New race:#WHITE# Krogs. Ogres transformed by the very thing that should kill them. Their powerful attacks can stun their foes and they are so strong they can dual wield any one handed weapons.
#LIGHT_UMBER#Many new zones:#WHITE# Explore the Scourge Pits, fight your way out of a giant worm (don't ask how you get *in*), discover the wonders of the Occult Egress and many more strange and tentacle-filled zones!
#LIGHT_UMBER#New horrors:#WHITE# You liked radiant horrors? You'll love searing horrors! And Nethergames. And Entropic Shards. And ... more
#LIGHT_UMBER#Sick of your own head:#WHITE#  Replace it with a nice cozy horror!
#LIGHT_UMBER#A ton#WHITE# of artifacts, lore, events... 

]], "_t")
t("#GOLD#Online Profile", "#GOLD#Perfil online", "_t")
t("Login", "Iniciar sesión", "_t")
t("Register", "Registrarse", "_t")
t("Username: ", "Usuario: ", "_t")
t("Password: ", "Contraseña: ", "_t")
t("Login with Steam", "Iniciar sesión con Steam", "_t")
t("#GOLD#Online Profile#WHITE#", "#GOLD#Perfil online#WHITE#", "_t")
t("#LIGHT_BLUE##{underline}#%s#LAST##{normal}#", "#LIGHT_BLUE##{underline}#%s#LAST##{normal}#", "tformat")
t("#LIGHT_BLUE##{underline}#Logout", "#LIGHT_BLUE##{underline}#Cerrar sesión", "_t")
t("Username", "Usuario", "_t")
t("Your username is too short", "Tu usuario es demasiado corto", "_t")
t("Password", "Contraseña", "_t")
t("Your password is too short", "Tu contraseña es demasiado corta", "_t")
t("Login...", "Iniciando sesión...", "_t")
t("Logging in your account, please wait...", "Iniciando sesión, espera...", "_t")
t("Steam client not found.", "Cliente Steam no encontrado.", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/NewGame.lua"


-- new text
t("New Game", "Nueva partida", "_t")
t("Show all versions", "Mostrar todas las versiones", "_t")
t("Show incompatible", "Mostrar incompatibles", "_t")
t([[You can get new games at
#LIGHT_BLUE##{underline}#https://te4.org/games#{normal}#]], [[You can get new games at
#LIGHT_BLUE##{underline}#https://te4.org/games#{normal}#]], "_t")
t("Game Module", "Módulo del juego", "_t")
t("Version", "Versión", "_t")
t("Enter your character's name", "Introduce el nombre de tu personaje", "_t")
t("Overwrite character?", "¿Sobrescribir personaje?", "_t")
t("There is already a character with this name, do you want to overwrite it?", "Ya existe un personaje con ese nombre, ¿quieres sobrescribirlo?", "_t")
t("No", "No", "_t")
t("Yes", "Sí", "_t")
t("This game is not compatible with your version of T-Engine, you can still try it but it might break.", "Este juego no es compatible con tu version de T-Engine, puedes probarlo pero podria romperse.", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/Profile.lua"


-- new text
t("Player Profile", "Perfil del jugador", "_t")
t("Logout", "Cerrar sesión", "_t")
t("You are logged in", "Has iniciado sesión", "_t")
t("Do you want to log out?", "¿Quieres cerrar sesión?", "_t")
t("Log out", "Cerrar sesión", "_t")
t("Cancel", "Cancelar", "_t")
t("Login", "Iniciar sesión", "_t")
t("Create Account", "Crear cuenta", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/ProfileLogin.lua"


-- new text
t("Online profile ", "Perfil online ", "_t")
t("Username: ", "Usuario: ", "_t")
t("Password: ", "Contraseña: ", "_t")
t("Login", "Iniciar sesión", "_t")
t("Cancel", "Cancelar", "_t")
t("Password again: ", "Contraseña de nuevo: ", "_t")
t("Email: ", "Correo electronico: ", "_t")
t("Accept to receive #{bold}#very infrequent#{normal}# (a few per year) mails about important game events from us.", "Acepto recibir #{bold}#poco frecuentes#{normal}# (unas pocas al anyo) emails sobre eventos importantes del juego.", "_t")
t("You at least 16 years old, or have parental authorization to play the game.", "Tienes al menos 16 años, o autorización parental para jugar.", "_t")
t("Create", "Crear", "_t")
t("Privacy Policy (opens in browser)", "Política de privacidad (se abre en el navegador)", "_t")
t("Password", "Contraseña", "_t")
t("Password mismatch!", "¡Las contraseñas no coinciden!", "_t")
t("Username", "Usuario", "_t")
t("Your username is too short", "Tu usuario es demasiado corto", "_t")
t("Your password is too short", "Tu contraseña es demasiado corta", "_t")
t("Email", "Correo electronico", "_t")
t("Your email seems invalid", "Tu email parece inválido", "_t")
t("Age Check", "Verificación de edad", "_t")
t("You need to be 16 years old or more or to have parental authorization to play this game.", "Necesitas 16 años o más, o autorización parental para jugar.", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/ProfileSteamRegister.lua"


-- new text
t("Steam User Account", "Cuenta de usuario Steam", "_t")
t([[Welcome to #GOLD#Tales of Maj'Eyal#LAST#.
To enjoy all the features the game has to offer it is #{bold}#highly#{normal}# recommended that you register your steam account.
Luckily this is very easy to do: you only require a profile name and optionally an email (we send very few email, maybe two a year at most).
]], [[Welcome to #GOLD#Tales of Maj'Eyal#LAST#.
To enjoy all the features the game has to offer it is #{bold}#highly#{normal}# recommended that you register your steam account.
Luckily this is very easy to do: you only require a profile name and optionally an email (we send very few email, maybe two a year at most).
]], "_t")
t("Username: ", "Usuario: ", "_t")
t("Email: ", "Correo electrónico:", "_t")
t("Accept to receive #{bold}#very infrequent#{normal}# (a few per year) mails about important game events from us.", "Acepto recibir #{bold}#poco frecuentes#{normal}# (unas pocas al anyo) emails sobre eventos importantes del juego.", "_t")
t("You at least 16 years old, or have parental authorization to play the game.", "Tienes al menos 16 años, o autorización parental para jugar.", "_t")
t("Register", "Registrarse", "_t")
t("Cancel", "Cancelar", "_t")
t("Privacy Policy (opens in browser)", "Política de privacidad (se abre en el navegador)", "_t")
t("Username", "Usuario", "_t")
t("Your username is too short", "Tu usuario es demasiado corto", "_t")
t("Email", "Correo electronico", "_t")
t("Your email does not look right.", "Tu email no parece correcto.", "_t")
t("Age Check", "Verificación de edad", "_t")
t("You need to be 16 years old or more or to have parental authorization to play this game.", "Necesitas 16 años o más, o autorización parental para jugar.", "_t")
t("Registering...", "Registrando...", "_t")
t("Registering on https://te4.org/, please wait...", "Registrando en https://te4.org/, espera...", "_t")
t("Steam client not found.", "Cliente Steam no encontrado.", "_t")
t("Error", "Error", "_t")
t("Username or Email already taken, please select an other one.", "Usuario o Email ya en uso, elige otro.", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/UpdateAll.lua"


-- new text
t("Update all game modules", "Actualizar todos los módulos", "_t")
t([[All those components will be updated:
]], [[All those components will be updated:
]], "_t")
t("Component", "Componente", "_t")
t("Version", "Versión", "_t")
t("Nothing to update", "Nada que actualizar", "_t")
t("All your game modules are up to date.", "Todos tus módulos están actualizados.", "_t")
t("Game: #{bold}##GOLD#", "Juego: #{bold}##GOLD#", "_t")
t("Engine: #{italic}##LIGHT_BLUE#", "Motor: #{italic}##LIGHT_BLUE#", "_t")
t("Error!", "¡Error!", "_t")
t([[There was an error while downloading:
]], [[There was an error while downloading:
]], "_t")
t("Downloading: ", "Descargando: ", "_t")
t("Update", "Actualizar", "_t")
t("All updates installed, the game will now restart", "Todas las actualizaciones instaladas, el juego se reiniciará", "_t")


------------------------------------------------
-- section "mod-boot/mod/dialogs/ViewHighScores.lua"


-- new text
t("View High Scores", "Ver altas puntuaciones", "_t")
t("Game Module", "Módulo del juego", "_t")
t("Version", "Versión", "_t")
t("World", "Mundo", "_t")
t([[#{bold}##GOLD#%s#GREEN# High Scores#WHITE##{normal}#

]], [[#{bold}##GOLD#%s#GREEN# High Scores#WHITE##{normal}#

]], "tformat")
t([[#{bold}##GOLD#%s(%s)#GREEN# High Scores#WHITE##{normal}#

]], [[#{bold}##GOLD#%s(%s)#GREEN# High Scores#WHITE##{normal}#

]], "tformat")


------------------------------------------------
-- section "mod-boot/mod/init.lua"


-- new text
t("Tales of Maj'Eyal Main Menu", "Menú principal de Tales of Maj'Eyal", "init.lua long_name")
t([[Bootmenu!
]], [[Bootmenu!
]], "init.lua description")


------------------------------------------------
-- section "mod-boot/mod/load.lua"


-- new text
t("Strength", "Fuerza", "stat name")
t("str", "Fue", "stat short_name")
t("Dexterity", "Destreza", "stat name")
t("dex", "Des", "stat short_name")
t("Constitution", "Constitución", "stat name")
t("con", "Con", "stat short_name")


