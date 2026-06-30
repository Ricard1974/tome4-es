------------------------------------------------
section "tome-items-vault/data/entities/fortress-grids.lua"


-- new text
--[==[
t("Item's Vault Control Orb", "Orb de Control del Banco de Objetos", "entity name")
--]==]


------------------------------------------------
section "tome-items-vault/init.lua"


-- new text
--[==[
t("Items Vault", "Banco de Objetos", "init.lua long_name")
t("Adds access to the items vault (donator feature). The items vault will let you upload a few unwanted items to your online profile and retrieve them on other characters.", "Anade acceso al banco de objetos (funcion de donantes). El banco de objetos te permite subir objetos no deseados a tu perfil online y recuperarlos con otros personajes.", "init.lua description")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb-offline.lua"


-- new text
--[==[
t("Transfering this item will place a level %d requirement on it, since it has no requirements. ", "Transferir este objeto le pondra un requisito de nivel %d, ya que no tiene requisitos. ", "tformat")
t("Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "Algunas propiedades del objeto se perderan al transferirlo, ya que son especificas de clase o talento. ", "_t")
t([[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#CRIMSON#Offline mode#WHITE#: The item's vault works even without a network connection but items will thus only be saved on your computer and can not be shared to an other one.
The offline vault is only available when offline and contains 3 slots.]], [[*#LIGHT_GREEN#Este orbe parece ser una interfaz hacia un banco de objetos extradimensional.
Todos tus personajes de universos alternativos podran acceder a el desde aqui.
Solo se pueden subir objetos de versiones validadas del juego.#WHITE#*

#CRIMSON#Modo offline#WHITE#: El banco de objetos funciona incluso sin conexion a la red, pero los objetos solo se guardaran en tu ordenador y no podran compartirse con otros.
El banco offline solo esta disponible sin conexion y tiene 3 espacios.]], "_t")
t("[Place an item in the vault]", "[Colocar objeto en el banco]", "_t")
t("Item's Vault", "Banco de objetos", "_t")
t("You can not place an item in the vault from debug mode game.", "No puedes colocar objetos en el banco desde una partida en modo depuracion.", "_t")
t("Place an item in the Item's Vault", "Colocar objeto en el Banco de Objetos", "_t")
t("Caution", "Precaucion", "_t")
t("Continue?", "Continuar?", "_t")
t("[Retrieve an item from the vault]", "[Recuperar objeto del banco]", "_t")
t("[Leave the orb alone]", "[Dejar el orbe en paz]", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb.lua"


-- new text
--[==[
t("Transfering this item will place a level %d requirement on it, since it has no requirements. ", "Transferir este objeto le pondra un requisito de nivel %d, ya que no tiene requisitos. ", "tformat")
t("Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "Algunas propiedades del objeto se perderan al transferirlo, ya que son especificas de clase o talento. ", "_t")
t([[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#GOLD#Donator's Feature#ANCIENT_WHITE#: Items are saved on the server, only donators have access to this feature and the number of items storable at once depends on your generosity.
I, DarkGod, the maker of this game want to personaly thank all donators because you people are keeping this game going. Thanks and enjoy!]], [[*#LIGHT_GREEN#Este orbe parece ser una interfaz hacia un banco de objetos extradimensional.
Todos tus personajes de universos alternativos podran acceder a el desde aqui.
Solo se pueden subir objetos de versiones validadas del juego.#WHITE#*

#GOLD#Funcion de donantes#ANCIENT_WHITE#: Los objetos se guardan en el servidor, solo los donantes tienen acceso a esta funcion y el numero de objetos almacenables depende de tu generosidad.
Yo, DarkGod, el creador de este juego, quiero agradecer personalmente a todos los donantes porque vosotros manteneis este juego en marcha. Gracias y disfrutad!]], "_t")
t("\
#CRIMSON#Note for Steam Players#ANCIENT_WHITE#: This feature requires you to have registered a profile & bound it to steam (automatic if you register ingame) because it needs to store things on the server.\
Until you do so you will get an error.", "\
#CRIMSON#Nota para jugadores de Steam#ANCIENT_WHITE#: Esta funcion requiere que tengas un perfil registrado y vinculado a Steam (automatico si te registras desde el juego) porque necesita almacenar cosas en el servidor.\
Hasta que lo hagas, recibiras un error.", "_t")
t("[Place an item in the vault]", "[Colocar objeto en el banco]", "_t")
t("Item's Vault", "Banco de objetos", "_t")
t("You can not place an item in the vault from an un-validated game.", "No puedes colocar objetos en el banco desde una partida no validada.", "_t")
t("Place an item in the Item's Vault", "Colocar objeto en el Banco de Objetos", "_t")
t("Caution", "Precaucion", "_t")
t("Continue?", "Continuar?", "_t")
t("[Retrieve an item from the vault]", "[Recuperar objeto del banco]", "_t")
t("#GOLD#I wish to help the funding of this game and donate#WHITE#", "#GOLD#Quiero ayudar a financiar este juego y donar#WHITE#", "_t")
t("[Leave the orb alone]", "[Dejar el orbe en paz]", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/maps/items-vault/fortress.lua"


-- new text
--[==[
t("Psionic Metarial Retention", "Retencion de Material Psionico", "_t")
t("Temporal Locked Vault", "Banco Temporal Bloqueado", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/class/ItemsVaultDLC.lua"


-- new text
--[==[
t("the #GOLD#Item's Vault#WHITE#", "el #GOLD#Banco de Objetos#WHITE#", "_t")
t("\
#CRIMSON#This item has been sent to the Item's Vault.", "\
#CRIMSON#Este objeto ha sido enviado al Banco de Objetos.", "_t")
t("Transfering...", "Transfiriendo...", "_t")
t("Teleporting object to the vault, please wait...", "Teletransportando objeto al banco, espere...", "_t")
t("unknown reason", "motivo desconocido", "_t")
t("#LIGHT_BLUE#You transfer %s to the online item's vault.", "#LIGHT_BLUE#Transferes %s al banco de objetos en linea.", "logPlayer")
t("#LIGHT_RED#Error while transfering %s to the online item's vault, please retry later.", "#LIGHT_RED#Error al transferir %s al banco en linea, intentalo mas tarde.", "logPlayer")
t("#CRIMSON#Server said: %s", "#CRIMSON#El servidor dice: %s", "logPlayer")
t("#LIGHT_BLUE#You transfer %s to the offline item's vault.", "#LIGHT_BLUE#Transferes %s al banco de objetos local.", "logPlayer")
t("Teleporting object from the vault, please wait...", "Teletransportando objeto desde el banco, espere...", "_t")
t("Transfer failed", "Transferencia fallida", "_t")
t([[This item comes from a previous version and would not work in your current game.
To prevent the universe from imploding the item was not transfered from the vault.]], [[Este objeto proviene de una version anterior y no funcionaria en tu partida actual.
Para evitar que el universo implosione, el objeto no se ha transferido del banco.]], "_t")
t("Item's Vault", "Banco de objetos", "_t")
t("Checking item's vault list, please wait...", "Comprobando lista del banco, espere...", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVault.lua"


-- new text
--[==[
t("Item's Vault", "Banco de objetos", "_t")
t("Impossible to contact the server, please wait a few minutes and try again.", "Imposible contactar con el servidor, espera unos minutos e intentalo de nuevo.", "_t")
t("Item's Vault (%d/%d)", "Banco de Objetos (%d/%d)", "tformat")
t([[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], [[Recuperar un objeto del banco. Cuando colocas un objeto en el banco, las energias de paradoja a su alrededor son tan poderosas que debes esperar una hora antes de recuperarlo.
	#CRIMSON#Aviso: aunque *puedes* recuperar objetos hechos con versiones anteriores del juego, no se garantiza que el universo (o tu personaje) no explote.]], "_t")
t("Name", "Nombre", "_t")
t("Usable", "Utilizable", "_t")
t("#LIGHT_GREEN#Yes", "#LIGHT_GREEN#Si", "_t")
t("#LIGHT_RED#In less than one minute", "#LIGHT_RED#En menos de un minuto", "_t")
t("#LIGHT_RED#In %d minutes", "#LIGHT_RED#En %d minutos", "tformat")
t("Cooldown", "Reutilizacion", "_t")
t("This item has been placed recently in the vault, you must wait a bit before removing it.", "Este objeto ha sido colocado recientemente en el banco, debes esperar un poco antes de retirarlo.", "_t")
t("#LIGHT_BLUE#You transfer %s from the online item's vault.", "#LIGHT_BLUE#Recuperas %s del banco de objetos en linea.", "log")
t("#LIGHT_RED#Error while transfering from the online item's vault, please retry later.", "#LIGHT_RED#Error al recuperar del banco en linea, intentalo mas tarde.", "log")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVaultOffline.lua"


-- new text
--[==[
t("Item's Vault", "Banco de objetos", "_t")
t("Impossible to contact the server, please wait a few minutes and try again.", "Imposible contactar con el servidor, espera unos minutos e intentalo de nuevo.", "_t")
t("Item's Vault (%d/%d)", "Banco de Objetos (%d/%d)", "tformat")
t([[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], [[Recuperar un objeto del banco. Cuando colocas un objeto en el banco, las energias de paradoja a su alrededor son tan poderosas que debes esperar una hora antes de recuperarlo.
	#CRIMSON#Aviso: aunque *puedes* recuperar objetos hechos con versiones anteriores del juego, no se garantiza que el universo (o tu personaje) no explote.]], "_t")
t("Name", "Nombre", "_t")
t("Usable", "Utilizable", "_t")
t("#LIGHT_GREEN#Yes", "#LIGHT_GREEN#Si", "_t")
t("#LIGHT_RED#In less than one minute", "#LIGHT_RED#En menos de un minuto", "_t")
t("#LIGHT_RED#In %d minutes", "#LIGHT_RED#En %d minutos", "tformat")
t("Cooldown", "Reutilizacion", "_t")
t("This item has been placed recently in the vault, you must wait a bit before removing it.", "Este objeto ha sido colocado recientemente en el banco, debes esperar un poco antes de retirarlo.", "_t")
t("#LIGHT_BLUE#You transfer %s from the offline item's vault.", "#LIGHT_BLUE#Recuperas %s del banco de objetos local.", "log")
t("#LIGHT_RED#Error while transfering from the offline item's vault, please retry later.", "#LIGHT_RED#Error al recuperar del banco local, intentalo mas tarde.", "log")
--]==]


