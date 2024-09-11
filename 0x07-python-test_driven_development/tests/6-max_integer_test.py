#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(max_integer([1, 2, 10, 5]), 10)

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -2, -10, -15]), -1)

    def test_null_list(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_shuffle_list(self):
        self.assertEqual(max_integer([1, -2, -10, 5, 25, -100, 40]), 40)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
