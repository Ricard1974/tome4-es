-- Carga las traducciones al español para ToME4
-- Spanish translation loader for ToME4
-- Se ejecuta al cargar el addon

local locale = "es"

-- Cargar las traducciones del módulo principal
local function loadMainLocale()
	local path = "/data/locales/" .. locale .. ".lua"
	local ok, err = dofile(path)
	if not ok then
		print("[ToME4-es] Error cargando " .. path .. ": " .. tostring(err))
	end
end

-- Cargar las traducciones del engine
local function loadEngineLocale()
	local path = "/data/locales/engine/" .. locale .. ".lua"
	local ok, err = dofile(path)
	if not ok then
		print("[ToME4-es] Error cargando " .. path .. ": " .. tostring(err))
	end
end

-- Hook para cargar las traducciones al inicio del juego
class:bindHook("ToME:load", function()
	loadEngineLocale()
	loadMainLocale()
	print("[ToME4-es] Traducciones al español cargadas")
end)
