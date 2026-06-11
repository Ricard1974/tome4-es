import os
import re
def copy_file(locale, part, path):
    if part == "engine":
        path = path + "/data/locales/engine/" + locale + ".lua"
    else:
        path = path + "/data/locales/" + locale + ".lua"
    try:
        os.makedirs(re.sub(r"[^\\/]+\.[^\\/]+$", "", path), True)
    except FileExistsError:
        pass
    fo = open(path, "w", encoding="utf-8")
    fo.write('locale "' + locale + '"\n')
    if os.path.exists(part + ".copy.lua"):
        f = open(part + ".copy.lua", "r", encoding="utf-8")
        fo.write(f.read())
    if os.path.exists(part + ".lua"):
        f = open(part + ".lua", "r", encoding="utf-8")
        fo.write(f.read())
    fo.close()

copy_file("es", "tome-items-vault", "subdir:/|/tmp/t-engine4-linux64-1.7.6/game/addons/tome-items-vault.teaa")
copy_file("es", "mod-boot", "/tmp/t-engine4-linux64-1.7.6/game/modules/boot-te4-1.7.6.team")
copy_file("es", "mod-tome", "/tmp/t-engine4-linux64-1.7.6/game/modules/tome-1.7.6.team")
copy_file("es", "engine", "/tmp/t-engine4-linux64-1.7.6/game/engines/te4-1.7.6.teae")
copy_file("es", "mod-example_realtime", "/tmp/t-engine4-linux64-1.7.6/game/modules/example_realtime")
copy_file("es", "tome-remote-designer", "subdir:/|/tmp/t-engine4-linux64-1.7.6/game/addons/tome-remote-designer.teaa")
copy_file("es", "mod-example", "/tmp/t-engine4-linux64-1.7.6/game/modules/example")
copy_file("es", "tome-addon-dev", "subdir:/|/tmp/t-engine4-linux64-1.7.6/game/addons/tome-addon-dev.teaa")
