import random
from interface.featuresGL import *
from structures.robot import *
from basiques.cube import *
from structures.arene import *
from save.saveJson import *
from save.csvToJson import *

"""Pour modifier les valeurs, allez dans save.csv"""
CsvToJson("save") #convertit le fichier .csv en .json
a1 = loadFic("save") #charge le .json
a1.afficher()
wPrincipale = Window(1000,1000,'Arene')
for c in a1.liste_cube:
    if isinstance(c, Mur):
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,1)
    elif isinstance(c, Sol):
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,3)
    else:
        wPrincipale.addcube(c.x,c.y,c.z,c.larg,c.long,c.haut,1)
for r in a1.liste_robot:
    x,y,z=r.position
    lx,ly,lz=r.dimension
    wPrincipale.addcube(x,y,z,lx,ly,lz,2)
pyglet.app.run()
a1.liste_robot[0].move()
