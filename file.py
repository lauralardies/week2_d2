from vikingsclasses import Viking
from vikingsclasses import Saxon
from vikingsclasses import War

v1 = Viking('Ana', 500, 76)
v2 = Viking('Carolina', 390, 97)
v3 = Viking('Soraya', 910, 23)
v4 = Viking('Claudia', 200, 120)

s1 = Saxon(415, 65)
s2 = Saxon(678, 41)
s3 = Saxon(873, 89)
s4 = Saxon(278, 90)

war = War()

war.addViking(v1)
war.addViking(v2)
war.addViking(v3)
war.addViking(v4)

war.addSaxon(s1)
war.addSaxon(s2)
war.addSaxon(s3)
war.addSaxon(s4)

war.vikingAttack()
war.saxonAttack()
war.saxonAttack()
war.showStatus()
war.vikingAttack()