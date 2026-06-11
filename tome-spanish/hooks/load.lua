local class = require "engine.class"

-- Carga las traducciones al español para ToME4
-- Spanish translation addon for ToME4

-- Registrar español en la lista de idiomas
class:bindHook("I18N:listLanguages", function(self, data)
	local list = data.list
	local found = false
	for _, item in ipairs(list) do
		if item.locale == "es" then
			found = true
			break
		end
	end
	if not found then
		list[#list+1] = {name = "Español (Spanish)", locale="es"}
	end
end)

-- Cargar locales al iniciar el módulo
class:bindHook("ToME:load", function()
	-- Intentar cargar engine locale
	local ok, err = pcall(dofile, "/data/locales/engine/es.lua")
	if ok then
		print("[ToME4-es] Engine locales loaded")
	end

	-- Intentar cargar módulo locale
	ok, err = pcall(dofile, "/data/locales/es.lua")
	if ok then
		print("[ToME4-es] Module locales loaded")
	end
end)
