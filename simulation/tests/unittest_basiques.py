import unittest 
from basiques import *
from structures.Arene import *

""" Unittest du module basiques """

class TestMur(unittest.TestCase):
    def setUp(self):
        self.mur = Mur(1,1,1,10,10,10)

    def test_CreationMur(self):
        self.assertIsInstance()

    def test_affichage(self):
        print(self.mur.safficher())
    
    def test_MurAleatoire(self):
        a   = Creation_Arene()
        self.mur = Creation_Mur(a)
    
    def test_MurAleatoireXY(self):
        a = Creation_Arene()
        self.mur = Creation_Mur_xy(2,2,a)
    
    def test_Sauvegarde(self):
        f = open ('testMur.txt', 'w')
        self.mur.toSaveF(f)
        f = open ('testMur.txt', 'r')
        lines = f.readlines()
        phrase = ""
        for mot in lines :
            phrase+=mot
        f.close
        self.mur.assertSequenceEqual(phrase, 'Mur;' + str(self.mur.x) + ';' + str(self.mur.y) + ';' + str(self.mur.z) + ';' + str(self.mur.larg) + ';' + str(self.mur.long) + ';' + str(self.mur.haut) + ';\n' ))

class TestCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(1,1,1,10,10,10)
    
    def test_affichage(self):
        print(self.cube.safficher())
    
    def test_CubeAleatoire(self):
        a = Creation_Arene()
        self.cube = Creation_Cube(a)
        x,y,z = self.cube.getPos()
        self.assertEqual(self.cube.x, x)
        self.assertEqual(self.cube.y, y)
        self.assertEqual(self.cube.z, z)

    def test_CubeAleatoireXY(self):
        a = Creation_Arene()
        self.cube = Creation_Cube_xy(2,2,a)
        x,y,z = self.cube.getPos()
        self.assertEqual(self.cube.x, x)
        self.assertEqual(self.cube.y, y)
        self.assertEqual(self.cube.z, z)

    def test_Sauvegarde(self):
        f = open ('testCube.txt', 'w')
        self.cube.toSaveF(f)
        f = open ('testCube.txt', 'r')
        lines = f.readlines()
        phrase = ""
        for mot in lines :
            phrase+=mot
        f.close
        self.cube.assertSequenceEqual(phrase, 'Cube;' + str(self.cube.x) + ';' + str(self.cube.y) + ';' + str(self.cube.z) + ';' + str(self.cube.larg) + ';' + str(self.cube.long) + ';' + str(self.cube.haut) + ';\n' ))

class TestSol (unittest.TestCase):
    def setUp (self):
        self.sol = Sol(1,1,1,10,10)
    
    def test_affichage(self):
        print(self.sol.safficher())

    def test_SolAleatoire(self):
        a = Creation_Arene()
        self.sol = Creation_Sol(a)
        x,y,z = self.sol.getPos()
        self.assertEqual(self.sol.x, x)
        self.assertEqual(self.sol.y, y)
        self.assertEqual(self.sol.z, z)
    
    def test_Sauvegarde(self):
        f = open ('testSol.txt', 'w')
        self.sol.toSaveF(f)
        f = open ('testSol.txt', 'r')
        lines = f.readlines()
        phrase = ""
        for mot in lines :
            phrase += mot
        f.close
        self.sol.assertSequenceEqual(phrase, 'Sol;' + str(self.sol.x) + ';' + str(self.sol.y) + ';' + str(self.sol.z) + ';' + str(self.sol.larg) + ';' + str(self.sol.long) + ';' + str(self.sol.haut) + ';\n' ))


if __name__ == '__main__':
    unittest.main()


    