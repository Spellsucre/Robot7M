from basiques.Cube import *
from structures.Arene import *

""" Test des differents elements du Cube """

#Creation d'un cube de coordonnee donnees 
print("#Creation d'un cube de coordonnee donnees ")
c1 = Cube(1,1,1,10,10,10)
c1.safficher()
print ('\n')

#Creation d'un Cube aleatoire a partir d'une arene aleatoire
print("#Creation d'un Cube aleatoire a partir d'une arene aleatoire")
a = Creation_Arene()
c = Creation_Cube(a)
c.safficher()
print ('Pos: x, y, z')
print (c.getPos())
print ("\n")

#Creation d'un cube de taille aleatoire mais de position donnee
print ("#Creation d'un cube de taille aleatoire mais de position donnee")
c=Creation_Cube_xy(1,1,a)
c.safficher()
print('Pos: x, y, z')
print(c.getPos())
print ("\n")


#Enregistre les coordonnees d'un cube dans un fichier donne
print("#Enregistre les coordonnees d'un cube dans un fichier donne")
f = open ('testCube.txt', 'w')
c1.toSaveF(f)
f = open ('testCube.txt', 'r')
lines = f.readlines()
print ("Lecture du fichier ")
for mot in lines :
    print (mot)
f.close


#MG