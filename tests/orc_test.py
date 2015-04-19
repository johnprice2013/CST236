"""
Test for Lab2.orc
"""
import orc
from unittest import TestCase

class TestOrc(TestCase):

    def test_orc_distance(self):
        testOrc = orc.Orc(1, 2, 0)
        result = testOrc.getDistance()
        self.assertEqual(result, 1)

    def test_orc_velocity(self):
        testOrc = orc.Orc(1, 2, 0)
        result = testOrc.getVelocity()
        self.assertEqual(result, 2)

    def test_orc_type(self):
        testOrc = orc.Orc(1,2,0)
        result = testOrc.getType()
        self.assertEqual(result, 'heavy')

    def test_orc_type_last(self):
        testOrc = orc.Orc(1,2,7)
        result = testOrc.getType()
        self.assertEqual(result, 'fatty')

    def test_orc_id(self):
        testOrc = orc.Orc(1,2,0)
        result = testOrc.getId()
        self.assertEqual(result, 0)
