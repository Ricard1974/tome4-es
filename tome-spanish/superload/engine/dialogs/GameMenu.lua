local _M = loadPrevious(...)

-- Si loadPrevious falla, devolver tabla vacia para evitar crash
if not _M then
	return {}
end

if _M.generateList then
	local old_gen = _M.generateList
	_M.generateList = function(self, actions)
		old_gen(self, actions)
		-- Replace English strings with Spanish
		for _, item in ipairs(self.list) do
			if item[1] == "Resume" then item[1] = "Reanudar"
			elseif item[1] == "Language" then item[1] = "Idioma"
			elseif item[1] == "Key Bindings" then item[1] = "Asignación de teclas"
			elseif item[1] == "Video Options" then item[1] = "Opciones de vídeo"
			elseif item[1] == "Display Resolution" then item[1] = "Resolución de pantalla"
			elseif item[1] == "Show Achievements" then item[1] = "Mostrar logros"
			elseif item[1] == "Audio Options" then item[1] = "Opciones de audio"
			elseif item[1] == "Developer Mode" then item[1] = "Modo desarrollador"
			elseif item[1] == "Save Game" then item[1] = "Guardar partida"
			elseif item[1] == "Main Menu" then item[1] = "Menú principal"
			elseif item[1] == "Exit Game" then item[1] = "Salir del juego"
			end
		end
	end
end

return _M
