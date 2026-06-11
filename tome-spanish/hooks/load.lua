local class = require "engine.class"
local Dialog = require "engine.ui.Dialog"

-- Registrar español en la lista de idiomas
class:bindHook("I18N:listLanguages", function(self, data)
	data.list[#data.list+1] = {name = "Español (Spanish)", locale="es"}
end)

-- Activar español cuando el módulo esté completamente cargado
class:bindHook("ToME:load", function()
	local I18N = require "engine.I18N"
	
	-- Cargar traducciones
	pcall(I18N.loadLocale, I18N, "/data-spanish/locales/engine/es.lua")
	pcall(I18N.loadLocale, I18N, "/data-spanish/locales/es.lua")
	
	-- Activar español
	I18N:setLocale("es")
	
	-- Forzar recarga de diálogos cacheados
	package.loaded["engine.dialogs.GameMenu"] = nil
	package.loaded["engine.dialogs.LanguageSelect"] = nil
	
	print("[ToME4-es] Traducciones cargadas y español activado")
end)

-- Mostrar diálogo informativo solo la primera vez
class:bindHook("ToME:run", function(self, data)
	if config.settings.firstrun_es ~= false then
		game:onTickEnd(function()
			game:saveSettings("firstrun_es", "firstrun_es = false\n")
			Dialog:simplePopup(
				"Traducción al Español Activada",
				"#GOLD#¡El español está activado!#LAST#\n\n"
				.. "Para traducir también el menú principal:\n"
				.. "1. Abre #LIGHT_STEEL_BLUE#tome-spanish.teaa#LAST# como un .zip\n"
				.. "2. Extrae #GOLD#boot-spanish.teaa#LAST# a #LIGHT_STEEL_BLUE#game/addons/#LAST#\n"
				.. "3. Selecciona español en Options → Language"
			)
		end)
	end
end)
