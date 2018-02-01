class Robot:
	"""
		Classe caractérisé par:
		Sa Position: triplet(x, y, z)
		Sa direction: triplet(a, b, c)
		Sa dimension(final): triplet(longueur, largeur, hauteur)
		Sa vitesse: entier
	"""

	def __init__(self, position, direction, dimension):
		self.position = position
		self.direction = direction
		self.dimension = dimension
		self.vitesse = 0


	def move(self):
		x, y, z = self.getPosition()
		a, b, c = self.getDirection()
		vitesse = self.getVitesse()
		x += a*vitesse
		y += b*vitesse
		z += c*vitesse
		self.__setPosition((x, y, z))

	def rotation(self, teta):
		a, b, c = self.getDirection()
		a = a*Math.cos(teta) - y*Math.sin(teta)
		y = x*Math.sin(teta) + y*Math.cos(teta)
		self.__setDirection((a, b, c))

	def toString(self):
		return "position:",self.getPosition()
		#à compléter


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
		self.positon = position

	def __setDirection(self, direction):
		self.direction = direction

	def __setVitesse(self, vitesse):
		self.vitesse = vitesse


def creation_robot() :
    """ Test création robot"""
    robot = Robot((0,0,0), (0,0,0), (1,1,1))
    robot.move()
    robot.toString()

creation_robot()