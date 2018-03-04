from Arene import *
from Robot import *
from Capteur import *
#test capteur

a1=Creation_Arene()
a1.generateur_arene()

#m1=Mur(20,20,0,40,30,500)
#a1.ajouter_cube(m1)

a1.afficher()

point = 150,10,10
print(point)
print("~>",isCubeList(point[0],point[1],point[2], a1.liste_cube))
