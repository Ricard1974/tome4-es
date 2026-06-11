------------------------------------------------
section "tome-items-vault/data/entities/fortress-grids.lua"


-- new text
--[==[
t("Item's Vault Control Orb", "Item's Vault Control Orb", "entity name")
--]==]


------------------------------------------------
section "tome-items-vault/init.lua"


-- new text
--[==[
t("Items Vault", "Items Vault", "init.lua long_name")
t("Adds access to the items vault (donator feature). The items vault will let you upload a few unwanted items to your online profile and retrieve them on other characters.", "Adds access to the items vault (donator feature). The items vault will let you upload a few unwanted items to your online profile and retrieve them on other characters.", "init.lua description")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb-offline.lua"


-- new text
--[==[
t("Transfering this item will place a level %d requirement on it, since it has no requirements. ", "Transfering this item will place a level %d requirement on it, since it has no requirements. ", "tformat")
t("Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "_t")
t([[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#CRIMSON#Offline mode#WHITE#: The item's vault works even without a network connection but items will thus only be saved on your computer and can not be shared to an other one.
The offline vault is only available when offline and contains 3 slots.]], [[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#CRIMSON#Offline mode#WHITE#: The item's vault works even without a network connection but items will thus only be saved on your computer and can not be shared to an other one.
The offline vault is only available when offline and contains 3 slots.]], "_t")
t("[Place an item in the vault]", "[Place an item in the vault]", "_t")
t("Item's Vault", "Item's Vault", "_t")
t("You can not place an item in the vault from debug mode game.", "You can not place an item in the vault from debug mode game.", "_t")
t("Place an item in the Item's Vault", "Place an item in the Item's Vault", "_t")
t("Caution", "Caution", "_t")
t("Continue?", "Continue?", "_t")
t("[Retrieve an item from the vault]", "[Retrieve an item from the vault]", "_t")
t("[Leave the orb alone]", "[Leave the orb alone]", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/chats/items-vault-command-orb.lua"


-- new text
--[==[
t("Transfering this item will place a level %d requirement on it, since it has no requirements. ", "Transfering this item will place a level %d requirement on it, since it has no requirements. ", "tformat")
t("Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "Some properties of the item will be lost upon transfer, since they are class- or talent-specific. ", "_t")
t([[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#GOLD#Donator's Feature#ANCIENT_WHITE#: Items are saved on the server, only donators have access to this feature and the number of items storable at once depends on your generosity.
I, DarkGod, the maker of this game want to personaly thank all donators because you people are keeping this game going. Thanks and enjoy!]], [[*#LIGHT_GREEN#This orb seems to be some kind of interface to an extra-dimentional vault of items.
All your characters in alternate universes will be able to access it from here.
Only items from a validated game versions are uploadable.#WHITE#*

#GOLD#Donator's Feature#ANCIENT_WHITE#: Items are saved on the server, only donators have access to this feature and the number of items storable at once depends on your generosity.
I, DarkGod, the maker of this game want to personaly thank all donators because you people are keeping this game going. Thanks and enjoy!]], "_t")
t("\
#CRIMSON#Note for Steam Players#ANCIENT_WHITE#: This feature requires you to have registered a profile & bound it to steam (automatic if you register ingame) because it needs to store things on the server.\
Until you do so you will get an error.", "\
#CRIMSON#Note for Steam Players#ANCIENT_WHITE#: This feature requires you to have registered a profile & bound it to steam (automatic if you register ingame) because it needs to store things on the server.\
Until you do so you will get an error.", "_t")
t("[Place an item in the vault]", "[Place an item in the vault]", "_t")
t("Item's Vault", "Item's Vault", "_t")
t("You can not place an item in the vault from an un-validated game.", "You can not place an item in the vault from an un-validated game.", "_t")
t("Place an item in the Item's Vault", "Place an item in the Item's Vault", "_t")
t("Caution", "Caution", "_t")
t("Continue?", "Continue?", "_t")
t("[Retrieve an item from the vault]", "[Retrieve an item from the vault]", "_t")
t("#GOLD#I wish to help the funding of this game and donate#WHITE#", "#GOLD#I wish to help the funding of this game and donate#WHITE#", "_t")
t("[Leave the orb alone]", "[Leave the orb alone]", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/data/maps/items-vault/fortress.lua"


-- new text
--[==[
t("Psionic Metarial Retention", "Psionic Metarial Retention", "_t")
t("Temporal Locked Vault", "Temporal Locked Vault", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/class/ItemsVaultDLC.lua"


-- new text
--[==[
t("the #GOLD#Item's Vault#WHITE#", "the #GOLD#Item's Vault#WHITE#", "_t")
t("\
#CRIMSON#This item has been sent to the Item's Vault.", "\
#CRIMSON#This item has been sent to the Item's Vault.", "_t")
t("Transfering...", "Transfering...", "_t")
t("Teleporting object to the vault, please wait...", "Teleporting object to the vault, please wait...", "_t")
t("unknown reason", "unknown reason", "_t")
t("#LIGHT_BLUE#You transfer %s to the online item's vault.", "#LIGHT_BLUE#You transfer %s to the online item's vault.", "logPlayer")
t("#LIGHT_RED#Error while transfering %s to the online item's vault, please retry later.", "#LIGHT_RED#Error while transfering %s to the online item's vault, please retry later.", "logPlayer")
t("#CRIMSON#Server said: %s", "#CRIMSON#Server said: %s", "logPlayer")
t("#LIGHT_BLUE#You transfer %s to the offline item's vault.", "#LIGHT_BLUE#You transfer %s to the offline item's vault.", "logPlayer")
t("Teleporting object from the vault, please wait...", "Teleporting object from the vault, please wait...", "_t")
t("Transfer failed", "Transfer failed", "_t")
t([[This item comes from a previous version and would not work in your current game.
To prevent the universe from imploding the item was not transfered from the vault.]], [[This item comes from a previous version and would not work in your current game.
To prevent the universe from imploding the item was not transfered from the vault.]], "_t")
t("Item's Vault", "Item's Vault", "_t")
t("Checking item's vault list, please wait...", "Checking item's vault list, please wait...", "_t")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVault.lua"


-- new text
--[==[
t("Item's Vault", "Item's Vault", "_t")
t("Impossible to contact the server, please wait a few minutes and try again.", "Impossible to contact the server, please wait a few minutes and try again.", "_t")
t("Item's Vault (%d/%d)", "Item's Vault (%d/%d)", "tformat")
t([[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], [[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], "_t")
t("Name", "Name", "_t")
t("Usable", "Usable", "_t")
t("#LIGHT_GREEN#Yes", "#LIGHT_GREEN#Yes", "_t")
t("#LIGHT_RED#In less than one minute", "#LIGHT_RED#In less than one minute", "_t")
t("#LIGHT_RED#In %d minutes", "#LIGHT_RED#In %d minutes", "tformat")
t("Cooldown", "Cooldown", "_t")
t("This item has been placed recently in the vault, you must wait a bit before removing it.", "This item has been placed recently in the vault, you must wait a bit before removing it.", "_t")
t("#LIGHT_BLUE#You transfer %s from the online item's vault.", "#LIGHT_BLUE#You transfer %s from the online item's vault.", "log")
t("#LIGHT_RED#Error while transfering from the online item's vault, please retry later.", "#LIGHT_RED#Error while transfering from the online item's vault, please retry later.", "log")
--]==]


------------------------------------------------
section "tome-items-vault/overload/mod/dialogs/ItemsVaultOffline.lua"


-- new text
--[==[
t("Item's Vault", "Item's Vault", "_t")
t("Impossible to contact the server, please wait a few minutes and try again.", "Impossible to contact the server, please wait a few minutes and try again.", "_t")
t("Item's Vault (%d/%d)", "Item's Vault (%d/%d)", "tformat")
t([[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], [[Retrieve an item from the vault. When you place an item in the vault the paradox energies around it are so powerful you must wait one hour before retrieving it.
	#CRIMSON#Warning: while you *can* retrieve items made with previous versions of the game, no guarantee is given that the universe (or your character) will not explode.]], "_t")
t("Name", "Name", "_t")
t("Usable", "Usable", "_t")
t("#LIGHT_GREEN#Yes", "#LIGHT_GREEN#Yes", "_t")
t("#LIGHT_RED#In less than one minute", "#LIGHT_RED#In less than one minute", "_t")
t("#LIGHT_RED#In %d minutes", "#LIGHT_RED#In %d minutes", "tformat")
t("Cooldown", "Cooldown", "_t")
t("This item has been placed recently in the vault, you must wait a bit before removing it.", "This item has been placed recently in the vault, you must wait a bit before removing it.", "_t")
t("#LIGHT_BLUE#You transfer %s from the offline item's vault.", "#LIGHT_BLUE#You transfer %s from the offline item's vault.", "log")
t("#LIGHT_RED#Error while transfering from the offline item's vault, please retry later.", "#LIGHT_RED#Error while transfering from the offline item's vault, please retry later.", "log")
--]==]


