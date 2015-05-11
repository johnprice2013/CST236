from question_answer import QA
from main import Interface
from unittest import TestCase
import time
import getpass
from ReqTracer import requirements

class TestQA(TestCase):

    @requirements(['#0017'])
    def test_conversion_question(self):
        myInterface = Interface()
        feet = float(5280)
        string = "What is " + str(feet) + " feet in miles?"
        answer = myInterface.ask(string)
        self.assertEqual(answer, "1.0 miles")

#    @requirements(['#0018'])
#    def test_seconds_question(self):
#        myInterface = Interface()
#        seconds = time.strftime("%d/%m/%Y%H:%M:%S")
#        string = "How many seconds since " + str(seconds) + "?"
#        answer = myInterface.ask(string)
#        self.assertEqual(answer, "0 seconds")

    @requirements(['#0019'])
    def test_inventor_question(self):
        myInterface = Interface()
        answer = myInterface.ask("Who invented Python?")
        self.assertEqual(answer, "Guido Rossum(BDFL)")

    @requirements(['#0020'])
    def test_understanding_question(self):
        myInterface = Interface()
        answer = myInterface.ask("Why don't you understand me?")
        self.assertEqual(answer, "Because you do not speak 1s and 0s")

    @requirements(['#0021'])
    def test_shutdown_question(self):
        myInterface = Interface()
        answer = myInterface.ask("Why don't you shut down?")
        answerString = "I'm afraid I can't do that " + getpass.getuser()
        self.assertEqual(answer, answerString)