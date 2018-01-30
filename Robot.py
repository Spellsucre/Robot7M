class Robot:
	"""Classe caractérisé par:
		Ses coordonnées
		Sa direction
		Sa dimension
		Sa vitesse"""

	def __init__(self, position, direction, dimension, vitesse):
		self.position = position
		self.direction = direction
		self.dimension = dimension
		self.vitesse = 0

	def getPosition(self):
		return self.position

	def getDirection(self):
		return self.direction

	def getDimension(self):
		return self.dimension

	def getVitesse(self):
		return self.vitesse

		
	