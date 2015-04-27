from question_answer import QA
from main import Interface
from unittest import TestCase

class TestQA(TestCase):

    def test_has_spaces(self):
        myInterface = Interface()
        myInterface.ask("What amI>")
        answer = myInterface.last_question
        self.assertEqual(answer, "What am I>")

    def test_answers_90_percent(self):
        myInterface = Interface()
        answer = myInterface.ask("How many seconds sinc>")
        self.assertEqual(answer, "42 seconds")

    def test_answers_number_removal_correct(self):
        myInterface = Interface()
        answer = myInterface.ask("What is feet in 5280 miles>")
        self.assertEqual(answer, '1.0')

    def test_answers_number_removal_question(self):
        myInterface = Interface()
        answer = myInterface.ask("What is feet in 234 miles>")
        answer = myInterface.last_question
        self.assertEqual(answer, "What is feet in miles")

    def test_valid_question_answer_return(self):
        myInterface = Interface()
        answer = myInterface.ask("How many seconds since>")
        self.assertEqual(answer, "42 seconds")

    def test_unknown_question(self):
        myInterface = Interface()
        answer = myInterface.ask("Who are you>")
        self.assertEqual(answer, "I don't know, please provide the answer")