import logging
class Orc(object):
    velocity = 0
    distance = 0
    types = ['heavy', 'bowman', 'grunt', 'rifleman', 'shielder', 'boss', 'scout', 'fatty']
    logger = logging.getLogger(__name__)
    def __init__(self, passedDistance = 0, passedVelocity = 0, typeIndex = 0, passedId = 0, priority = 0):
        self.distance = passedDistance
        self.velocity = passedVelocity
        self.type = self.types[typeIndex]
        self.Id = passedId
        self.priority = priority

    def getVelocity(self):
        return self.velocity

    def getDistance(self):
        return self.distance

    def writeInfoLogger(self):
        self.logger.info('orc info test')

    def getType(self):
        return self.type

    def getId(self):
        return self.Id