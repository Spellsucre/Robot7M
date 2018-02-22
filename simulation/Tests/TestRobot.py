"""Il faudra tester les différents éléments du robot ici"""
from Robot import Robot

#1ere phase: creer le robot faire un déplacement nul
robot = Robot((0,0,0), (0,0,0), (1,1,1))
robot.move()
print(robot.toString())

#2eme phase: effectuer une rotation
robot.rotation(45)
robot.move()
print(robot.toString())

#3eme phase: avancer le robot
#à compléter

#4eme phase: stopper le robot
#à compléter

#5eme phase: chercher une cible
#à compléter

#6eme phase: éviter une cible
#à compléter

#7eme phase: chercher une objectif vers lequel se diriger et effectuer les phases 2 à 6 en conséquence
#à compléter

