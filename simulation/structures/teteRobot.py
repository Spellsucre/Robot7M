import random
import math


class TeteRobot:
    """
    Classe caractérisé par:
    son orientation: doublet(orx, ory) la tete ne bouge pas sur l'axe Z donc pas de triplet seulement un doublet
    """

    def __init__(self, orientation):
        """Constructeur de la classe TeteRobot"""
        self.orientation = orientation

    def rotation(self, angle):
        """Methode de rotation de tete"""
        
        vx = self.orientation[0]
        vy = self.orientation[1]

        angle = math.radians(angle)
        
        vrx = vx * math.cos(angle) - vy * math.sin(angle)
        vry = vx * math.sin(angle) + vy * math.cos(angle)

        #vrx = round(vrx)
        #vry = round(vry)
        
        self.setOrientation((vrx,vry))
		

    def toString(self):
        return "ROBOT[Tete] | direction: {0}".format(self.orientation,)

    def safficher(self):
        """Methode d'affichage d'un robot au format :
        Robot[position, orientation, dimension]
        """
        return "[Tete] direction: {0}".format(self.orientation)
#________________________________GETTER_______________________________________


    def getOrientation(self):
        return self.orientation

#________________________________SETTER_____________________________________

    def setOrientation(self, orientation):
        self.orientation = orientation


def Creation_TeteRobot():
    """Creation d'une tete de robot"""

    orx= 10
    ory= 10
    
    return TeteRobot((orx, ory))

