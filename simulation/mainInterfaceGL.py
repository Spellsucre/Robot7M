import random
from interface.cubeGL import *
from structures.robot import *
from basiques.cube import * 
from structures.arene import *
from save.saveJson import *
from save.csvToJson import *

"""Pour modifier les valeurs, allez dans save.csv"""
CsvToJson("save")
a1 = loadFic('save')
a1.afficher()
wPrincipale = Window(1366,768,'Arene')
for c in a1.liste_cube:
    if isinstance(c, Mur):
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,1)
    elif isinstance(c, Sol):
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,4)
    else:
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,1)
for r in a1.liste_robot:
    x,y,z=r.position
    lx,ly,lz=r.dimension
    wPrincipale.addcube(x,y,z,lx,ly,lz,3)
pyglet.app.run()
a1.liste_robot[0].move()
