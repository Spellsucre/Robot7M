from Cube import Cube
class Mur(Cube):
    """Classe héritant de la classe Cube, caractérisée par:
        -ses coordonnées: x, y, z
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


def Creation_Mur(x,y,z,long,arene):     #ajouter des parametres c'est étrange pour une création rapide de mur mais bon pourquoi pas :)
    """Création d'un mur avec une hauteur et une epaisseur fixé par les limites de l'Arene"""
    
    return Mur(x, y, z, 10, long, arene.lz)


    
    
