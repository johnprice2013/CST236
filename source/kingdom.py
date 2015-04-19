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

    def setIsBreached(self,passedBool):
        self.isBreached = passedBool

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