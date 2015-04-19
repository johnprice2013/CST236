class Orc(object):
	velocity = 0
	distance = 0
	def __init__(self,passedDistance,passedVelocity):
		Orc.distance = passedDistance
		Orc.velocity = passedVelocity

	def getVelocity(self):
		return self.velocity

	def getDistance(self):
		return self.distance