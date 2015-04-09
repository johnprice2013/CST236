"""
Test for source.source2
"""
from source.source2 import get_quadrilateral_type
from unittest import TestCase

class TestGetQuadrilateralType(TestCase):

    def test_get_quadrilateral_square_all_int(self):
        result = get_quadrilateral_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rhombus_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4)
        self.assertEqual(result, 'rhombus')

    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(1,1,2,2)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_is_instance_list(self):
        myList = [1,2,1,2]
        result = get_quadrilateral_type(myList)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_is_instance_tuple(self):
        myTup = 1,2,2,1
        result = get_quadrilateral_type(myTup)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_is_instance_dict(self):
        myDict = dict(one = 1, two = 1, five = 1, eight = 1)
        result = get_quadrilateral_type(myDict)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_is_invalid_zero(self):
        result = get_quadrilateral_type(0,0,0,0)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_is_invalid_type_string(self):
        result = get_quadrilateral_type("you", "are", "really", "awesome")
        self.assertEqual(result, 'invalid')