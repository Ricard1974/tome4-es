local class = require "engine.class"
local Dialog = require "engine.ui.Dialog"
local I18N = require "engine.I18N"

-- Cargar traducciones (siempre)
pcall(I18N.loadLocale, I18N, "/data/locales/engine/es.lua")
pcall(I18N.loadLocale, I18N, "/data/locales/es.lua")

-- Registrar español en la lista de idiomas
class:bindHook("I18N:listLanguages", function(self, data)
	data.list[#data.list+1] = {name = "Español (Spanish)", locale="es"}
end)

-- Configurar primera ejecución
class:bindHook("ToME:load", function(self, data)
	firstrun_es = config.settings.firstrun_es
	if config.settings.locale == "es" then
		-- Activar español si ya está seleccionado
		I18N:setLocale("es")
		firstrun_es = false
	end
end)

-- Mostrar diálogo de bienvenida en la primera ejecución
class:bindHook("ToME:run", function(self, data)
	if firstrun_es ~= false then
		game:onTickEnd(function()
			local text = "#WHITE#Haz clic en #GOLD#Activar traducción#LAST# para configurar el idioma y reiniciar el módulo con los cambios aplicados.\n\n"
				.. "#AQUAMARINE#¿Quieres traducir también el menú principal? **RECOMENDADO**#LAST#\n\n"
				.. "     1. Ve a la carpeta #LIGHT_STEEL_BLUE#game/addons#LAST# del juego.\n"
				.. "     2. Abre el archivo #GOLD#tome-spanish.teaa#LAST# (como un .zip).\n"
				.. "     3. Copia el archivo #GOLD#boot-spanish.teaa#LAST# y pégalo en la carpeta #LIGHT_STEEL_BLUE#addons#LAST#.\n\n"
				.. "¡Listo! Ahora puedes seleccionar el idioma en el menú principal.\n\n"
				.. "#FIREBRICK#¿Dudas o sugerencias? https://github.com/Ricard1974/tome4-es#LAST#"

			local options = {
				{name="#GOLD#Activar traducción", val=1},
				{name="No mostrar de nuevo", val=2},
				{name="Copiar ruta de la carpeta de addons", val=3}
			}

			Dialog:listPopup("Bienvenido a la Traducción al Español", text,
				options, 550, 400,
				function(sel)
					if not sel then
						return
					end

					if sel.val == 1 then
						-- Activar traducción
						game:saveSettings("locale", 'locale = "es"\n')
						game:saveSettings("firstrun_es", "firstrun_es = false\n")
						I18N:setLocale("es")
						util.showMainMenu(false, nil, nil, __load_module, __player_name, false)

					elseif sel.val == 2 then
						-- No mostrar de nuevo
						game:saveSettings("firstrun_es", "firstrun_es = false\n")

					elseif sel.val == 3 then
						-- Copiar ruta de addons al clipboard
						local addon_path = fs.getRealPath("/addons")
						core.key.setClipboard(addon_path)
						Dialog:simplePopup(
							"¡Ruta copiada!",
							"Ruta de la carpeta addons copiada al portapapeles:\n" ..
							"#GOLD#" .. addon_path .. "#LAST#\n" ..
							"Pégala en el explorador de archivos."
						)
					end
				end
			)
		end)
	end
end)
