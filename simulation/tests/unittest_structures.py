import unittest
from structures.Arene import *
from basiques.Cube import *

""" Test du module structures """

class TestArene(unittest.TestCase):

    def setUp(self):
        self.l_c=[]
        self.a= Arene(10,10,10,self.l_c)
        self.a1=Creation_Arene()
        self.c = Cube(1,1,1,10,10,10)

    def test_afficher(self):
        print(self.a.afficher())

    def test_creationArene(self):
        self.assertIsInstance(self.a, Arene, msg='None')
        self.assertIsInstance(self.a1, Arene, msg='None')

    def test_ajouterCube(self):
        c = Creation_Cube(self.a)
        self.assertTrue(self.a1.ajouter_cube(c))

    def test_retirerCube(self):
        self.assertFalse(self.a.retirer_cube(0,0,0))
        self.assertTrue(self.a1.ajouter_cube(self.c))
        self.assertTrue(self.a1.retirer_cube(1,1,1))
    
    def test_isCube(self):
        self.assertTrue(self.a1.ajouter_cube(self.c))
        self.assertTrue(self.a1.isCube(self.c.x, self.c.y, self.c.z))
    
    def test_isCubeAtPoint(self):
        self.assertTrue(self.a1.ajouter_cube(self.c))
        self.assertTrue(self.a1.isCubeAtPoint(5,5,5))           #PB
        self.assertFalse(self.a1.isCubeAtPoint(0,0,0))

    def test_renvoieCube(self):
        self.assertTrue(self.a1.ajouter_cube(self.c))
        self.assertIsNotNone(self.a1.renvoie_cube(1,1,1))
        self.assertIsNone(self.a1.renvoie_cube(5,5,5))

    def test_ajoutRobot(self):
        r = Robot((1,1,1), ((0,0),(2,0),(2,2),(0,2)), (1,1), (1,1,1), 1)
        self.assertTrue(self.a1.ajouter_robot(r))

    def test_possedeSol(self):
        self.assertFalse(self.a1.possede_sol())
        s = Sol(1,1,1,10,10)
        self.assertTrue(self.a1.ajouter_cube(self.c))
        self.assertFalse(self.a1.possede_sol())        
        self.assertTrue(self.a1.ajouter_cube(s))
        self.assertTrue(self.a1.possede_sol())

    def test_sauvegarde(self):
        f = open('testArene.txt', 'w')
        self.a1.toSaveF(f)
        sauvegardeEnv(self.a1, 'testArene.txt')
        a2 = chargerEnv('testArene.txt')
        self.assertEqual(self.a1.lx, a2.lx)
        self.assertEqual(self.a1.ly, a2.ly)
        self.assertEqual(self.a1.lz, a2.lz)
        self.assertEqual(self.a1.liste_cube, a2.liste_cube)
        self.assertEqual(self.a1.liste_robot, a2.liste_robot)

class TestRobot (unittest.TestCase):
    def setUp (self):
        a = Creation_Arene()
        self.r  = Robot((1,1,1), ((0,0),(2,0),(2,2),(0,2)), (1,1), (1,1,1), 1)
        self.r2 = Creation_Robot(a)

    def test_creation(self):
        self.assertIsInstance(self.r, Robot)
        self.assertIsInstance(self.r2, Robot)

    def test_afficher(self):
        print(self.r2.safficher())
        print(self.r2.toString())


    def test_getter_setter(self):
        self.r.setPosition((0,0,0))
        self.assertEqual(self.r.getPosition(), self.r.position)
        self.r.setDirection((1,1))
        self.assertEqual(self.r.getDirection(), self.r.direction)
        self.assertEqual(self.r.getDimension(), self.r.dimension)
        self.r.setVitesse(1)
        self.assertEqual(self.r.getVitesse(), self.r.vitesse)
        self.r.setCoords(((0,0),(2,0),(2,2),(0,2)))
        self.assertEqual(self.r.getCoords(), self.r.coords)

    def test_move(self):
        x,y,z = self.r.getPosition()
        self.r.move((1,1))
        x += 1*self.r.vitesse
        y += 1*self.r.vitesse
        self.assertEqual(self.r.position, (x,y, z))
        
        x,y,z =self.r.getPosition()
        self.r.move_bis()
        self.assertEqual(self.r.position, ((x+self.r.direction[0])*self.r.vitesse,(y+self.r.direction[1])*self.r.vitesse, z ))

    def test_retourne_angle(self):
        teta = self.r.retourne_angle(1,1,1,1)
        self.assertEqual(teta, 0)
        #PB ? Pas compris la fonction , pourquoi ne renvoit pas 0 ?

    def test_rotation(self):
        a,b = self.r.direction
        self.r.rotation(360)
        self.assertEqual(self.r.direction, (a,b))
        #PB ? Rotation de 360 deg est sense revenir a la meme direction ?

        a,b = self.r.direction
        self.r.rotation_bis(360)
        self.assertEqual(self.r.direction, (a,b))

   # def test_calcdir(self):
        #Pas compris la fonction
    
    def test_rotationTete(self):
        a,b = self.r.tete.getOrientation()
        self.r.rotation_tete(360)
        self.assertEqual(self.r.tete.getOrientation(), (a,b))

    def test_sauvegarde(self):
        f = open ('testRobot.txt', 'w')
        self.r.toSaveF(f)
        f = open ('testRobot.txt', 'r')
        lines = f.readlines()
        print ("Lecture du fichier ")
        phrase =""
        for mot in lines :
            phrase += mot
        f.close
        self.assertSequenceEqual(phrase, 'Robot;' + str(self.r.position) + ';' +  str(self.r.direction) + ';' + str(self.r.dimension) + ';' + str(self.r.vitesse) + ';\n')


class TestTeteRobot(unittest.TestCase):
    def setUp(self):
        self.tr  = Creation_TeteRobot();
        self.tr2 = TeteRobot((1,1))

    def test_creation(self):
        self.assertIsInstance(self.tr, TeteRobot)
        self.assertIsInstance(self.tr2, TeteRobot)

    def test_afficher(self):
        print(self.tr.safficher())
        print(self.tr2.toString())

    def test_getter_setter(self):
        self.tr.setOrientation((1,1))
        self.assertEqual(self.tr.getOrientation(), (1,1))

    def test_rotation(self):
        x,y = self.tr.orientation
        self.tr.rotation(360)
        self.assertEqual(self.tr.orientation, (x,y))

    


if __name__ == '__main__':
    unittest.main()    