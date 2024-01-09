#!/usr/bin/python3
"""Def imprt."""


import unittest
from max_integer_module import max_integer  # Replace 'your_module' with the actual name of your module or file

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_max_integer_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Maximum integer is expected to be 4")

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-5, -3, -9, -2]), -2, "Maximum integer is expected to be -2")

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 0, 5, -2]), 5, "Maximum integer is expected to be 5")

    def test_max_integer_duplicate(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3, "Maximum integer is expected to be 3 for duplicate values")

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([42]), 42, "Maximum integer is expected to be 42 for a single element list")

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 1.75, 1.0]), 2.5, "Maximum float is expected to be 2.5")

    def test_max_integer_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])  # List with mixed types should raise TypeError

    def test_max_integer_non_iterable(self):
        with self.assertRaises(TypeError):
            max_integer("not_a_list")  # Non-iterable input should raise TypeError

if __name__ == '__main__':
    unittest.main()