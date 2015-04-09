"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1,1,2)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_is_instance_list(self):
        myList = [1,2,3]
        result = get_triangle_type(myList)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_is_instance_tuple(self):
        myTup = 1,2,3
        result = get_triangle_type(myTup)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_is_instance_dict(self):
        myDict = dict(one = 1, two = 2, five = 5)
        result = get_triangle_type(myDict)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_is_invalid_zero(self):
        result = get_triangle_type(0,0,0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_is_invalid_type_string(self):
        result = get_triangle_type("you", "are", "awesome")
        self.assertEqual(result, 'invalid')