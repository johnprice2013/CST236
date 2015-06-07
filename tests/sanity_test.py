import os
import random
from modulefinder import ModuleFinder
from unittest import TestCase
import inspect
import logging


#class function_test():
    # def runTest(self,function, arg):
        # thing = "passed"
        # try:
            # thing = function(arg)
        # except Exception:
            # thing = "failed"
            # print function.__module__
        # return thing

class sanity_test(TestCase):

    def setUp(self):
        self.failMessage = "passed"
        self.finder = ModuleFinder()
        self.modules = self.finder.run_script("C:/Users/John/Documents/GitHub/CST236/tests/main.py")
        self.moduleslist = {}
        for name, mod in self.finder.modules.iteritems():
            filename = mod.__file__
            if filename is None:
                continue
            if '__' in name:
                continue
            self.moduleslist[name.split(".")[0]] = True


    def test_run(self):
        self.failMessage = "import clean"
        for name, dummy in self.moduleslist.iteritems():
            try:
                __import__(name)
            except ImportError:
                self.failMessage = "import " + name + " failed"
        self.assertEqual(self.failMessage, "import clean")

    def test_all_classes(self):
        self.logger = logging.getLogger("classes")
        count = 0
        for name, dummy in self.moduleslist.iteritems():
            count += 1
            try:
                __import__(name)
            except ImportError:
                self.failMessage = "import " + name + " failed"
                self.logger.debug(self.failMessage)
                self.logger.debug(len(self.moduleslist))
        for name, dummy in self.moduleslist.iteritems():
            for item in dir(name):
                    myClass = getattr(name,item)
                    if inspect.isclass(myClass):
                        try:
                            thing = myClass()
                            for method in dir(thing):
                                worksWith = ""
                                #try as empty function
                                try:
                                    myFunction = getattr(item,method)
                                    myFunction()
                                except Exception as emptyExcept:
                                    worksWith += "empty "
                                #try with number arguments
                                try:
                                    myFunction = getattr(item,method)
                                    myFunction(3)
                                except Exception as intExcept:
                                    worksWith += "number "
                                #try with string arguments
                                try:
                                    myFunction = getattr(item,method)
                                    myFunction("string")
                                except Exception as intExcept:
                                    worksWith += "string"
#This will log the functions that don't work while empty, with an int and with a
#string.  It excludes a few methods that fail because that would be a TON of functions
# to look up
                                if worksWith == "" and method != "__init__" and method != "__class__" and method != "__subclasshook__" and method != "format":
                                    self.logger.debug(name +"." + method + " doesn't work with empty arguments, a number or a string")
                        except Exception as e:
                            self.logger.debug(e.message)
#this will force output, just for the sake of this example
        self.assertEqual(self.failMessage,"pased")