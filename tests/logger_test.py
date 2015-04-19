import orc
import kingdom
import logging
from testfixtures import LogCapture
from unittest import TestCase

class LoggingTest(TestCase):
    def test_multi_class_filter(self):
        testOrc = orc.Orc(1,2)
        testKingdom = kingdom.Kingdom()
        with LogCapture('kingdom', level = logging.INFO) as log:
            testKingdom.writeDualLogger()
            testOrc.writeInfoLogger()
        log.check(('kingdom', 'INFO', 'kingdom info test'))