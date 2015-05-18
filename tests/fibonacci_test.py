from question_answer import QA
from unittest import TestCase
import time
import random
import mock
from ReqTracer import requirements
from main import Interface
from answer_funcs import get_fibonacci_seq
from answer_funcs import FibSeqFinder


class FibonacciQA(TestCase):

    def setUp(self):
        from answer_funcs import seq_finder
        self.method = get_fibonacci_seq

    def tearDown(self):
        from answer_funcs import seq_finder
        seq_finder.stop()

    @requirements(['#0028'])
    def test_fib_return_value(self):
        from answer_funcs import seq_finder
        self.method(0)
#        myInterface = Interface()
        time.sleep(5)
#        answer = myInterface.ask("What is the 10 digit of the Fibonacci sequence?")
        answer = self.method(10)
        self.assertEqual(answer, 55)

    @requirements(['#0029'])
    def test_fib_wait_cool(self):
        from random import randint
        random.randint = mock.Mock(return_value = 1)
        answer = self.method(1000)
        answer2 = "cool your jets"
        self.assertEqual(answer,answer2)

    @requirements(['#0029'])
    def test_fib_wait_second(self):
        from random import randint
        random.randint = mock.Mock(return_value = 1.01)
        answer = self.method(1000)
        answer2 = "One second"
        self.assertEqual(answer,answer2)

    @requirements(['#0029'])
    def test_fib_wait_second2(self):
        from random import randint
        random.randint = mock.Mock(return_value = 3.99)
        answer = self.method(1000)
        answer2 = "One second"
        self.assertEqual(answer,answer2)

    @requirements(['#0029'])
    def test_fib_wait_thinking(self):
        from random import randint
        random.randint = mock.Mock(return_value = 4)
        answer = self.method(1000)
        answer2 = "Thinking..."
        self.assertEqual(answer,answer2)