from Interface.mur import *
from Basiques.Cube import * 
from Structures.Arene import *

a1 = chargerEnv('save.txt')
a1.afficher()
windowa = Window(1000,1000,'Arene')
for c in a1.liste_cube:
    windowa.addmur(c.x,c.y,c.z,c.larg,c.long,c.haut)
pyglet.app.run()
