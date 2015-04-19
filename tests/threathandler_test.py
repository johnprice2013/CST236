import logging
import threathandler
import kingdom
from unittest import TestCase
class ThreatHandlerTest(TestCase):
    def test_threathandler_init(self):
        threatHandle = threathandler.ThreatHandler()
        self.assertNotEqual(threatHandle, None)
