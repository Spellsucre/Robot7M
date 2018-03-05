from structures.TeteRobot import *
from structures.Robot     import *

""" Test des differentes fonctionnalites de la classe TeteRobot """
print('')
#initialisation d'une TeteRobot
print("#initialisation d'une TeteRobot")
tete = TeteRobot((5,5))
print(tete.safficher())

print('')
#Creation d'une TeteRobot a partir d'un Robot donne
print("#Creation d'une TeteRobot a partir d'un Robot donne")
r    = Robot((0,0,0), ((0,0),(2,0),(2,2),(0,2)), (1,1), (1,1,1), 1)
print (r.safficher())
tete = Creation_TeteRobot()
print(tete.toString())

print('')
#Rotation de la TeteRobot
print("#Rotation de la TeteRobot")
tete.rotation(180)
print(tete.toString())


#MG
