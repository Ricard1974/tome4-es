------------------------------------------------
section "tome-addon-dev/hooks/load.lua"



------------------------------------------------
section "tome-addon-dev/init.lua"

tDef(20, "ToME Addon's Development Tools", "init.lua long_name", true) -- 
tDef(27, "Provides tools to develop and publish addons.", "init.lua description", true) -- 


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/ArrangeText.lua"

tDef(153, "[ERROR] format string error near '%s' of string %s\
", "tformat", true) -- 
tDef(204, "[WARNING]Mismatched tformat string:\
        Source: %s %s\
        Target: %s %s (args=%s)\
", "log", true) -- 
tDef(218, "[WARNING]Mismatched translation for %s(%s): \
Last occurance: %s (from section %s)\
Current occurance: %s (from section %s)\
", "log", true) -- 
tDef(323, "Success", "_t", true) -- 
tDef(323, "Translation text checked.\
Logs written to %s", "tformat", true) -- 
tDef(384, "\
-- new text\
", "_t", true) -- 
tDef(390, "\
-- untranslated text\
", "_t", true) -- 
tDef(396, "\
-- old translated text\
", "_t", true) -- 
tDef(418, "Translation text rearranged.\
Logs written to %s", "tformat", true) -- 


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/Extractor.lua"

tDef(356, "Luafish parse error on file %s: %s", "log", true) -- 
tDef(373, "error reading file %s", "log", true) -- 
tDef(397, "Error writing file %s", "log", true) -- 
tDef(410, "MD5 matched for part %s, skipped.", "log", true) -- 
tDef(420, "Extracting text", "_t", true) -- 
tDef(420, "Processing source code of %s", "tformat", true) -- 
tDef(446, "Success", "_t", true) -- 
tDef(446, "Translation text extracted.", "_t", true) -- 


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/FSHelper.lua"

tDef(149, "Error %s", "log", true) -- 
tDef(162, "Calculating MD5", "_t", true) -- 
tDef(162, "Calculating MD5 for %s", "tformat", true) -- 


------------------------------------------------
section "tome-addon-dev/overload/luafish/lua2c.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/macro.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/math.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/parser.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/run.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/serializer.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/staticmodule.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/string.lua"



------------------------------------------------
section "tome-addon-dev/overload/luafish/type.lua"



------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/AddonDeveloper.lua"

