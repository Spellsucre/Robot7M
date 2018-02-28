#imports

import random
import math
from structures.TeteRobot import*
#code

class Robot:
    """
        Classe caractérisé par:
        Sa Position: triplet(x, y, z)
        Les coordonnees de ses 4 angles (xy0, xy1, xy2, xy3)
        Sa direction: triplet(a, b)
        Sa dimension(final): triplet(longueur, largeur, hauteur)
        Sa vitesse: entier
        sa tete: Class TeteRobot
    """

    def __init__(self, position, coords, direction, dimension, vitesse):
        self.position = position
        self.coords = coords
        self.direction = direction
        self.dimension = dimension
        self.vitesse = vitesse
        self.tete= Creation_TeteRobot()
    
    def move(self,direc):
        x, y, z = self.getPosition()
        a, b = direc
        vitesse = self.getVitesse()
        #xt, yt, zt = (self.tete).getPosition()
        longr, larg, haut = self.getDimension()
        
        x += a*vitesse
        y += b*vitesse
        #z += c*vitesse
        z += 0
        self.__setPosition((x, y, z))
        
        #xt= x + larg/2
        #yt= y
        #zt= z + haut/2
        #(self.tete).setPosition((xt, yt, zt))


    def move_bis(self):
        x, y, z = self.position
        xdir, ydir = self.direction
        larg, long, haut = self.dimension
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords
        
        vitesse = self.vitesse
        x += self.direction[0]*vitesse
        y += self.direction[1]*vitesse

        x0 += self.direction[0]*vitesse
        y0 += self.direction[1]*vitesse
        x1 += self.direction[0]*vitesse
        y1 += self.direction[1]*vitesse
        x2 += self.direction[0]*vitesse
        y2 += self.direction[1]*vitesse
        x3 += self.direction[0]*vitesse
        y3 += self.direction[1]*vitesse
        

        self.__setPosition((x, y, z))
        #print("1:",self.coords)
        self.setCoords(((x0,y0),(x1,y1),(x2,y2),(x3,y3)))
        #self.setCoords( ((x-larg/2, y+long/2), (x+larg/2, y+long/2), (x+larg/2, y-long/2), (x-larg/2, y-long/2)) )
        #print("2:",self.coords)
        #print("dir=",self.direction,"    centre=",self.position,"    coords=",self.coords)
        
        
    def retourne_angle(self,x,y,xx,yy) :
        """ retourne un angle teta en radian selon une direction initale d'un
            vecteur u(x,y) et une les coordonées du vecteur de la prochaine
            direction d'un vecteur v(xx,yy) en paramètres """

        sgn = (x*yy)+(xx*y)
        u = sqrt((x*x)+(y*y)) #norme de u
        v = sqrt((xx*xx)+(yy*yy)) #norme de v
        
        tmp = ((x*xx)+(y*yy))/(u+v)
        teta = acos(tmp)

        if(sgn < 0):
            return -1*teta
        return teta
        #teta: int en degré

    
    def rotation(self, teta):

        """la rotation est effectuée dans le sens anti-horaire"""
        teta = math.radians(teta)
        a, b = self.getDirection()
        temp = a
        a = math.ceil(a*math.cos(teta) - b*math.sin(teta))
        b = math.ceil(temp*math.sin(teta) + b*math.cos(teta))
        if(a == -0.0):
            a = abs(a)
        if(b == -0.0):
            b = abs(b)
        self.__setDirection((a, b))


    def rotation_bis(self,teta):
        """Effectue une rotation du robot (sur lui-même) de teta°"""
        angle = math.radians(teta)
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords
        
        ctx0 = (x0-self.position[0])*math.cos(angle) - (y0-self.position[1])*math.sin(angle) + self.position[0]
        cty0 = (x0-self.position[0])*math.sin(angle) + (y0-self.position[1])*math.cos(angle) + self.position[1]

        ctx1 = (x1-self.position[0])*math.cos(angle) - (y1-self.position[1])*math.sin(angle) + self.position[0]
        cty1 = (x1-self.position[0])*math.sin(angle) + (y1-self.position[1])*math.cos(angle) + self.position[1]
    
        ctx2 = (x2-self.position[0])*math.cos(angle) - (y2-self.position[1])*math.sin(angle) + self.position[0]
        cty2 = (x2-self.position[0])*math.sin(angle) + (y2-self.position[1])*math.cos(angle) + self.position[1]
    
        ctx3 = (x3-self.position[0])*math.cos(angle) - (y3-self.position[1])*math.sin(angle) + self.position[0]
        cty3 = (x3-self.position[0])*math.sin(angle) + (y3-self.position[1])*math.cos(angle) + self.position[1]

        newcoords = [ (round(ctx0), round(cty0)),
                      (round(ctx1), round(cty1)),
                      (round(ctx2), round(cty2)),
                      (round(ctx3), round(cty3))]
        
        self.setCoords(newcoords)   #maj coords des 4 points du robot
        print("coords=",self.coords)
        self.calcdir()              #maj direction du robot
        

    def calcdir(self):
        """ Calcule la direction du robot (correspond a l'avant du robot) et retourne cette derniere sous la forme : (x, y) """
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords

        dirxy1 = (self.position[0], self.position[1])
        dirxy2 = ( ((x0 + x1)/2), ((y0+y1)/2) )
        newdir = ( round(dirxy2[0]-dirxy1[0]), round(dirxy2[1]-dirxy1[1]) )
        self.__setDirection(newdir)

    
    def rotation_tete(self, teta):
        self.tete.rotation(teta)

    def toString(self):
        return "ROBOT[Corps]|position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())+"\n"+self.tete.toString()

    def safficher(self):
                """Methode d'affichage d'un robot au format :
                Robot[position, direction, taille, vitesse]
                """
                return "ROBOT([Corps] position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())#||| "+self.tete.safficher()+")"
                

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

    def setCoords(self, coords):
        self.coords = coords
        
        
    
    """-----------------------SAVER-------------------------"""
    def toSaveF(self, f):
        """Ecrit les coordonnees du robot dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Robot;' + str(self.position) + ';' +  str(self.direction) + ';' + str(self.dimension) + ';' + str(self.vitesse) + ';\n')


def Creation_Robot(arene):
        """creation d'un Robot avec une position aleatoire"""

        x = random.randint(175, arene.lx/2)
        y = random.randint(175, arene.ly/2)

        #x = random.randint(0, 100)
        #y = random.randint(0, 100)

        #x = 60
        #y = 60
        z = 1   #un robot est posé sur le sol

        larg = 40
        long = 40
        haut = 10
        
        dirx = 2
        diry = 2

        dirxy1 = (x, y)
        dirxy2 = (((x-larg/2)+(x+larg/2))/2, ((y+long/2)+(y+long/2))/2 )
        
        newdir = ( round(dirxy2[0]-dirxy1[0]), round(dirxy2[1]-dirxy1[1]) )

        vitesse = 1

        coords = ((x-larg/2, y+long/2), (x+larg/2, y+long/2), (x+larg/2, y-long/2), (x-larg/2, y-long/2))

        return Robot((x, y, z), coords, newdir, (larg, long, haut), vitesse)

        

