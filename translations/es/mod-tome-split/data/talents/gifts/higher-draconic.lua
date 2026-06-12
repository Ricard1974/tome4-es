-- mod-tome/data/talents/gifts/higher-draconic.lua
-- Total: 5 cadenas
-- Estado: ⏳ Pendiente
-- Ultima actualizacion: --
-- Traductor: --

t("Prismatic Slash", "Prismático Slash", "talent name")
t("Venomous Breath", "Venomous Aliento", "talent name")
t("@Source@ breathes venom!", "@Source@ respira veneno!", "_t")
t("Wyrmic Guile", "Wyrmic Guile", "talent name")
t("Chromatic Fury", "Chromatic Furia", "talent name")

t("Unleash raw, chaotic elemental damage upon your enemy.
\n\t\tYou strike your enemy for %d%% weapon damage in one of blinding sand, disarming acid, freezing and slowing ice, dazing lightning or stunning flames, with equal odds.
\n\t\tAdditionally, you will cause a burst that deals %0.2f of that damage to creatures in radius %d, regardless of if you hit with the blow.
\n\t\tLevels in Prismatic Slash increase your Physical and Mental attack speeds by %d%%.
\n
\n\t\tThis talent will also attack with your shield, if you have one equipped.", "Uneash crudo, caótico daño elemental sobre su enemigo.\nUsted golpea a su enemigo por daños de arma %d %% en una de arena cegadora, desarmar ácido, congelar y ralentizar el hielo, relámpagos o llamas impresionantes, con iguales probabilidades.\nAdemás, causarás una ráfaga que afecte a las criaturas en radius %d, independientemente de si golpeas con el golpe.\nLos niveles de choque prismático aumentan sus velocidades de ataque físico y mental por %d %%.\n\nEste talento también atacará con su escudo, si tiene uno equipado.", "tformat")
t("You breathe crippling poison in a frontal cone of radius %d. Any target caught in the area will take %0.2f nature damage each turn for 6 turns.
\n\t\tThe poison also gives enemies a %d%% chance to fail actions more complicated than basic attacks and movement, while it is in effect.
\n\t\tThe damage will increase with your Strength, and the critical chance is based on your Mental crit rate.
\n\t\tEach point in Venomous Breath also increases your nature resistance by 3%%, and your nature damage by 4%%.]] ):tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), effect)
\n\tend,
\n}
\n
\nnewTalent{
\n\tname = \"Wyrmic Guile\",
\n\ttype = {\"wild-gift/higher-draconic\", 3},
\n\trequire = gifts_req_high3,
\n\tpoints = 5,
\n\tmode = \"passive\",
\n\tresistKnockback = function(self, t) return self:combatTalentLimit(t, 1, .2, .5) end, -- Limit < 100%
\n\tresistBlindStun = function(self, t) return self:combatTalentLimit(t, 1, .1, .25) end, -- Limit < 100%
\n\tpassives = function(self, t, p)
\n\t\tself:talentTemporaryValue(p, \"knockback_immune\", t.resistKnockback(self, t))
\n\t\tself:talentTemporaryValue(p, \"stun_immune\", t.resistBlindStun(self, t))
\n\t\tself:talentTemporaryValue(p, \"blind_immune\", t.resistBlindStun(self, t))
\n\tend,
\n\tinfo = function(self, t)
\n\t\treturn ([[You have mastered your draconic nature.
\n\t\tYou gain %d%% knockback resistance, and your blindness and stun resistances are increased by %d%%.", "Respira veneno desgarrador en un cono frontal de %d radio. Cualquier objetivo atrapado en la zona tomará daño de la naturaleza %0.2f cada turno por 6 vueltas.\nEl veneno también da a los enemigos una %d %% oportunidad de fallar acciones más complicadas que los ataques y movimientos básicos, mientras que está en efecto.\nEl daño aumentará con su fuerza, y la probabilidad crítica se basa en su tasa de criminalidad mental.\nCada punto en el aliento venenoso también aumenta su resistencia a la naturaleza por 3%%, y su daño natural por 4%%.]]:tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), efecto)\nFin,\n}\n\nNewTalent{\nnombre = \"Guía Jurídica\",\ntipo = {\"gift-gift/higher-draconic\", 3},\nRequiere = regalos req high3,\npuntos = 5,\nmodo = \"pasivo\",\nresistKnockback = función (self, t) volverse a sí mismo:combatTalentLimit(t, 1, .2, .5) final, -- Limite\nresistBlindStun = función(self, t) volverse a sí mismo:combatTalentLimit(t, 1, .1, .25) final, -- Limite\npasivos = función(self, t, p)\nauto:talentoTemporaryValue(p, \"knockback immune\", t.resistKnockback(self, t)))\nauto:talentoTemporarioValue(p, \"stun immune\", t.resistBlindStun(self, t)))\nauto:talentoTemporarioValue(p, \"blind immune\", t.resistBlindStun(self, t)))\nFin,\ninfo = función(self, t)\nretorno ([Usted ha dominado su naturaleza dracónica.\nGanas resistencia a golpes %d %%, y tus cegueras y resistencias a aturdimientos se incrementan por %d %%.", "tformat")
t("Unleash raw, chaotic elemental damage upon your enemy.
\n\t\tYou strike your enemy for %d%% weapon damage in one of blinding sand, disarming acid, freezing and slowing ice, dazing lightning or stunning flames, with equal odds.
\n\t\tAdditionally, you will cause a burst that deals %0.2f of that damage to creatures in radius %d, regardless of if you hit with the blow.
\n\t\tLevels in Prismatic Slash increase your Physical and Mental attack speeds by %d%%.
\n
\n\t\tThis talent will also attack with your shield, if you have one equipped.", "Uneash crudo, caótico daño elemental sobre su enemigo.\nUsted golpea a su enemigo por daños de arma %d %% en una de arena cegadora, desarmar ácido, congelar y ralentizar el hielo, relámpagos o llamas impresionantes, con iguales probabilidades.\nAdemás, causarás una ráfaga que afecte a las criaturas en radius %d, independientemente de si golpeas con el golpe.\nLos niveles de choque prismático aumentan sus velocidades de ataque físico y mental por %d %%.\n\nEste talento también atacará con su escudo, si tiene uno equipado.", "tformat")
t("You breathe crippling poison in a frontal cone of radius %d. Any target caught in the area will take %0.2f nature damage each turn for 6 turns.
\n\t\tThe poison also gives enemies a %d%% chance to fail actions more complicated than basic attacks and movement, while it is in effect.
\n\t\tThe damage will increase with your Strength, and the critical chance is based on your Mental crit rate.
\n\t\tEach point in Venomous Breath also increases your nature resistance by 3%%, and your nature damage by 4%%.]] ):tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), effect)
\n\tend,
\n}
\n
\nnewTalent{
\n\tname = \"Wyrmic Guile\",
\n\ttype = {\"wild-gift/higher-draconic\", 3},
\n\trequire = gifts_req_high3,
\n\tpoints = 5,
\n\tmode = \"passive\",
\n\tresistKnockback = function(self, t) return self:combatTalentLimit(t, 1, .2, .5) end, -- Limit < 100%
\n\tresistBlindStun = function(self, t) return self:combatTalentLimit(t, 1, .1, .25) end, -- Limit < 100%
\n\tpassives = function(self, t, p)
\n\t\tself:talentTemporaryValue(p, \"knockback_immune\", t.resistKnockback(self, t))
\n\t\tself:talentTemporaryValue(p, \"stun_immune\", t.resistBlindStun(self, t))
\n\t\tself:talentTemporaryValue(p, \"blind_immune\", t.resistBlindStun(self, t))
\n\tend,
\n\tinfo = function(self, t)
\n\t\treturn ([[You have mastered your draconic nature.
\n\t\tYou gain %d%% knockback resistance, and your blindness and stun resistances are increased by %d%%.", "Respira veneno desgarrador en un cono frontal de %d radio. Cualquier objetivo atrapado en la zona tomará daño de la naturaleza %0.2f cada turno por 6 vueltas.\nEl veneno también da a los enemigos una %d %% oportunidad de fallar acciones más complicadas que los ataques y movimientos básicos, mientras que está en efecto.\nEl daño aumentará con su fuerza, y la probabilidad crítica se basa en su tasa de criminalidad mental.\nCada punto en el aliento venenoso también aumenta su resistencia a la naturaleza por 3%%, y su daño natural por 4%%.]]:tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), efecto)\nFin,\n}\n\nNewTalent{\nnombre = \"Guía Jurídica\",\ntipo = {\"gift-gift/higher-draconic\", 3},\nRequiere = regalos req high3,\npuntos = 5,\nmodo = \"pasivo\",\nresistKnockback = función (self, t) volverse a sí mismo:combatTalentLimit(t, 1, .2, .5) final, -- Limite\nresistBlindStun = función(self, t) volverse a sí mismo:combatTalentLimit(t, 1, .1, .25) final, -- Limite\npasivos = función(self, t, p)\nauto:talentoTemporaryValue(p, \"knockback immune\", t.resistKnockback(self, t)))\nauto:talentoTemporarioValue(p, \"stun immune\", t.resistBlindStun(self, t)))\nauto:talentoTemporarioValue(p, \"blind immune\", t.resistBlindStun(self, t)))\nFin,\ninfo = función(self, t)\nretorno ([Usted ha dominado su naturaleza dracónica.\nGanas resistencia a golpes %d %%, y tus cegueras y resistencias a aturdimientos se incrementan por %d %%.", "tformat")
t("You have gained the full power of the various drakes throughout the world, and have become both resistant and attuned to physical, fire, cold, lightning, acid, nature, blight, and darkness damage.
\n\t\tYour resistance to these elements is increased by %0.1f%% and all damage you deal with them is increased by %0.1f%% with %0.1f%% resistance penetration.
\n
\n\t\tLearning this talent will add a Willpower bonus to your breath talent damage with the same scaling as Strength, effectively doubling it when the stats are equal.", "Usted ha ganado el pleno poder de los diversos drakes en todo el mundo, y se han vuelto resistentes y atestados a los daños físicos, de fuego, fríos, relámpagos, ácido, naturaleza, luz y oscuridad.\nSu resistencia a estos elementos se incrementa por %0.1f %% y todo el daño que usted enfrenta con ellos se aumenta por %0.1f %% con la penetración de resistencia %0.1f %%.\n\nAprender este talento añadirá una bonificación de Willpower a su daño de talento respiratorio con el mismo escalado que Fuerza, duplicando eficazmente cuando las estadísticas son iguales.", "tformat")
t("Unleash raw, chaotic elemental damage upon your enemy.\n\t\tYou strike your enemy for %d%% weapon damage in one of blinding sand, disarming acid, freezing and slowing ice, dazing lightning or stunning flames, with equal odds.\n\t\tAdditionally, you will cause a burst that deals %0.2f of that damage to creatures in radius %d, regardless of if you hit with the blow.\n\t\tLevels in Prismatic Slash increase your Physical and Mental attack speeds by %d%%.\n\n\t\tThis talent will also attack with your shield, if you have one equipped.", "Uneash crudo, caótico daño elemental sobre su enemigo.\nUsted golpea a su enemigo por daños de arma %d %% en una de arena cegadora, desarmar ácido, congelar y ralentizar el hielo, relámpagos o llamas impresionantes, con iguales probabilidades.\nAdemás, causarás una ráfaga que afecte a las criaturas en radius %d, independientemente de si golpeas con el golpe.\nLos niveles de choque prismático aumentan sus velocidades de ataque físico y mental por %d %%.\n\nEste talento también atacará con su escudo, si tiene uno equipado.", "tformat")
t("You breathe crippling poison in a frontal cone of radius %d. Any target caught in the area will take %0.2f nature damage each turn for 6 turns.\n\t\tThe poison also gives enemies a %d%% chance to fail actions more complicated than basic attacks and movement, while it is in effect.\n\t\tThe damage will increase with your Strength, and the critical chance is based on your Mental crit rate.\n\t\tEach point in Venomous Breath also increases your nature resistance by 3%%, and your nature damage by 4%%.]] ):tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), effect)\n\tend,\n}\n\nnewTalent{\n\tname = \"Wyrmic Guile\",\n\ttype = {\"wild-gift/higher-draconic\", 3},\n\trequire = gifts_req_high3,\n\tpoints = 5,\n\tmode = \"passive\",\n\tresistKnockback = function(self, t) return self:combatTalentLimit(t, 1, .2, .5) end, -- Limit < 100%\n\tresistBlindStun = function(self, t) return self:combatTalentLimit(t, 1, .1, .25) end, -- Limit < 100%\n\tpassives = function(self, t, p)\n\t\tself:talentTemporaryValue(p, \"knockback_immune\", t.resistKnockback(self, t))\n\t\tself:talentTemporaryValue(p, \"stun_immune\", t.resistBlindStun(self, t))\n\t\tself:talentTemporaryValue(p, \"blind_immune\", t.resistBlindStun(self, t))\n\tend,\n\tinfo = function(self, t)\n\t\treturn ([[You have mastered your draconic nature.\n\t\tYou gain %d%% knockback resistance, and your blindness and stun resistances are increased by %d%%.", "Respira veneno desgarrador en un cono frontal de %d radio. Cualquier objetivo atrapado en la zona tomará daño de la naturaleza %0.2f cada turno por 6 vueltas.\nEl veneno también da a los enemigos una %d %% oportunidad de fallar acciones más complicadas que los ataques y movimientos básicos, mientras que está en efecto.\nEl daño aumentará con su fuerza, y la probabilidad crítica se basa en su tasa de criminalidad mental.\nCada punto en el aliento venenoso también aumenta su resistencia a la naturaleza por 3%%, y su daño natural por 4%%.]]:tformat(self:getTalentRadius(t), damDesc(self, DamageType.NATURE, t.getDamage(self,t)/6), efecto)\nFin,\n}\n\nNewTalent{\nnombre = \"Guía Jurídica\",\ntipo = {\"gift-gift/higher-draconic\", 3},\nRequiere = regalos req high3,\npuntos = 5,\nmodo = \"pasivo\",\nresistKnockback = función (self, t) volverse a sí mismo:combatTalentLimit(t, 1, .2, .5) final, -- Limite\nresistBlindStun = función(self, t) volverse a sí mismo:combatTalentLimit(t, 1, .1, .25) final, -- Limite\npasivos = función(self, t, p)\nauto:talentoTemporaryValue(p, \"knockback immune\", t.resistKnockback(self, t)))\nauto:talentoTemporarioValue(p, \"stun immune\", t.resistBlindStun(self, t)))\nauto:talentoTemporarioValue(p, \"blind immune\", t.resistBlindStun(self, t)))\nFin,\ninfo = función(self, t)\nretorno ([Usted ha dominado su naturaleza dracónica.\nGanas resistencia a golpes %d %%, y tus cegueras y resistencias a aturdimientos se incrementan por %d %%.", "tformat")
t("You have gained the full power of the various drakes throughout the world, and have become both resistant and attuned to physical, fire, cold, lightning, acid, nature, blight, and darkness damage.\n\t\tYour resistance to these elements is increased by %0.1f%% and all damage you deal with them is increased by %0.1f%% with %0.1f%% resistance penetration.\n\n\t\tLearning this talent will add a Willpower bonus to your breath talent damage with the same scaling as Strength, effectively doubling it when the stats are equal.", "Usted ha ganado el pleno poder de los diversos drakes en todo el mundo, y se han vuelto resistentes y atestados a los daños físicos, de fuego, fríos, relámpagos, ácido, naturaleza, luz y oscuridad.\nSu resistencia a estos elementos se incrementa por %0.1f %% y todo el daño que usted enfrenta con ellos se aumenta por %0.1f %% con la penetración de resistencia %0.1f %%.\n\nAprender este talento añadirá una bonificación de Willpower a su daño de talento respiratorio con el mismo escalado que Fuerza, duplicando eficazmente cuando las estadísticas son iguales.", "tformat")
