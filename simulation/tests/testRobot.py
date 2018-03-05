"""Il faudra tester les differents elements du robot ici"""
from structures.Robot import *
from structures.Arene import *


#1ere phase: creer le robot faire un deplacement nul
print("#1ere phase: creer le robot faire un deplacement nul")
robot = Robot((0,0,0), ((0,0),(2,0),(2,2),(0,2)), (1,1), (1,1,1), 1)
robot.move((0,0))
print(robot.toString())

print('\n')
#2eme phase: effectuer une rotation
print("#2eme phase: effectuer une rotation")
robot.rotation(45)
robot.move((0,0))
print(robot.toString())

print('\n')
#3eme phase: avancer le robot
print("#3eme phase: avancer le robot avec une direction donne")
robot.move((1,1))
print(robot.toString())

print('\n')
#4eme phase: stopper le robot
print("#4eme phase: stopper le robot")
robot.setVitesse(0)
print(robot.toString())
robot.setVitesse(1)

print('\n')
#5eme phase: chercher une cible
#a completer
                                        #Besoin de Capteur
#6eme phase: eviter une cible
#a completer

#7eme phase: chercher une objectif vers lequel se diriger et effectuer les phases 2 a 6 en consequence
#a completer

#fonction calcdir() , resultat attendu ??
print("#fonction calcdir() , resultat attendu ??")
print(robot.getDirection())
robot.calcdir()
print(robot.getDirection())

print('\n')
#fonction move_bis()
print("fonction move_bis() // Selon la direction du robot")
print(robot.toString())
robot.move_bis()
print(robot.toString())

print('\n')
#fonction retourne_angle
print("fonction retourne angle")
teta = robot.retourne_angle(1,1,1,1)
print(teta)

print('\n')
#fonction rotation
print("fonction rotation")
robot.rotation(teta)
print(robot.toString())

print('\n')
#fonction rotation_bis
print("fonction rotation_bis()")
robot.rotation_bis(teta)
print(robot.toString())

print('\n')
#fonction Creation_Robot aleatoire a partir d'une arene 
print("#fonction Creation_Robot aleatoire a partir d'une arene ")
a   = Creation_Arene()
rob = Creation_Robot(a) 
print(rob.toString())

print('\n')
#fonction rotation tete en DEGRE
print("Fonction rotation_tete en DEGRE")
robot.rotation_tete(180)
print(robot.toString())


print('\n')
#Fonction toSave pour sauvegarder le Robot dans un fichier
print("#Fonction toSave pour sauvegarder le Robot dans un fichier")
f = open ('testRobot.txt', 'w')
rob.toSaveF(f)
f = open ('testRobot.txt', 'r')
lines = f.readlines()
print ("Lecture du fichier ")
for mot in lines :
    print (mot)
f.close


#MG