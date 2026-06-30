local class = require "engine.class"
local Dialog = require "engine.ui.Dialog"

-- Registrar español en la lista de idiomas
class:bindHook("I18N:listLanguages", function(self, data)
	data.list[#data.list+1] = {name = "Español (Spanish)", locale="es"}
end)

-- Activar español cuando el módulo esté completamente cargado
class:bindHook("ToME:load", function()
	local ok, I18N = pcall(require, "engine.I18N")
	if not ok or not I18N then
		print("[ToME4-es] ERROR: No se pudo cargar engine.I18N")
		return
	end
	
	-- Cargar traducciones (pcall para no crashear si fallan)
	local ok1 = pcall(I18N.loadLocale, I18N, "/data-spanish/locales/engine/es.lua")
	local ok2 = pcall(I18N.loadLocale, I18N, "/data-spanish/locales/es.lua")
	
	if ok1 or ok2 then
		-- Solo activar si al menos una traduccion se cargo
		pcall(I18N.setLocale, I18N, "es")
		print("[ToME4-es] Traducciones cargadas y español activado")
	else
		print("[ToME4-es] ERROR: No se pudieron cargar las traducciones")
	end
end)

-- Traducir contenido de lore/scrolls (el texto, no solo los titulos)
class:bindHook("ToME:run", function(self, data)
	-- NOTA: esto se ejecuta DESPUES de que todas las traducciones se hayan cargado
	-- y el locale "es" ya esta activo. Gettext estara disponible como _() o _t()
	
	-- Determinar funcion de traduccion disponible
	local T = type(_) == "function" and _ or (type(_t) == "function" and _t) or nil
	
	-- Si no hay funcion _(), intentar obtener I18N directamente
	if not T then
		local ok, I18N = pcall(require, "engine.I18N")
		if ok and I18N then
			T = function(text) return I18N.gettext(I18N, text) end
		else
			print("[ToME4-es] ERROR: No se puede traducir lore - I18N no disponible")
			return
		end
	end
	
	-- Traducir textos de lore en game.lore_db (textos de scrolls, libros, etc.)
	if game and game.lore_db then
		local count = 0
		for id, lore in pairs(game.lore_db) do
			if lore.text and type(lore.text) == "string" then
				local translated = T(lore.text)
				if translated and translated ~= lore.text then
					lore.text = translated
					count = count + 1
				end
			end
		end
		if count > 0 then
			print("[ToME4-es] " .. count .. " textos de lore traducidos")
		end
	end
	
	-- Traducir textos de dialogos de eventos especiales
	if game and game.dialog_db then
		local count = 0
		for id, dialog in pairs(game.dialog_db) do
			if dialog.text and type(dialog.text) == "string" then
				local translated = T(dialog.text)
				if translated and translated ~= dialog.text then
					dialog.text = translated
					count = count + 1
				end
			end
		end
		if count > 0 then
			print("[ToME4-es] " .. count .. " textos de dialogo traducidos")
		end
	end
	
	-- Mostrar diálogo informativo solo la primera vez
	if not game or not config or not config.settings then
		return
	end
	
	if config.settings.firstrun_es ~= false then
		game:onTickEnd(function()
			if game.saveSettings then
				game:saveSettings("firstrun_es", "firstrun_es = false\n")
			end
			if Dialog and Dialog.simplePopup then
				Dialog:simplePopup(
					"Traduccion al Espanol Activada",
					"#GOLD#El espanol esta activado!#LAST#\n\n"
					.. "Para traducir tambien el menu principal:\n"
					.. "1. Abre #LIGHT_STEEL_BLUE#tome-spanish.teaa#LAST# como un .zip\n"
					.. "2. Extrae #GOLD#boot-spanish.teaa#LAST# a #LIGHT_STEEL_BLUE#game/addons/#LAST#\n"
					.. "3. Selecciona espanol en Options -> Language"
				)
			end
		end)
	end
end)
