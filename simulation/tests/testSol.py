from basiques.Sol import *
from structures.Arene import *

""" Test des differents elements du Sol"""
print ('\n')

#Creation d'un Sol de coordonnee donnees 
print("#Creation d'un Sol de coordonnee donnees ")
s = Sol(1,1,1,10,10)
s.safficher()
print ('\n')

#Creation d'un Sol aleatoire a partir d'une arene aleatoire
print("#Creation d'un Sol aleatoire a partir d'une arene aleatoire")
a = Creation_Arene()
s = Creation_Sol(a)
s.safficher()
print ("\n")

#Enregistre les coordonnees d'un Sol dans un fichier donne
print("#Enregistre les coordonnees d'un Sol dans un fichier donne")
f = open ('testSol.txt', 'w')
s.toSaveF(f)
f = open ('testSol.txt', 'r')
lines = f.readlines()
print ("Lecture du fichier ")
for mot in lines :
    print (mot)
f.close


#MG