import sys
import pywinauto
from pywinauto import application
from unittest import TestCase


class apptest(TestCase):

    def setUp(self):
        self.app = application.Application()
        self.app.start_("C:\Users\John\Downloads\SharpTona.exe")
        self.sharp = self.app.sharpTona
        
    def tearDown(self):
        self.sharp.TypeKeys("%{F4}")

    def test_win_title(self):
        answer = self.sharp.Texts()[0]
        self.assertEqual(answer, u'SharpTona')

    def test_answer_label(self):
        answer = self.sharp['Answer:'].Texts()[0]
        self.assertEqual(answer, u'Answer: ')

    def test_question_label(self):
        answer = self.sharp['Question:'].Texts()[0]
        self.assertEqual(answer, u'Question:')

    def test_ask_default(self):
        
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u'42')

    def test_disabled_teach(self):
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer, False)

    def test_disabled_correct(self):
        answer = self.sharp['Correct'].IsEnabled()
        self.assertEqual(answer, False)

    def test_no_question(self):
        self.sharp['Ask'].Click()
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u'Was that a question?')

    def test_input_after_ask(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('Editing')
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u'Editing')

    def test_correct_disable_correct(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('Editing')

        answer = self.sharp['Correct'].IsEnabled()
        self.assertEqual(answer, True)

        self.sharp['Correct'].Click()

        answer = self.sharp['Correct'].IsEnabled()
        self.assertEqual(answer, False)


    def test_correct_disable_teach(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('Editing')

        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer, False)

        self.sharp['Correct'].Click()

        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer, False)


    def test_correct_disable_answer(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('Editing')

        answer = self.sharp['Answer:Edit'].IsEnabled()
        self.assertEqual(answer, True)

        self.sharp['Correct'].Click()

        answer = self.sharp['Answer:Edit'].IsEnabled()
        self.assertEqual(answer, False)

    def test_correct_correct_update(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('What is the answer to everything?', with_spaces = True)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('Editing')
        self.sharp['Correct'].Click()
        self.sharp['Ask'].Click()
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u'Editing')

    def test_unknown_question_teach_enabled(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('Who are you?', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,False)
        self.sharp['Ask'].Click()
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u"I don't know please teach me.")
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,True)

    def test_teach_set_answer(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('Who are you?', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,False)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('I am god.', with_spaces = True)
        self.sharp['Teach'].Click()
        self.sharp['Ask'].Click()
        answer = self.sharp['Answer:Edit'].Texts()[0]
        self.assertEqual(answer, u'I am god.')

    def test_teach_disable_teach(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('Who are you?', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,False)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('I am god.', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer, True)
        self.sharp['Teach'].Click()
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer, False)

    def test_teach_disable_answer(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('Who are you?', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,False)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('I am god.', with_spaces = True)
        answer = self.sharp['Answer:Edit'].IsEnabled()
        self.assertEqual(answer, True)
        self.sharp['Teach'].Click()
        answer = self.sharp['Answer:Edit'].IsEnabled()
        self.assertEqual(answer, False)

    def test_teach_disable_correct(self):
        self.sharp['Question:Edit'].Click()
        self.sharp.TypeKeys('Who are you?', with_spaces = True)
        answer = self.sharp['Teach'].IsEnabled()
        self.assertEqual(answer,False)
        self.sharp['Ask'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].Click()
        self.sharp['Answer:Edit'].SetText("")
        self.sharp.TypeKeys('I am god.', with_spaces = True)
        answer = self.sharp['Correct'].IsEnabled()
        self.assertEqual(answer, False)
        self.sharp['Teach'].Click()
        answer = self.sharp['Correct'].IsEnabled()
        self.assertEqual(answer, False)