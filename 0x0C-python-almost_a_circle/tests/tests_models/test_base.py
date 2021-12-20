#!/usr/bin/python3
# test_base.py
# Juan Duque <3428@holbertonschool.com>
""" Impor the libraries and modules to testing 

    Unittest Modules:
    """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_base(unittest.TestCase):

    def test_not_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_args(self):
        b1 = Base(id=10)
        b2 = Base(id=100)
        self.assertIsNotNone(b1.id, b2.id)


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_new_Rectangle(self):
        rectangle = Rectangle(width=10, height=20, x=10, y=10)
        rectangle2 = Rectangle(width=23413242413214331211432,
                               height=1234123412, x=3214123, y=1523)


class test_is_types(unittest.TestCase):
    """This is new reference to type class"""

    def test_is_float(self):
        if isinstance(self, float):
            raise TypeError

    def test_is_instance(self):
        if isinstance(self, str):
            raise TypeError

    def test_is_int(self):
        if isinstance(self, int):
            raise TypeError


if __name__ == "__main__":
    unittest.main()
