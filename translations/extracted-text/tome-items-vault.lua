------------------------------------------------
section "tome-items-vault/data/entities/fortress-grids.lua"

tDef(21, "Item's Vault Control Orb", "entity name", true) -- 


------------------------------------------------
section "tome-items-vault/hooks/load.lua"



------------------------------------------------
section "tome-items-vault/init.lua"

tDef(20, "Items Vault", "init.lua long_name", true) -- 
tDef(27, "Adds access to the items vault (donator feature). The items vault will let you upload a few unwanted items to your online profile and retrieve them on other characters.", "init.lua description", true) -- 


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb-offline.lua"

tDef(28, "Transfering this item will place a level %d requirement on it, since it has no requirements. ", "tformat", true) -- 
tDef(31, "Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "_t", true) -- 
tDef(60, "*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.\
All your characters in alternate universes will be able to access it from here.\
Only items from a validated game versions are uploadable.#WHITE#*\
\
#CRIMSON#Offline mode#WHITE#: The item's vault works even without a network connection but items will thus only be saved on your computer and can not be shared to an other one.\
The offline vault is only available when offline and contains 3 slots.", "_t", true) -- 
tDef(67, "[Place an item in the vault]", "_t", true) -- 
tDef(69, "Item's Vault", "_t", true) -- 
tDef(69, "You can not place an item in the vault from debug mode game.", "_t", true) -- 
tDef(74, "Place an item in the Item's Vault", "_t", true) -- 
tDef(80, "Caution", "_t", true) -- 
tDef(80, "Continue?", "_t", true) -- 
tDef(97, "[Retrieve an item from the vault]", "_t", true) -- 
tDef(101, "[Leave the orb alone]", "_t", true) -- 


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb.lua"

tDef(28, "Transfering this item will place a level %d requirement on it, since it has no requirements. ", "tformat", true) -- 
tDef(31, "Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "_t", true) -- 
tDef(60, "*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.\
All your characters in alternate universes will be able to access it from here.\
Only items from a validated game versions are uploadable.#WHITE#*\
\
#GOLD#Donator's Feature#ANCIENT_WHITE#: Items are saved on the server, only donators have access to this feature and the number of items storable at once depends on your generosity.\
I, DarkGod, the maker of this game want to personaly thank all donators because you people are keeping this game going. Thanks and enjoy!", "_t", true) -- 
tDef(74, "\
#CRIMSON#Note for Steam Players#ANCIENT_WHITE#: This feature requires you to have registered a profile & bound it to steam (automatic if you register ingame) because it needs to store things on the server.\
Until you do so you will get an error.", "_t", true) -- 
tDef(79, "[Place an item in the vault]", "_t", true) -- 
tDef(81, "Item's Vault", "_t", true) -- 
tDef(81, "You can not place an item in the vault from an un-validated game.", "_t", true) -- 
tDef(86, "Place an item in the Item's Vault", "_t", true) -- 
tDef(92, "Caution", "_t", true) -- 
tDef(92, "Continue?", "_t", true) -- 
tDef(109, "[Retrieve an item from the vault]", "_t", true) -- 
tDef(113, "#GOLD#I wish to help the funding of this game and donate#WHITE#", "_t", true) -- 
tDef(114, "[Leave the orb alone]", "_t", true) -- 


------------------------------------------------
section "tome-items-vault/overload/data/maps/items-vault/fortress.lua"

tDef(43, "Psionic Metarial Retention", "_t", true) -- 
tDef(47, "Temporal Locked Vault", "_t", true) -- 


------------------------------------------------
section "tome-items-vault/overload/engine/EntityVaultSave.lua"



------------------------------------------------
section "tome-items-vault/overload/mod/class/ItemsVaultDLC.lua"

tDef(30, "the #GOLD#Item's Vault#WHITE#", "_t", true) -- 
tDef(74, "\
#CRIMSON#This item has been sent to the Item's Vault.", "_t", true) -- 
tDef(91, "Transfering...", "_t", true) -- 
tDef(91, "Teleporting object to the vault, please wait...", "_t", true) -- 
tDef(94, "unknown reason", "_t", true) -- 
tDef(97, "#LIGHT_BLUE#You transfer %s to the online item's vault.", "logPlayer", true) -- 
tDef(108, "#LIGHT_RED#Error while transfering %s to the online item's vault, please retry later.", "logPlayer", true) -- 
tDef(109, "#CRIMSON#Server said: %s", "logPlayer", true) -- 
tDef(125, "#LIGHT_BLUE#You transfer %s to the offline item's vault.", "logPlayer", true) -- 
tDef(282, "Teleporting object from the vault, please wait...", "_t", true) -- 
tDef(309, "Transfer failed", "_t", true) -- 
tDef(309, "This item comes from a previous version and would not work in your current game.\
To prevent the universe from imploding the item was not transfered from the vault.", "_t", true) -- 
tDef(334, "Item's Vault", "_t", true) -- 
tDef(334, "Checking item's vault list, please wait...", "_t", true) -- 


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVault.lua"

tDef(32, "Item's Vault", "_t", true) -- 
tDef(32, "Impossible to contact the server, please wait a few minutes and try again.", "_t", true) -- 
tDef(37, "Item's Vault (%d/%d)", "tformat", true) -- 
tDef(39, "Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.\
\9#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.", "_t", true) -- 
tDef(43, "Name", "_t", true) -- 
tDef(44, "Usable", "_t", true) -- 
tDef(67, "#LIGHT_GREEN#Yes", "_t", true) -- 
tDef(70, "#LIGHT_RED#In less than one minute", "_t", true) -- 
tDef(72, "#LIGHT_RED#In %d minutes", "tformat", true) -- 
tDef(94, "Cooldown", "_t", true) -- 
tDef(94, "This item has been placed recently in the vault, you must wait a bit before removing it.", "_t", true) -- 
tDef(105, "#LIGHT_BLUE#You transfer %s from the online item's vault.", "log", true) -- 
tDef(107, "#LIGHT_RED#Error while transfering from the online item's vault, please retry later.", "log", true) -- 


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVaultOffline.lua"

tDef(32, "Item's Vault", "_t", true) -- 
tDef(32, "Impossible to contact the server, please wait a few minutes and try again.", "_t", true) -- 
tDef(37, "Item's Vault (%d/%d)", "tformat", true) -- 
tDef(39, "Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.\
\9#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.", "_t", true) -- 
tDef(43, "Name", "_t", true) -- 
tDef(44, "Usable", "_t", true) -- 
tDef(67, "#LIGHT_GREEN#Yes", "_t", true) -- 
tDef(70, "#LIGHT_RED#In less than one minute", "_t", true) -- 
tDef(72, "#LIGHT_RED#In %d minutes", "tformat", true) -- 
tDef(94, "Cooldown", "_t", true) -- 
tDef(94, "This item has been placed recently in the vault, you must wait a bit before removing it.", "_t", true) -- 
tDef(105, "#LIGHT_BLUE#You transfer %s from the offline item's vault.", "log", true) -- 
tDef(107, "#LIGHT_RED#Error while transfering from the offline item's vault, please retry later.", "log", true) -- 


