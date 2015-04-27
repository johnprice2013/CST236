from question_answer import QA
from main import Interface
from unittest import TestCase

class TestQA(TestCase):

    def test_correct_func_exists(self):
        myInterface = Interface()
        "correct" in dir(Interface)
        self.assertEqual(True, "teach" in dir(Interface))

    def test_correct_func_works(self):
        myInterface = Interface()
        myInterface.ask("How many seconds since>")
        myInterface.correct("52 seconds")
        answer = myInterface.ask("How many seconds since>")
        self.assertEqual(answer, "52 seconds")

    def test_correct_no_question_provided(self):
        myInterface = Interface()
        answer = myInterface.correct("The very best")
        self.assertEqual(answer, "Please ask a question first")