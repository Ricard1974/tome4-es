------------------------------------------------
section "mod-example_realtime/class/Actor.lua"


-- new text
--[==[
t("You do not have enough power to activate %s.", "You do not have enough power to activate %s.", "logPlayer")
t("You do not have enough power to cast %s.", "You do not have enough power to cast %s.", "logPlayer")
t("%s", "%s", "logSeen")
t("%s activates %s.", "%s activates %s.", "logSeen")
t("%s deactivates %s.", "%s deactivates %s.", "logSeen")
t("%s uses %s.", "%s uses %s.", "logSeen")
--]==]


------------------------------------------------
section "mod-example_realtime/class/Game.lua"


-- new text
--[==[
t("There is no way out of this level here.", "There is no way out of this level here.", "log")
t("Saving game...", "Saving game...", "log")
--]==]


------------------------------------------------
section "mod-example_realtime/class/Player.lua"


-- new text
--[==[
t("taken damage", "taken damage", "_t")
t("LOW HEALTH!", "LOW HEALTH!", "_t")
t("#00ff00#Talent %s is ready to use.", "#00ff00#Talent %s is ready to use.", "log")
t("LEVEL UP!", "LEVEL UP!", "_t")
t("#00ffff#Welcome to level %d.", "#00ffff#Welcome to level %d.", "log")
--]==]


------------------------------------------------
section "mod-example_realtime/data/birth/descriptors.lua"


-- new text
--[==[
t("base", "base", "birth descriptor name")
t("Destroyer", "Destroyer", "birth descriptor name")
t("Acid-maniac", "Acid-maniac", "birth descriptor name")
--]==]


------------------------------------------------
section "mod-example_realtime/data/damage_types.lua"


-- new text
--[==[
t("%s hits %s for %s%0.2f %s damage#LAST#.", "%s hits %s for %s%0.2f %s damage#LAST#.", "logSeen")
t("Kill!", "Kill!", "_t")
--]==]


------------------------------------------------
section "mod-example_realtime/data/general/grids/basic.lua"


-- new text
--[==[
t("exit to the wilds", "exit to the wilds", "entity name")
t("previous level", "previous level", "entity name")
t("next level", "next level", "entity name")
t("floor", "floor", "entity name")
t("wall", "wall", "entity name")
t("door", "door", "entity name")
t("open door", "open door", "entity name")
--]==]


------------------------------------------------
section "mod-example_realtime/data/general/npcs/kobold.lua"


-- new text
--[==[
t("humanoid", "humanoid", "entity type")
t("kobold", "kobold", "entity subtype")
t("Ugly and green!", "Ugly and green!", "_t")
t("kobold warrior", "kobold warrior", "entity name")
t("armoured kobold warrior", "armoured kobold warrior", "entity name")
--]==]


------------------------------------------------
section "mod-example_realtime/data/talents.lua"


-- new text
--[==[
t("role", "role", "talent category")
t("Kick", "Kick", "talent name")
t("Acid Spray", "Acid Spray", "talent name")
--]==]


------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/zone.lua"


-- new text
--[==[
t("Old ruins", "Old ruins", "_t")
--]==]


------------------------------------------------
section "mod-example_realtime/dialogs/DeathDialog.lua"


-- new text
--[==[
t("Death!", "Death!", "_t")
t("#LIGHT_BLUE#You resurrect! CHEATER !", "#LIGHT_BLUE#You resurrect! CHEATER !", "logPlayer")
--]==]


------------------------------------------------
section "mod-example_realtime/dialogs/Quit.lua"


-- new text
--[==[
t("Really exit Example Module?", "Really exit Example Module?", "_t")
--]==]


------------------------------------------------
section "mod-example_realtime/init.lua"


-- new text
--[==[
t("Realtime Example Module for T-Engine4", "Realtime Example Module for T-Engine4", "init.lua long_name")
t([[This is *NOT* a game, just an example/template to make your own using the T-Engine4.
]], [[This is *NOT* a game, just an example/template to make your own using the T-Engine4.
]], "init.lua description")
--]==]


------------------------------------------------
section "mod-example_realtime/load.lua"


-- new text
--[==[
t("Strength", "Strength", "stat name")
t("str", "str", "stat short_name")
t("Dexterity", "Dexterity", "stat name")
t("dex", "dex", "stat short_name")
t("Constitution", "Constitution", "stat name")
t("con", "con", "stat short_name")
--]==]


