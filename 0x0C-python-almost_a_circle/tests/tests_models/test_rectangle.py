#!/usr/bin/python3
# test_rectangle.py
# Juan Duque <3428@holbertonschool.com>
""" Import files to inheritance for your value"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
""" Define new Class Father"""


class test_rectangles(unittest.TestCase):
    """ This is reference to class Father"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)


""" Define new class testing"""


class test_rectangle_str(unittest.TestCase):
    """ This is new referente to rectangle class instaciate"""

    def test_is_type_string(self):
        with self.assertRaises(TypeError):
            Rectangle("10")


class test_rectangle_float(unittest.TestCase):
    """ This is new reference to float testing rectangle"""

    def test_is_type_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1.0)
            Rectangle()


if __name__ == "__main__":
    unittest.main()
