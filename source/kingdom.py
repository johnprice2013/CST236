import logging
import orc

class Kingdom(object):
    testString = None
    logger = logging.getLogger(__name__)
    streamHandle = logging.StreamHandler(__name__)
    def __init__(self):
        self.orcList = list()
        self.isBreached = False
        self.threatCount = 0
        pass
    """
    :mod:`source.kingdom.setIsBreached` -- Example source code
    ============================================

    The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
    """
    def setIsBreached(self,passedBool):
        """
        Determine if the given triangle is equilateral, scalene or Isosceles

        :param a: line a
        :type a: float or int or tuple or list or dict

        :param b: line b
        :type b: float

        :param c: line c
        :type c: float

        :return: "equilateral", "isosceles", "scalene" or "invalid"
        :rtype: str
        """
        self.isBreached = passedBool
        return self.isBreached

    def getIsBreached(self):
        return self.isBreached

    def writeDebugLogger(self):
        self.logger.debug("kingdom debug test")

    def writeInfoLogger(self):
        self.logger.info("kingdom info test")

    def writeDualLogger(self):
        self.writeDebugLogger()
        self.writeInfoLogger()

    def createOrcList(self,count):
        for x in range(count):
            testOrc = orc.Orc(1,2,x%8,self.threatCount)
            self.threatCount += 1
            self.orcList.append(testOrc)
        return self.orcList

    def addOrc(self, orcDistance, orcVelocity, orcType):
        newOrc = orc.Orc(orcDistance, orcVelocity, orcType, self.threatCount)
        self.orcList.append(newOrc)
        self.threatCount += 1
        return newOrc

    def removeOrc(self, orcId):
        for x in range(len(self.orcList)):
            if self.orcList[x].Id == orcId:
                self.orcList.remove(self.orcList[x])
                return True
        return False

    def setPriority(self, orcIndex, passedPriority):
        self.orcList[orcIndex].priority = passedPriority

    def removeAllThreats(self):
        self.orcList = []