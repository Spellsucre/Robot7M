import json
from structures.arene import *
from structures.robot import *
from structures.teteRobot import *
from basiques.cube import *
from basiques.sol import *
from basiques.mur import *
from save.saveJson import *

"""Cette fonction permet d'utiliser un fichier csv nommé save.csv (facile à modifier) pour le formatter en Json"""
def CsvToJson(nomfichierJson):
    """Fonction de chargement, ouverture du fichier en mode lecture"""
    with open("save/save.csv",'r') as f:
        liste_cube = list()
        liste_robot = list()
        """deux listes vides pour contenir les objets charges"""
        for line in f:
            ligne=line.split(";")
            if ligne[0] == 'Arene':
                """On cree une nouvelle arene avec les parametres trouves sur la ligne, separes par des ';' """
                arene = Arene(int(ligne[1]),int(ligne[2]),int(ligne[3]),liste_cube,liste_robot)
                arene.liste_robot=liste_robot
            elif ligne[0] == 'Cube':
                """On ajoute le cube a la liste de cube de l'arene, avec parametres trouves sur la ligne"""
                arene.liste_cube.append(Cube(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5]),int(ligne[6])))
            elif ligne[0] == 'Mur':
                arene.liste_cube.append(Mur(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5]),int(ligne[6])))
            elif ligne[0] == 'Sol':
                arene.liste_cube.append(Sol(int(ligne[1]),int(ligne[2]),int(ligne[3]),int(ligne[4]),int(ligne[5])))
            elif ligne[0] == 'Robot':
                (x,y,z)=literal_eval(ligne[1])
                ((cax,cay),(cbx,cby),(ccx,ccy),(cdx,cdy))=literal_eval(ligne[2])
                (a,b,c)=literal_eval(ligne[3])
                (lo,la,ha)=literal_eval(ligne[4])
                vitesse=literal_eval(ligne[5])
                arene.liste_robot.append(Robot((x,y,z),((cax,cay),(cbx,cby),(ccx,ccy),(cdx,cdy)),(a,b,c),(lo,la,ha),vitesse))
    saveFic(arene,nomfichierJson)
        
