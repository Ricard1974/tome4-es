------------------------------------------------
section "tome-addon-dev/init.lua"


-- new text
--[==[
t("ToME Addon's Development Tools", "ToME Addon's Development Tools", "init.lua long_name")
t("Provides tools to develop and publish addons.", "Provides tools to develop and publish addons.", "init.lua description")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/ArrangeText.lua"


-- new text
--[==[
t([[[ERROR] format string error near '%s' of string %s
]], [[[ERROR] format string error near '%s' of string %s
]], "tformat")
t([[[WARNING]Mismatched tformat string:
        Source: %s %s
        Target: %s %s (args=%s)
]], [[[WARNING]Mismatched tformat string:
        Source: %s %s
        Target: %s %s (args=%s)
]], "log")
t([[[WARNING]Mismatched translation for %s(%s): 
Last occurance: %s (from section %s)
Current occurance: %s (from section %s)
]], [[[WARNING]Mismatched translation for %s(%s): 
Last occurance: %s (from section %s)
Current occurance: %s (from section %s)
]], "log")
t("Success", "Success", "_t")
t([[Translation text checked.
Logs written to %s]], [[Translation text checked.
Logs written to %s]], "tformat")
t("\
-- new text\
", "\
-- new text\
", "_t")
t("\
-- untranslated text\
", "\
-- untranslated text\
", "_t")
t("\
-- old translated text\
", "\
-- old translated text\
", "_t")
t([[Translation text rearranged.
Logs written to %s]], [[Translation text rearranged.
Logs written to %s]], "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/Extractor.lua"


-- new text
--[==[
t("Luafish parse error on file %s: %s", "Luafish parse error on file %s: %s", "log")
t("error reading file %s", "error reading file %s", "log")
t("Error writing file %s", "Error writing file %s", "log")
t("MD5 matched for part %s, skipped.", "MD5 matched for part %s, skipped.", "log")
t("Extracting text", "Extracting text", "_t")
t("Processing source code of %s", "Processing source code of %s", "tformat")
t("Success", "Success", "_t")
t("Translation text extracted.", "Translation text extracted.", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/overload/engine/i18nhelper/FSHelper.lua"


-- new text
--[==[
t("Error %s", "Error %s", "log")
t("Calculating MD5", "Calculating MD5", "_t")
t("Calculating MD5 for %s", "Calculating MD5 for %s", "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/AddonDeveloper.lua"


-- new text
--[==[
t("Addon Developer", "Addon Developer", "_t")
t([[- Your profile has been enabled for addon uploading, you can go to #{italic}##LIGHT_BLUE#https://te4.org/addons/tome#LAST##{normal}# and upload your addon.
]], [[- Your profile has been enabled for addon uploading, you can go to #{italic}##LIGHT_BLUE#https://te4.org/addons/tome#LAST##{normal}# and upload your addon.
]], "_t")
t("Archive for %s", "Archive for %s", "tformat")
t([[Addon archive created:
- Addon file: #LIGHT_GREEN#%s#LAST# in folder #{bold}#%s#{normal}#
- Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard)
%s
]], [[Addon archive created:
- Addon file: #LIGHT_GREEN#%s#LAST# in folder #{bold}#%s#{normal}#
- Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard)
%s
]], "_t")
t("Registering new addon", "Registering new addon", "_t")
t("Addon init.lua must contain a tags table, i.e: tags={'foo', 'bar'}", "Addon init.lua must contain a tags table, i.e: tags={'foo', 'bar'}", "_t")
t("Addon init.lua must contain a description field", "Addon init.lua must contain a description field", "_t")
t("Addon: %s", "Addon: %s", "tformat")
t("Addon #LIGHT_GREEN#%s#LAST# registered. You may now upload a version for it.", "Addon #LIGHT_GREEN#%s#LAST# registered. You may now upload a version for it.", "tformat")
t("Addon #LIGHT_RED#%s#LAST# not registered: %s", "Addon #LIGHT_RED#%s#LAST# not registered: %s", "tformat")
t("unknown reason", "unknown reason", "_t")
t("Uploading addon", "Uploading addon", "_t")
t("Addon #LIGHT_GREEN#%s#LAST# uploaded, players may now play with it!", "Addon #LIGHT_GREEN#%s#LAST# uploaded, players may now play with it!", "tformat")
t("Addon #LIGHT_RED#%s#LAST# not upload: %s", "Addon #LIGHT_RED#%s#LAST# not upload: %s", "tformat")
t("Connecting to server", "Connecting to server", "_t")
t("Steam Workshop: %s", "Steam Workshop: %s", "tformat")
t("Update error: %s", "Update error: %s", "tformat")
t("unknown", "unknown", "_t")
t("Uploading addon to Steam Workshop", "Uploading addon to Steam Workshop", "_t")
t("There was an error uploading the addon.", "There was an error uploading the addon.", "_t")
t([[Addon succesfully uploaded to the Workshop.
You need to accept Steam Workshop Agreement in your Steam Client before the addon is visible to the community.]], [[Addon succesfully uploaded to the Workshop.
You need to accept Steam Workshop Agreement in your Steam Client before the addon is visible to the community.]], "_t")
t("Go to Workshop", "Go to Workshop", "_t")
t("Later", "Later", "_t")
t("Addon succesfully uploaded to the Workshop.", "Addon succesfully uploaded to the Workshop.", "_t")
t("Uploading addon preview to Steam Workshop", "Uploading addon preview to Steam Workshop", "_t")
t("There was an error uploading the addon preview.", "There was an error uploading the addon preview.", "_t")
t("Addon update & preview succesfully uploaded to the Workshop.", "Addon update & preview succesfully uploaded to the Workshop.", "_t")
t("Addon update succesfully uploaded to the Workshop.", "Addon update succesfully uploaded to the Workshop.", "_t")
t("Choose an addon for MD5", "Choose an addon for MD5", "_t")
t("MD5 for %s", "MD5 for %s", "tformat")
t([[Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard).
However you should'nt need that anymore, you can upload your addon directly from here.]], [[Addon MD5: #LIGHT_BLUE#%s#LAST# (this was copied to your clipboard).
However you should'nt need that anymore, you can upload your addon directly from here.]], "tformat")
t("Choose an addon to archive", "Choose an addon to archive", "_t")
t("Choose an addon to register", "Choose an addon to register", "_t")
t("Choose an addon to publish", "Choose an addon to publish", "_t")
t("Name for this addon's release", "Name for this addon's release", "_t")
t("Name", "Name", "_t")
t("Choose an addon to publish to Steam Workshop (needs to have been published to te4.org first)", "Choose an addon to publish to Steam Workshop (needs to have been published to te4.org first)", "_t")
t("Addon preview", "Addon preview", "_t")
t([[Addons on Steam Workshop need a "preview" image for the listing.
The game has generated a default one, however it is best if you make a custom one and place it in the folder #LIGHT_GREEN#%s#LAST# named #LIGHT_BLUE#%s#LAST# (512x512 is a good size for it)
You can still upload now and place it later.]], [[Addons on Steam Workshop need a "preview" image for the listing.
The game has generated a default one, however it is best if you make a custom one and place it in the folder #LIGHT_GREEN#%s#LAST# named #LIGHT_BLUE#%s#LAST# (512x512 is a good size for it)
You can still upload now and place it later.]], "_t")
t("Upload now", "Upload now", "_t")
t("Wait", "Wait", "_t")
t("Generate Addon's MD5", "Generate Addon's MD5", "_t")
t("Register new Addon", "Register new Addon", "_t")
t("Publish Addon to te4.org", "Publish Addon to te4.org", "_t")
t("Publish Addon to Steam Workshop", "Publish Addon to Steam Workshop", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ChooseTranslationParts.lua"


-- new text
--[==[
t("DEBUG -- Choose game parts", "DEBUG -- Choose game parts", "_t")
t([[Choose game parts you want to translated.
Unchecked parts will not be scanned, rearranged or released.
Your configuration will be lost after closing the game.
]], [[Choose game parts you want to translated.
Unchecked parts will not be scanned, rearranged or released.
Your configuration will be lost after closing the game.
]], "_t")
t("Checked", "Checked", "_t")
t("Short name", "Short name", "_t")
t("Long Name", "Long Name", "_t")
t("Flip All", "Flip All", "_t")
t("Finish", "Finish", "_t")
t("enabled", "enabled", "_t")
t("disabled", "disabled", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/DebugMain.lua"


-- new text
--[==[
t("Addon Developer", "Addon Developer", "_t")
t("Translation Tool", "Translation Tool", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ExampleAddonMaker.lua"


-- new text
--[==[
t("DEBUG -- Create Translation Addon", "DEBUG -- Create Translation Addon", "_t")
t("", "", "_t")
t("#LIGHT_GREEN#Locale Code:#LAST# ", "#LIGHT_GREEN#Locale Code:#LAST# ", "_t")
t("#LIGHT_GREEN#Language Name:#LAST# ", "#LIGHT_GREEN#Language Name:#LAST# ", "_t")
t("Finish", "Finish", "_t")
t("Cancel", "Cancel", "_t")
t("Failure", "Failure", "_t")
t("Addon %s already exists", "Addon %s already exists", "tformat")
t([[Fail when copying file to /addons/%s:
%s]], [[Fail when copying file to /addons/%s:
%s]], "tformat")
t([[Addon %s successfully created
Newly created addon is stored in %s]], [[Addon %s successfully created
Newly created addon is stored in %s]], "tformat")
t("Success", "Success", "_t")
t("\
ToME4 is about to relaunch and change locale to %s, proceed?", "\
ToME4 is about to relaunch and change locale to %s, proceed?", "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/ReleaseTranslation.lua"


-- new text
--[==[
t("Choose addon", "Choose addon", "_t")
t("Choose the addon you want to copy translation file to.", "Choose the addon you want to copy translation file to.", "_t")
t("Failure", "Failure", "_t")
t([[Fail when copying file to %s:
%s]], [[Fail when copying file to %s:
%s]], "tformat")
t("Success", "Success", "_t")
t([[Translation text copied to %s
Logs written to %s]], [[Translation text copied to %s
Logs written to %s]], "tformat")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TalentFinder.lua"


-- new text
--[==[
t("Search: ", "Search: ", "_t")
--]==]


------------------------------------------------
section "tome-addon-dev/superload/mod/dialogs/debug/TranslationTool.lua"


-- new text
--[==[
t("Translation Toolkit", "Translation Toolkit", "_t")
t("Change locale", "Change locale", "_t")
t("Enter locale code", "Enter locale code", "_t")
t("Change working locale (current: %s)", "Change working locale (current: %s)", "tformat")
t("Create translation addon", "Create translation addon", "_t")
t("Extract text index", "Extract text index", "_t")
t("Rearrange translation files", "Rearrange translation files", "_t")
t("Check translation files", "Check translation files", "_t")
t("Release translation as addon", "Release translation as addon", "_t")
t("Choose which part to translate", "Choose which part to translate", "_t")
--]==]


