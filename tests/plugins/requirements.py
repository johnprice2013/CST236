
from nose2.events import Plugin

class Requirements(Plugin):
    configSection = 'requirements'


    def __init__(self):
        for x in Requirements:
            print Requirements.func_name
        self.fileName = "test_requirements_list"
        print self.requirements
        print self.awesome