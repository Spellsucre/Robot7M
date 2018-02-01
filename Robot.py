import math
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

	#teta: int en degré
	def rotation(self, teta):
		teta = math.radians(teta)
		a, b, c = self.getDirection()
		a = a*math.cos(teta) - b*math.sin(teta)
		y = a*math.sin(teta) + b*math.cos(teta)
		self.__setDirection((a, b, c))

	def toString(self):
		return "position: {0}, direction: {1}, vitesse: {2}".format(self.getPosition(),self.getDirection(),self.getVitesse())

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