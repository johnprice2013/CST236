from question_answer import QA
from main import Interface
from unittest import TestCase
import time
import getpass
from ReqTracer import requirements
import mock
from answer_funcs import get_other_users

class TestQA(TestCase):

    @requirements(['#0017'])
    def test_conversion_question(self):
        myInterface = Interface()
        feet = float(5280)
        string = "What is " + str(feet) + " feet in miles?"
        answer = myInterface.ask(string)
        self.assertEqual(answer, "1.0 miles")



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

    @requirements(['#0022'])
    def test_where_am_i(self):
        myInterface = Interface()
        answer = myInterface.ask("Where am I?")
        self.assertEqual(answer, "lab5")

    @requirements(['#0023'])
    def test_where_are_you(self):
        myInterface = Interface()
        answer = myInterface.ask("Where are you?")
        self.assertEqual(answer, "https://github.com/johnprice2013/CST236.git")

    @requirements(['#0024','#0027'])
    def test_who_else(self):
        myInterface = Interface()
        myInterface.ask = mock.Mock(return_value = "bob$steven")
        answer = myInterface.ask("Who else is here?")
        self.assertEqual(answer, "bob$steven")

    @requirements(['#0025', '#0026'])
    def test_get_other_users(self):
        method = get_other_users
        method.socket = mock.Mock()
        method.socket.socket = mock.Mock()
        method.socket.socket("192.168.64.3, 1337")
        method.socket.socket.send = mock.Mock(return_value = "bob$steven")
        answer = method.socket.socket.send("Who?")
        self.assertEqual(answer, "bob$steven")

    @requirements(['#0027'])
    def test_get_other_users_failed(self):
        method = get_other_users
        method = mock.Mock(return_value = "IT'S A TRAAAPPPP")
        answer = method("failed")
        self.assertEqual(answer, "IT'S A TRAAAPPPP")

