from question_answer import QA
from unittest import TestCase
import time
import random
import mock
from ReqTracer import requirements
from main import Interface
from answer_funcs import get_number_seq
from answer_funcs import threaded_counter

class PerformQA2(TestCase):

    def setUp(self):
        from answer_funcs import num_getter
        self.method2 = get_number_seq

    def tearDown(self):
        from answer_funcs import num_getter
        num_getter.stop()

    def test_num_total(self):
        from answer_funcs import threaded_counter
        mynum = threaded_counter()
        mynum.run()
        self.method2(0)
        num = mynum.num_indexes
        self.assertEqual(num, 100)

    @requirements(['#0036'])
    def test_num_is_accurate(self):
        from answer_funcs import threaded_counter
        mynum = threaded_counter()
        mynum.run()
        answer = mynum.sequence[50]
        self.assertEqual(answer, 50)

    @requirements(['#0037'])
    def test_generates_only_100(self):
        from answer_funcs import threaded_counter
        mynum = threaded_counter()
        mynum.run()
        self.method2(0)
        answer = mynum.num_indexes
        self.assertEqual(answer, 100)
        self.assertLess(answer, 101)

    @requirements(['#0035'])
    def test_num_is_fast(self):
        from answer_funcs import threaded_counter
        mynum = threaded_counter()
        time1 = time.time()
        mynum.run()
        time2 = time.time()
        timefinal = time2 - time1
        self.assertLess(timefinal, 5)

    @requirements(['#0038'])
    def test_num_fast_fetch(self):
        from answer_funcs import threaded_counter
        mynum = threaded_counter
        self.method2(0)
        time.sleep(5)
        time1 = time.time()
        self.method2(50)
        time2 = time.time()
        timefinal = time2 - time1
        self.assertLess(timefinal, .05)
        