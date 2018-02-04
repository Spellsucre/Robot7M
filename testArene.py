#imports

from Cube import *
from Mur import *
from Sol import *
from Robot import *
from Arene import *

#main de test

a1 = Creation_Arene()
c1 = Creation_Cube(a1)
s1 = Creation_Sol(a1)
m1 = Creation_Mur(a1)
r1 = Creation_Robot(a1)


c1.safficher()
print('\n')
s1.safficher()
print('\n')
m1.safficher()
print('\n')
r1.safficher()
print('\n')

a1.ajouter_cube(c1)
a1.ajouter_cube(s1)
a1.ajouter_cube(m1)
a1.ajouter_robot(r1)

a1.afficher()
print('\n')

"""
r1 = Creation_Robot(a1)
"Robot(Pos (175, 242, 1) ,Dir (0, 1, 0) ,Dim (10, 10, 10) ,Vit( 0 ))"
r1._Robot__setVitesse(1)
r1.safficher()
"Robot(Pos (175, 242, 1) ,Dir (0, 1, 0) ,Dim (10, 10, 10) ,Vit( 1 ))"
r1.move()
r1.safficher()
"Robot(Pos (175, 242, 1) ,Dir (0, 1, 0) ,Dim (10, 10, 10) ,Vit( 1 ))"
#pb dans le move

"""
