import random
from Interface.mur import *
from Basiques.Cube import * 
from Structures.Arene import *
"""Pour modifier les valeurs, allez dans save.txt"""
a1 = chargerEnv('cst.txt')
a1.afficher()
windowa = Window(1000,1000,'Arene')
for c in a1.liste_cube:
    windowa.addmur(c.x,c.y,c.z,c.larg,c.long,c.haut,2)
for r in a1.liste_robot:
    x,y,z=r.position
    lx,ly,lz=r.dimension
    windowa.addmur(x,y,z,lx,ly,lz,3)
pyglet.app.run()
