
from nose2.events import Plugin
from nose2.events import StopTestRunEvent
from tests.ReqTracer import Requirements

class RequirementsClass(Plugin):
    configSection = 'requirements'


    def afterTestRun(self, event):
        print type(Requirements)
        f = open("test_requirements.txt", 'w')
        
        for key, value in Requirements.viewitems():
            f.write(str(key) + "\n")
            f.write(str(value.func_name)+ "\n")
        f.close()