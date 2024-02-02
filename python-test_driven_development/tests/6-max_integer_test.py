#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        """Test with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test with only one element in the list"""
        self.assertEqual(max_integer([1]), 1)

    def test_negative(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-2, -6, -1]), -1)

    def test_empty(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_none(self):
        """Test with None as input"""
        self.assertRaises(TypeError, max_integer([]), None)

if __name__ == '__main__':
    unittest.main()