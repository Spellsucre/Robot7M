import random
import math
from Robot import *

class TeteRobot:
    """
    Classe caractérisé par:
    sa position: triplet(x,y,z)
    son orientation: doublet(orx, ory)
    sa dimension: triplet(longueur, largeur, hauteur)
    un robot
    """

    def __init__(self, orientation):
        """Constructeur de la classe TeteRobot"""
        #self.position = position
        self.orientation = orientation
        #self.dimension = dimension
        #self.robot=robot

    def rotation(self, angle):
        """Methode de rotation de tete"""
        
        vx = self.orientation[0]
        vy = self.orientation[1]

        angle = math.radians(angle)
        
        vrx = vx * math.cos(angle) - vy * math.sin(angle)
        vry = vx * math.sin(angle) + vy * math.cos(angle)

        vrx = round(vrx)
        vry = round(vry)
        
        self.setOrientation((vrx,vry))
        print(self.safficher())

    def toString(self):
        return "ROBOT[Tete] | direction: {0}".format(self.orientation,)

    def safficher(self):
        """Methode d'affichage d'un robot au format :
        Robot[position, orientation, dimension]
        """
        return "[Tete] direction: {0}".format(self.orientation)
#________________________________GETTER_______________________________________


    """
    def getPosition(self):
        return self.position
    """
    def getOrientation(self):
        return self.orientation
    """
    def getDimension(self):
        return self.dimension
    """

#________________________________SETTER_____________________________________
    """
    def setPosition(self, position):
        self.position = position
    """
    def setOrientation(self, orientation):
        self.orientation = orientation
    """
    def setDimension(sel, dimension):
        self.dimension = dimension
    """


def Creation_TeteRobot():
    """Creation d'une tete de robot à partir d'un robot"""
    #xr, yr, zr =robot.position
    #longr, largr, hautr =robot.dimension
    """
    orx= xr
    ory= yr + longr/2
    """
    orx= 10
    ory= 10
    
    return TeteRobot((orx, ory))

