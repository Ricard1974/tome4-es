local class = require "engine.class"

class:bindHook("ToME:load", function()
	local I18N = require "engine.I18N"
	
	-- Cargar traducciones
	pcall(I18N.loadLocale, I18N, "/data/locales/engine/es.lua")
	pcall(I18N.loadLocale, I18N, "/data/locales/es.lua")
	
	-- Activar español
	I18N:setLocale("es")
	
	-- Modificar el diálogo de idiomas YA cacheado para añadir español
	local LS = package.loaded["engine.dialogs.LanguageSelect"]
	if LS then
		local old_gen = LS.generateList
		LS.generateList = function(self, ...)
			old_gen(self, ...)
			-- Añadir español si no está
			local found = false
			for _, item in ipairs(self.list) do
				if item.locale == "es" then
					found = true
					break
				end
			end
			if not found then
				self.list[#self.list+1] = {name = "Español (Spanish)", locale="es"}
			end
		end
	end
	
	print("[ToME4-es] Listo")
end)
