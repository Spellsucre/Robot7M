from Arene import *
from Robot import *

def isCube(x,y,z,cube): # FONCTIONNE
        #print("isCube:",x,y,z,cube.safficher())
        for i in range (cube.x, cube.x + cube.larg+1):
            for j in range (cube.y, cube.y + cube.long+1):
                if x == i and y == j and cube.haut >= z and z >= cube.z:
                        return True
        return False

def isCubeList(x,y,z,liste_cube):
        i = 0
        while i < len(liste_cube) :
                objet = liste_cube[i]
                if(isinstance(objet,Mur)):
                        if isCube(x,y,z,objet):
                                print("sortie pour objet :",i)
                                return True
                i = i + 1
        return False
        

class Capteur : 
        def __init__(self,arene):
                self.arene = arene

        def detecter(self):
                zone = 3
                r = self.arene.liste_robot[0]
                x,y,z = r.position
                long, larg, haut = r.dimension
                dirx, diry = r.direction
                ex = x
                ey = y + (long/2)*diry # coordonnées de l'éclaireur : mises à la tete du robot

                i = 0
                while i < zone : # balayage de la zone
                        if isCubeList(ex,ey,haut,self.arene.liste_cube):
                                return True
                        ex = ex + dirx
                        ey = ey + diry
                        i  = i + 1
                return False
        
        
                      
                        

