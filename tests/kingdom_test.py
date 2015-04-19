"""
Test for Lab2.kingdom
"""
import kingdom
import logging
from unittest import TestCase
from testfixtures import LogCapture

class KingdomTest(TestCase):

    def test_kingdom_isBreached_True(self):
        
        testKingdom = kingdom.Kingdom()
        testKingdom.setIsBreached(True)
        result = testKingdom.getIsBreached()
        self.assertEqual(result, True)

    def test_kingdom_isBreached_False(self):
        testKingdom = kingdom.Kingdom()
        testKingdom.setIsBreached(False)
        result = testKingdom.getIsBreached()
        self.assertEqual(result, False)

    def test_kingdom_logger_debug(self):
        testKingdom = kingdom.Kingdom()
        with LogCapture() as log:
            testKingdom.writeDebugLogger()
        log.check(('kingdom', 'DEBUG', 'kingdom debug test'))

    def test_kingdom_logger_info(self):
        testKingdom = kingdom.Kingdom()
        with LogCapture() as log:
            testKingdom.writeInfoLogger()
        log.check(('kingdom', 'INFO', 'kingdom info test'))

    def test_kingdom_multi_logging_no_filter(self):
        testKingdom = kingdom.Kingdom()
        with LogCapture() as log:
            testKingdom.writeDualLogger()
        log.check(('kingdom', 'DEBUG', 'kingdom debug test'),('kingdom', 'INFO', 'kingdom info test'))

    def test_kingdom_multi_logging_plus_filter(self):
        testKingdom = kingdom.Kingdom()
        with LogCapture('kingdom', level = logging.INFO) as log:
            testKingdom.writeDualLogger()
        log.check(('kingdom', 'INFO', 'kingdom info test'))

    def test_add_threat(self):
        testKingdom = kingdom.Kingdom()
        testOrc = testKingdom.addOrc(1,2,0)
        self.assertNotEqual(testOrc, None)

    def test_add_threat_count(self):
        crapKingdom = kingdom.Kingdom()
        crapKingdom.addOrc(1,2,0)
        self.assertEqual(len(crapKingdom.orcList), 1)

    def test_create_threats(self):
        testKingdom = kingdom.Kingdom()
        orcList = testKingdom.createOrcList(20)
        self.assertNotEqual(orcList, None)

    def test_create_threats_count(self):
        testKingdom = kingdom.Kingdom()
        orcList = testKingdom.createOrcList(20)
        self.assertEqual(len(orcList), 20)

    def test_remove_by_id(self):
        testKingdom = kingdom.Kingdom()
        testKingdom.createOrcList(20)
        result = testKingdom.removeOrc(10)
        self.assertEqual(result, True)

    def test_fail_remove_by_id(self):
        testKingdom = kingdom.Kingdom()
        testKingdom.createOrcList(20)
        result = testKingdom.removeOrc(100)
        self.assertEqual(result, False)

    def test_threat_count_after_remove(self):
        testKingdom = kingdom.Kingdom()
        testKingdom.createOrcList(20)
        testKingdom.removeOrc(10)
        self.assertEqual(len(testKingdom.orcList), 19)

    def test_threat_priority_set_one(self):
        testKingdom = kingdom.Kingdom()
        testKingdom.createOrcList(20)
        testKingdom.setPriority(3, 1)
        self.assertEqual(testKingdom.orcList[3].priority, 1)
