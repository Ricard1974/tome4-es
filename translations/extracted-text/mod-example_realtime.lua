------------------------------------------------
section "mod-example_realtime/class/Actor.lua"

tDef(161, "You do not have enough power to activate %s.", "logPlayer", true) -- 
tDef(166, "You do not have enough power to cast %s.", "logPlayer", true) -- 
tDef(175, "%s", "logSeen", true) -- 
tDef(178, "%s activates %s.", "logSeen", true) -- 
tDef(180, "%s deactivates %s.", "logSeen", true) -- 
tDef(182, "%s uses %s.", "logSeen", true) -- 


------------------------------------------------
section "mod-example_realtime/class/Game.lua"

tDef(322, "There is no way out of this level here.", "log", true) -- 
tDef(427, "Saving game...", "log", true) -- 


------------------------------------------------
section "mod-example_realtime/class/Grid.lua"



------------------------------------------------
section "mod-example_realtime/class/NPC.lua"



------------------------------------------------
section "mod-example_realtime/class/Player.lua"

tDef(99, "taken damage", "_t", true) -- 
tDef(104, "LOW HEALTH!", "_t", true) -- 
tDef(131, "#00ff00#Talent %s is ready to use.", "log", true) -- 
tDef(138, "LEVEL UP!", "_t", true) -- 
tDef(139, "#00ffff#Welcome to level %d.", "log", true) -- 


------------------------------------------------
section "mod-example_realtime/class/interface/Combat.lua"



------------------------------------------------
section "mod-example_realtime/data/birth/descriptors.lua"

tDef(21, "base", "birth descriptor name", true) -- 
tDef(35, "Destroyer", "birth descriptor name", true) -- 
tDef(47, "Acid-maniac", "birth descriptor name", true) -- 


------------------------------------------------
section "mod-example_realtime/data/damage_types.lua"

tDef(27, "%s hits %s for %s%0.2f %s damage#LAST#.", "logSeen", true) -- 
tDef(31, "Kill!", "_t", true) -- 


------------------------------------------------
section "mod-example_realtime/data/general/grids/basic.lua"

tDef(21, "exit to the wilds", "entity name", true) -- 
tDef(31, "previous level", "entity name", true) -- 
tDef(40, "next level", "entity name", true) -- 
tDef(49, "floor", "entity name", true) -- 
tDef(55, "wall", "entity name", true) -- 
tDef(67, "door", "entity name", true) -- 
tDef(78, "open door", "entity name", true) -- 


------------------------------------------------
section "mod-example_realtime/data/general/npcs/kobold.lua"

tDef(24, "humanoid", "entity type", true) -- 
tDef(24, "kobold", "entity subtype", true) -- 
tDef(26, "Ugly and green!", "_t", true) -- 
tDef(34, "kobold warrior", "entity name", true) -- 
tDef(42, "armoured kobold warrior", "entity name", true) -- 


------------------------------------------------
section "mod-example_realtime/data/gfx/particles/acid.lua"



------------------------------------------------
section "mod-example_realtime/data/rooms/pilar.lua"



------------------------------------------------
section "mod-example_realtime/data/rooms/simple.lua"



------------------------------------------------
section "mod-example_realtime/data/talents.lua"

tDef(19, "role", "talent category", true) -- 
tDef(22, "Kick", "talent name", true) -- 
tDef(43, "Acid Spray", "talent name", true) -- 


------------------------------------------------
section "mod-example_realtime/data/timed_effects.lua"



------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/grids.lua"



------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/npcs.lua"



------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/objects.lua"



------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/traps.lua"



------------------------------------------------
section "mod-example_realtime/data/zones/dungeon/zone.lua"

tDef(21, "Old ruins", "_t", true) -- 


------------------------------------------------
section "mod-example_realtime/dialogs/DeathDialog.lua"

tDef(31, "Death!", "_t", true) -- 
tDef(115, "#LIGHT_BLUE#You resurrect! CHEATER !", "logPlayer", true) -- 


------------------------------------------------
section "mod-example_realtime/dialogs/Quit.lua"

tDef(26, "Really exit Example Module?", "_t", true) -- 


------------------------------------------------
section "mod-example_realtime/init.lua"

tDef(21, "Realtime Example Module for T-Engine4", "init.lua long_name", true) -- 
tDef(27, "This is *NOT* a game, just an example/template to make your own using the T-Engine4.\
", "init.lua description", true) -- 


------------------------------------------------
section "mod-example_realtime/load.lua"

tDef(47, "Strength", "stat name", true) -- 
tDef(47, "str", "stat short_name", true) -- 
tDef(48, "Dexterity", "stat name", true) -- 
tDef(48, "dex", "stat short_name", true) -- 
tDef(49, "Constitution", "stat name", true) -- 
tDef(49, "con", "stat short_name", true) -- 


