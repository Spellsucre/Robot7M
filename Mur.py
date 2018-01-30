from Cube import Cube
class Mur(Cube):
    """Classe héritant de la classe Cube, caractérisée par:
        -ses coordonnées: x, y, z
        -sa hauteur
        -sa largueur
        -sa longueur"""

    def __init__(self, x, y, z, larg, long, haut):
        """Constructeur de la classe Mur"""
        self.x = x
        self.y = y
        self.z = z
        self.long = long
        self.larg=larg
        self.haut=haut


def Creation_Mur(x,y,z,long,arene):
    """Création d'un mur avec une hauteur et une epaisseur fixé par les limites de l'Arene"""
    
    return Mur(x, y, z, 10, long, arene.lz)


    
    
