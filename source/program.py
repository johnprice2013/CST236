class Program(object):
    def __init__(self, passedFile = 'blank'):
        self.importFile = passedFile
        self.readSuccessful = False

    def initialize(self):
        try:
            self.myFile = open(self.importFile)
            self.myString = self.myFile.read()
            self.readSuccessful = True
        except IOError:
            pass

    def createCities():
        pass