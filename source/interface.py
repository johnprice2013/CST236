import sys


class interface(object):
    def __init__(self):
        pass

    def getInput(self, input = None):
        return input

    def handleInput(self, input = None):
        if input == "X":
            self.quitProgram()
        elif input == "?":
            return self.showCommands()
        else:
            return "not valid"

    def quitProgram(self):
        sys.exit(0)

    def showCommands(self):
        return "X = quit, I = identify threats, U = useless command, ? = show commands"