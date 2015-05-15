from question_answer import QA
from main import Interface
from unittest import TestCase
from ReqTracer import requirements

class TestQA(TestCase):

    @requirements(['#0001'])
    def test_tries_to_answer(self):
        myInterface = Interface()
        answer = myInterface.ask("string?")
        assert isinstance(answer, str)

    @requirements(['#0002'])
    def test_try_keywords_who(self):
        myInterface = Interface()
        answer = myInterface.ask("Who am I?")
        assert isinstance(answer, str)

    @requirements(['#0002'])
    def test_try_keywords_what(self):
        myInterface = Interface()
        answer = myInterface.ask("What am I?")
        assert isinstance(answer, str)

    @requirements(['#0002'])
    def test_try_keywords_where(self):
        myInterface = Interface()
        answer = myInterface.ask("Where am I?")
        assert isinstance(answer, str)

    @requirements(['#0002'])
    def test_try_keywords_how(self):
        myInterface = Interface()
        answer = myInterface.ask("How am I?")
        assert isinstance(answer, str)

    @requirements(['#0002'])
    def test_try_keywords_why(self):
        myInterface = Interface()
        answer = myInterface.ask("Why am I?")
        assert isinstance(answer, str)

    @requirements(['#0003'])
    def test_bad_question_start(self):
        myInterface = Interface()
        answer = myInterface.ask("Bob is great>")
        self.assertEqual(answer, "Was that a question?")

    @requirements(['#0004'])
    def test_no_question_mark(self):
        myInterface = Interface()
        answer = myInterface.ask("Who")
        self.assertEqual(answer, "Was that a question?")