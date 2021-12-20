#!/usr/bin/python3
# 10-square.py
# Juan Duque <3428@holbertonschool.com>
"""
Import the modul what contain the new rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Rectangle subclass Square."""


class square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
