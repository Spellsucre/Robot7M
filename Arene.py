class Arene :
    """ Classe Arene caracterisée par les attributs:
    - lx : sa limite (double) sur l'axe des x
    - ly : sa limite (double) sur l'axe des y
    - lz : sa limite (double) sur l'axe des z
    - liste_cube : une liste contenant des "cubes"(sol,mur,obstacle) avec leurs coordonnées dans l'arene
    """

    def __init__(self,lx,ly,lz,liste_cube) :
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.liste_cube = liste_cube

    def ajouter_cube(self,cube) :
        """Si c'est possible on ajoute un cube dans l'arene
            et on return True, et False sinon"""
        bx = 0<cube.x and cube.x < self.lx
        by = 0<cube.y and cube.y < self.ly
        bz = 0<cube.z and cube.z < self.lz

        L = 0<cube.larg and cube.larg < self.lx
        l = 0<cube.long and cube.long < self.ly
        h = 0<cube.haut and cube.haut < self.lx
        
        if bx and by and bz and L and l and h:
            self.liste_cube.append(cube)
            return True
        return False
    
    def afficher(self):
        """Methode d'affichage d'une arene au format :
        Arene(limiteX= , limiteY= , limiteZ= )
        Liste d'objet [    ,    ,    ]
        """
        print("Arene(limiteX=%.2f,limiteY=%.2f,limiteZ=%.2f)"
              %(self.lx, self.ly, self.lz))
        print("Liste d'objet [")
        for i in self.liste_cube:
            print(i.safficher())
        print("]")
        

    def retirer_cube(self,x,y,z) :
        """Si il y'a un cube à la position (x,y,z) dans l'arene
            on le retire et on return True, sinon on return False """
        i = 0
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if c.x == x and c.y == y and c.z == z :
                del self.liste_cube[i]
                return True
            else :
                i= i+1
        return False

    
    def isCube(self,x,y,z) :
        """return True si il y'a un cube à la position (x,y,z)
            de l'arene et False sinon"""
        i = 0
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if c.x == x and c.y == y and c.z == z :
                return True
            else :
                i= i+1
        return False

    def isCubeAtPoint(self,x,y,z) :
        """return True si le point à la position (x,y,z) appartient à un cube
            de l'arene et False sinon"""
        i = 0
        cube = None
        if (self.liste_cube is None) or x >= self.lx or x < 0 or y >= self.ly or y < 0 or z < self.lz or z < self.lz :
            return False
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if (c.x+0.5*c.larg >=x and c.x-0.5*c.larg <= x) and (c.y+0.5*c.longr >= y and c.y-0.5*c.longr <= y) and (c.z+0.5*c.haut >= z and c.z-0.5*c.haut <= z):
                cube = c
            i= i+1
        return cube

    def renvoie_cube(self,x,y,z) :
        """ Renvoie le cube à la position (x,y,z) si il y'en a un
            et None sinon """

        i = 0
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if c.x == x and c.y == y and c.z == z :
                return c
            else :
                i= i+1
        return None


def Creation_Arene() :
    """ Test d'une creation d'Arene vide"""
    liste_cube = [] #liste vide pour créer une arène vide
    lx = 10
    ly = 10
    lz = 10 # valeurs limites de l'arène

    arene = Arene(lx,ly,lz,liste_cube)

    return arene





        

    
            
            
"Arene.py 2eme soumission (Vinson)" 
