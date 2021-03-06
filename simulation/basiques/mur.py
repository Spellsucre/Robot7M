from basiques.Cube import Cube
import random

class Mur(Cube):
    """Classe heritant de la classe Cube, caracterisee par:
        -ses coordonnees: x, y, z
        -sa hauteur
        -sa largueur
        -sa longueur"""

    def __init__(self, x, y, z, larg, long, haut):
        """Constructeur de la classe Mur"""
        Cube.__init__(self,x,y,z,larg,long,haut)

    def safficher(self):
        """Methode d'affichage d'un mur au format :
        mur[x= , y= , z= , larg= , long= , haut= ]
        """
        print("Mur(x=%.2f,y=%.2f,z=%.2f, larg=%.2f,long=%.2f,haut=%.2f)"%(self.x, self.y, self.z, self.larg, self.long, self.haut))

    def toSaveF(self, f):
        """Ecrit les coordonnees du mur dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Mur;' + str(self.x) + ';' + str(self.y) + ';' + str(self.z) + ';' + str(self.larg) + ';' + str(self.long) + ';' + str(self.haut) + ';\n' )
			
def Creation_Mur(arene):
    """Creation d'un mur avec une hauteur et une epaisseur fixe par les limites de l'Arene"""

    x = random.randint(0, arene.lx)
    y = random.randint(0, arene.ly)
    z = 1   #un mur est pose au sol

    larg = random.randint(10, 50) #largeur arbitraire
    long = random.randint(20,100)
    haut = arene.lz-1   #un mur va jusq'au plafond 
    
    return Mur(x, y, z, larg, long, haut)



#creation d'u constructeur temporaire pour l'affichage tkinter
def Creation_Mur_xy(x, y, arene):
    """Creation d'un mur avec une hauteur et une epaisseur fixe par les limites de l'Arene"""

    x = x
    y = y
    z = 1  # un mur est pose au sol

    larg = random.randint(50, arene.lx)
    long = 20
    haut = 499  # un mur monte jusqu'au plafond

    return Mur(x, y, z, larg, long, haut)
    
    
