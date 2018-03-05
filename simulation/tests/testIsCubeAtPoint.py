from Arene import *
from Cube import *

a1 = Creation_Arene()
test=False
i=0

while i<100:
	while test == False:
		c = Creation_Cube(a1)
		test = a1.ajouter_cube(c)

	print("_____________________________________")
	c.safficher()
	print()
	print(a1.ajouter_cube(c))
	print()
	print(a1.isCubeAtPoint(c.x,c.y,c.z))
	print(a1.isCubeAtPoint(c.x+c.larg,c.y,c.z))
	print(a1.isCubeAtPoint(c.x,c.y+c.long,c.z))
	print(a1.isCubeAtPoint(c.x,c.y,c.z+c.haut))
	print(a1.isCubeAtPoint(c.x+c.larg,c.y+c.long,c.z))
	print(a1.isCubeAtPoint(c.x+c.larg,c.y,c.z+c.haut))
	print(a1.isCubeAtPoint(c.x,c.y+c.long,c.z+c.haut))
	print(a1.isCubeAtPoint(c.x+c.larg,c.y+c.long,c.z+c.haut))
	print()
	print()

	a1.retirer_cube(c.x,c.y,c.z)
	test=False
	i=i+1
