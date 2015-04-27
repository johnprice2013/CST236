from question_answer import QA
from main import Interface
from unittest import TestCase

class TestQA(TestCase):

    def test_teach_func_exists(self):
        myInterface = Interface()
        "teach" in dir(Interface)
        self.assertEqual(True, "teach" in dir(Interface))

    def test_teach_func_works(self):
        myInterface = Interface()
        myInterface.ask("Who am I>")
        myInterface.teach("The very best")
        answer = myInterface.ask("Who am I>")
        self.assertEqual(answer, "The very best")

    def test_teach_no_question_provided(self):
        myInterface = Interface()
        answer = myInterface.teach("The very best")
        self.assertEqual(answer, "Please ask a question first")

    def test_teach_func_tried_twice(self):
        myInterface = Interface()
        myInterface.ask("Who am I>")
        myInterface.teach("The very best")
        answer = myInterface.teach("Not the very best")
        self.assertEqual(answer, "I don't know about that. I was taught differently")

    def test_teach_func_tried_twice_retains(self):
        myInterface = Interface()
        myInterface.ask("Who am I>")
        myInterface.teach("The very best")
        myInterface.teach("Not the very best")
        answer = myInterface.ask("Who am I>")
        self.assertEqual(answer, "The very best")
