
from basiques.Mur import *
from structures.Arene import *

""" Tests des differentes fonctionnalites de la classe Mur"""
print('\n')
#Creation d'un Mur  de coordonnee donnee
print("#Creation d'un Mur de coordonne donnee")
m = Mur(1,1,1,10,10,10)
m.safficher()
print('\n')

#Creation d'un Mur Aleatoire a partir d'une arene Aleatoire
print("#Creation d'un Mur Aleatoire a partir d'une arene Aleatoire")
a = Creation_Arene()
m = Creation_Mur(a)
m.safficher()
print('\n')

#Creation d'un mur avec une hauteur et une epaisseur fixe par les limites de l'Arene
print("#Creation d'un mur avec une hauteur et une epaisseur fixe par les limites de l'Arene")
m = Creation_Mur_xy(1,1,a)
m.safficher()
print('\n')


#Enregistre les coordonnees d'un Mur dans un fichier donne
print("#Enregistre les coordonnees d'un Mur dans un fichier donne")
f = open ('testMur.txt', 'w')
m.toSaveF(f)
f = open ('testMur.txt', 'r')
lines = f.readlines()
print ("Lecture du fichier ")
for mot in lines :
    print (mot)
f.close


#MG