tDef(28, "Addon Developer", "_t", true) -- 
tDef(101, "- Your profile has been enabled for addon uploading, you can go to #{italic}##LIGHT_BLUE#https://te4.org/addons/tome#LAST##{normal}# and upload your addon.\
", "_t", true) -- 
tDef(110, "Archive for %s", "tformat", true) -- 
tDef(110, "Addon archive created:\
- Addon file: #LIGHT_GREEN#%s#LAST# in folder #{bold}#%s#{normal}#\
- Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard)\
%s\
", "_t", true) -- 
tDef(122, "Registering new addon", "_t", true) -- 
tDef(122, "Addon init.lua must contain a tags table, i.e: tags={'foo', 'bar'}", "_t", true) -- 
tDef(126, "Addon init.lua must contain a description field", "_t", true) -- 
tDef(139, "Addon: %s", "tformat", true) -- 
tDef(146, "Addon #LIGHT_GREEN#%s#LAST# registered. You may now upload a version for it.", "tformat", true) -- 
tDef(148, "Addon #LIGHT_RED#%s#LAST# not registered: %s", "tformat", true) -- 
tDef(148, "unknown reason", "_t", true) -- 
tDef(175, "Uploading addon", "_t", true) -- 
tDef(189, "Addon #LIGHT_GREEN#%s#LAST# uploaded, players may now play with it!", "tformat", true) -- 
tDef(191, "Addon #LIGHT_RED#%s#LAST# not upload: %s", "tformat", true) -- 
tDef(245, "Connecting to server", "_t", true) -- 
tDef(252, "Steam Workshop: %s", "tformat", true) -- 
tDef(252, "Update error: %s", "tformat", true) -- 
tDef(252, "unknown", "_t", true) -- 
tDef(256, "Uploading addon to Steam Workshop", "_t", true) -- 
tDef(267, "There was an error uploading the addon.", "_t", true) -- 
tDef(269, "Addon succesfully uploaded to the Workshop.\
You need to accept Steam Workshop Agreement in your Steam Client before the addon is visible to the community.", "_t", true) -- 
tDef(271, "Go to Workshop", "_t", true) -- 
tDef(271, "Later", "_t", true) -- 
tDef(272, "Addon succesfully uploaded to the Workshop.", "_t", true) -- 
tDef(279, "Uploading addon preview to Steam Workshop", "_t", true) -- 
tDef(282, "There was an error uploading the addon preview.", "_t", true) -- 
tDef(283, "Addon update & preview succesfully uploaded to the Workshop.", "_t", true) -- 
tDef(288, "Addon update succesfully uploaded to the Workshop.", "_t", true) -- 
tDef(308, "Choose an addon for MD5", "_t", true) -- 
tDef(311, "MD5 for %s", "tformat", true) -- 
tDef(311, "Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard).\
However you should'nt need that anymore, you can upload your addon directly from here.", "tformat", true) -- 
tDef(314, "Choose an addon to archive", "_t", true) -- 
tDef(318, "Choose an addon to register", "_t", true) -- 
tDef(322, "Choose an addon to publish", "_t", true) -- 
tDef(323, "Name for this addon's release", "_t", true) -- 
tDef(323, "Name", "_t", true) -- 
tDef(331, "Choose an addon to publish to Steam Workshop (needs to have been published to te4.org first)", "_t", true) -- 
tDef(334, "Addon preview", "_t", true) -- 
tDef(334, "Addons on Steam Workshop need a \"preview\" image for the listing.\
The game has generated a default one, however it is best if you make a custom one and place it in the folder #LIGHT_GREEN#%s#LAST# named #LIGHT_BLUE#%s#LAST# (512x512 is a good size for it)\
You can still upload now and place it later.", "_t", true) -- 
tDef(338, "Upload now", "_t", true) -- 
tDef(338, "Wait", "_t", true) -- 
tDef(348, "Generate Addon's MD5", "_t", true) -- 
tDef(351, "Register new Addon", "_t", true) -- 
tDef(352, "Publish Addon to te4.org", "_t", true) -- 
tDef(353, "Publish Addon to Steam Workshop", "_t", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ChooseTranslationParts.lua"

tDef(31, "DEBUG -- Choose game parts", "_t", true) -- 
tDef(34, "Choose game parts you want to translated.\
Unchecked parts will not be scanned, rearranged or released.\
Your configuration will be lost after closing the game.\
", "_t", true) -- 
tDef(50, "Checked", "_t", true) -- 
tDef(51, "Short name", "_t", true) -- 
tDef(52, "Long Name", "_t", true) -- 
tDef(59, "Flip All", "_t", true) -- 
tDef(60, "Finish", "_t", true) -- 
tDef(78, "enabled", "_t", true) -- 
tDef(78, "disabled", "_t", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/DebugMain.lua"

tDef(22, "Addon Developer", "_t", true) -- 
tDef(23, "Translation Tool", "_t", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ExampleAddonMaker.lua"

tDef(28, "DEBUG -- Create Translation Addon", "_t", true) -- 
tDef(31, "", "_t", true) -- 
tDef(35, "#LIGHT_GREEN#Locale Code:#LAST# ", "_t", true) -- 
tDef(41, "#LIGHT_GREEN#Language Name:#LAST# ", "_t", true) -- 
tDef(46, "Finish", "_t", true) -- 
tDef(47, "Cancel", "_t", true) -- 
tDef(92, "Failure", "_t", true) -- 
tDef(92, "Addon %s already exists", "tformat", true) -- 
tDef(104, "Fail when copying file to /addons/%s:\
%s", "tformat", true) -- 
tDef(118, "Addon %s successfully created\
Newly created addon is stored in %s", "tformat", true) -- 
tDef(120, "Success", "_t", true) -- 
tDef(122, "\
ToME4 is about to relaunch and change locale to %s, proceed?", "tformat", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/NPCDesign.lua"



------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ReleaseTranslation.lua"

tDef(30, "Choose addon", "_t", true) -- 
tDef(32, "Choose the addon you want to copy translation file to.", "_t", true) -- 
tDef(49, "Failure", "_t", true) -- 
tDef(49, "Fail when copying file to %s:\
%s", "tformat", true) -- 
tDef(74, "Success", "_t", true) -- 
tDef(74, "Translation text copied to %s\
Logs written to %s", "tformat", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TalentFinder.lua"

tDef(34, "Search: ", "_t", true) -- 


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TranslationTool.lua"

tDef(31, "Translation Toolkit", "_t", true) -- 
tDef(63, "Change locale", "_t", true) -- 
tDef(63, "Enter locale code", "_t", true) -- 
tDef(81, "Change working locale (current: %s)", "tformat", true) -- 
tDef(82, "Create translation addon", "_t", true) -- 
tDef(83, "Extract text index", "_t", true) -- 
tDef(84, "Rearrange translation files", "_t", true) -- 
tDef(85, "Check translation files", "_t", true) -- 
tDef(86, "Release translation as addon", "_t", true) -- 
tDef(87, "Choose which part to translate", "_t", true) -- 


