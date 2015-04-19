import sys


class interface(object):
    def __init__(self):
        pass

    def getInput(self, input = None):
        return input

    def handleInput(self, input = None, kingdom = None):
        if input == "X":
            self.quitProgram()
        elif input == "?":
            return self.showCommands()
        elif input == 'ENTer the trees' and kingdom != None:
            kingdom.removeAllThreats()
            return
        else:
            return "not valid"

    def quitProgram(self):
        sys.exit(0)

    def showCommands(self):
        return "X = quit, I = identify threats, U = useless command, ? = show commands, ENTer the trees = remove all threats"