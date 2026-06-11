local class = require "engine.class"

class:bindHook("I18N:listLanguages", function(self, data)
	data.list[#data.list+1] = {name = "Español (Spanish)", locale="es"}
end)
