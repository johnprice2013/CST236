"""
Test for source.interface
"""
import interface
import kingdom
from unittest import TestCase

class InterfaceTest(TestCase):

    def test_interface_created(self):
        obj = interface.interface()
        self.assertNotEqual(None, obj)

    def test_interface_getInput(self):
        obj = interface.interface()
        result = obj.getInput("X")
        self.assertEqual(result, "X")

    def test_interface_X_quits(self):
        obj = interface.interface()
        input = "X"
        self.assertRaises(SystemExit, obj.handleInput, input)

    def test_interface_quit_program(self):
        obj = interface.interface()
        self.assertRaises(SystemExit, obj.quitProgram)

    def test_interface_non_X_or_question_input(self):
        obj = interface.interface()
        result = obj.handleInput('h')
        self.assertEqual(result, 'not valid')

    def test_interface_get_commands(self):
        obj = interface.interface()
        result = obj.showCommands()
        self.assertEqual(result, 'X = quit, I = identify threats, U = useless command, ? = show commands, ENTer the trees = remove all threats')

    def test_interface_question_show_commands(self):
        obj = interface.interface()
        result = obj.handleInput('?')
        self.assertEqual(result, 'X = quit, I = identify threats, U = useless command, ? = show commands, ENTer the trees = remove all threats')

    def test_interface_remove_all_threats(self):
        obj = interface.interface()
        testKingdom = kingdom.Kingdom()
        testKingdom.createOrcList(20)
        obj.handleInput('ENTer the trees',testKingdom)
        self.assertEqual(len(testKingdom.orcList), 0)