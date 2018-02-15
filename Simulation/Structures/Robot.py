#imports

import random
import math
from TeteRobot import*
#code

class Robot:
    """
        Classe caractérisé par:
        Sa Position: triplet(x, y, z)
        Sa direction: triplet(a, b, c)
        Sa dimension(final): triplet(longueur, largeur, hauteur)
        Sa vitesse: entier
        sa tete: Class TeteRobot
    """

    def __init__(self, position, direction, dimension):
        self.position = position
        self.direction = direction
        self.dimension = dimension
        self.vitesse = 0
        self.tete= Creation_TeteRobot(self)
    
    def move(self):
        x, y, z = self.getPosition()
        a, b, c = self.getDirection()
        vitesse = self.getVitesse()
        xt, yt, zt = (self.tete).getPosition()
        
        x += a*vitesse
        y += b*vitesse
        z += c*vitesse
        self.__setPosition((x, y, z))
        
        xt= x + larg/2
        yt= y
        zt= z + haut/2
        (self.tete).setPosition((xt, yt, zt))

    #teta: int en degré
    def rotation(self, teta):
        """la rotation est effectuée dans le sens anti-horaire"""
        teta = math.radians(teta)
        a, b, c = self.getDirection()
        temp = a
        a = math.ceil(a*math.cos(teta) - b*math.sin(teta))
        b = math.ceil(temp*math.sin(teta) + b*math.cos(teta))
        if(a == -0.0):
            a = abs(a)
        if(b == -0.0):
            b = abs(b)
        self.__setDirection((a, b, c))
       
    def rotation_tete(self, teta):
        self.tete.rotation(teta)

    def toString(self):
        return "position: {0}, direction: {1}, vitesse: {2}".format(self.getPosition(),self.getDirection(),self.getVitesse())

    def safficher(self):
                """Methode d'affichage d'un robot au format :
                Robot[position, direction, taille, vitesse]
                """
                print("Robot(Pos",self.position,",Dir",self.direction,",Dim",self.dimension,",Vit(",self.vitesse,"))")
                

    """-----------------------GETTTER-------------------------"""
    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction

    def getDimension(self):
        return self.dimension

    def getVitesse(self):
        return self.vitesse

    """-----------------------SETTER-------------------------"""
    def __setPosition(self, position):
        self.position = position

    def __setDirection(self, direction):
        self.direction = direction

    def setVitesse(self, vitesse):
        self.vitesse = vitesse
        
    
    """-----------------------SAVER-------------------------"""
    def toSaveF(self, f):
        """Ecrit les coordonnees du robot dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Robot;' + str(self.position) + ';' +  str(self.direction) + ';' + str(self.dimension) + ';' + str(self.vitesse) + ';\n')


def Creation_Robot(arene):
        """creation d'un Robot avec une position aleatoire"""

        x = random.randint(0, arene.lx)
        y = random.randint(0, arene.ly)
        z = 1   #un robot est posé sur le sol

        dirx = 20
        diry = 20
        dirz = 0

        larg = 50
        long = 50
        haut = 10

        return Robot((x, y, z), (dirx, diry, dirz), (larg, long, haut))

        

