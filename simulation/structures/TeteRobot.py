import random
import math
from structures.Robot import *

class TeteRobot:
    """
    Classe caractérisé par:
    sa position: triplet(x,y,z)
    son orientation: doublet(orx, ory)
    sa dimension: triplet(longueur, largeur, hauteur)
    un robot
    """

    def __init__(self, position, orientation, dimension, robot):
        """Constructeur de la classe TeteRobot"""
        self.position = position
        self.orientation = orientation
        self.dimension = dimension
        self.robot=robot

    def rotation(self, teta):
        """Methode de rotation de tete, retourne True s'il est possible de tourner la tete, sinon retourne False """
        teta = math.radians(teta)
        orx, ory = self.orientation
        x , y, z = self.position
        
        tmp = orx
        orx = math.ceil(orx*math.cos(teta) - ory*math.sin(teta))
        ory = math.ceil(tmp*math.sin(teta) + ory*math.cos(teta))

        if ( ory>= y and orx>=0):
            self.setOrientation((orx, ory))
            return True
        return False

    def toString(self):
        return "ROBOT[Tete] |position: {0}, direction: {1}, dimension: {2}".format(self.position, self.orientation, self.dimension)

    def safficher(self):
        """Methode d'affichage d'un robot au format :
        Robot[position, orientation, dimension]
        """
        return "[Tete] position: {0}, direction: {1}, dimension: {2}".format(self.position, self.orientation, self.dimension)
#________________________________GETTER_______________________________________



    def getPosition(self):
        return self.position

    def getOrientation(self):
        return self.orientation

    def getDimension(self):
        return self.dimension


#________________________________SETTER_____________________________________

    def setPosition(self, position):
        self.position = position

    def setOrientation(self, orientation):
        self.orientation = orientation

    def setDimension(sel, dimension):
        self.dimension = dimension



def Creation_TeteRobot(robot):
    """Creation d'une tete de robot à partir d'un robot"""
    xr, yr, zr =robot.position
    longr, largr, hautr =robot.dimension
    
    x= xr 
    y= yr + longr/2
    z= zr + hautr/2

    orx= xr 
    ory= yr + longr/2

    larg= largr/4
    long= longr/4
    haut= hautr/4

    return TeteRobot((x, y, z), (orx, ory), (larg, long, haut), robot)


    
