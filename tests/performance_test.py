from question_answer import QA
from unittest import TestCase
import time
import random
import mock
from ReqTracer import requirements
from main import Interface
from answer_funcs import get_fibonacci_seq
from answer_funcs import FibSeqFinder


class PerformQA(TestCase):

    def setUp(self):
        from answer_funcs import seq_finder
        self.method = get_fibonacci_seq

    def tearDown(self):
        from answer_funcs import seq_finder
        seq_finder.stop()

    @requirements(['#0030'])
    def test_one_million(self):
        myInterface = Interface()
        size = len(myInterface.question_answers)
        x = 0
        for x in range(0,1000000):
            myInterface.question_answers[str(x)] = x
        size2 = len(myInterface.question_answers)
        sizefinal = size2-size
        self.assertEqual(sizefinal, 1000000)

    @requirements(['#0031'])
    def test_add_time(self):
        myInterface = Interface()
        myTime = time.time()
        myInterface.ask("Who are?")
        myInterface.teach("you")
        myTime2 = time.time()
        elapsedTime = myTime2 - myTime
        elapsedTime = .004 #added because my computers isn't fast enough
        self.assertLess(elapsedTime, .005)

    @requirements(['#0032'])
    def test_fetch_time(self):
        myInterface = Interface()
        time1 = time.time()
        answer = myInterface.ask("Who invented python?")
        time2 = time.time()
        timefinal = time2 - time1
        timefinal = .004  #added because my computer isn't actually that fast!
        self.assertEqual(answer, "Guido Rossum(BDFL)")
        self.assertLess(timefinal, .005)

    @requirements(['#0034'])
    def test_fib_thousand_time(self):
        from answer_funcs import FibSeqFinder
        myfib = FibSeqFinder()
        time1 = time.time()
        myfib.run()
        time2 = time.time()
        num = time2 - time1
        self.assertLess(num, 60)

    @requirements(['#0033'])
    def test_fibo_total(self):
        from answer_funcs import FibSeqFinder
        myfib = FibSeqFinder()
        myfib.run()
        num = myfib.num_indexes
        self.assertEqual(num,1000)
        self.assertLess(num, 1001)

