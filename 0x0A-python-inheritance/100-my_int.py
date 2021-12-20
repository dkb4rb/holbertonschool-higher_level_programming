#!/usr/bin/python3
# 100-my_int.py
# Juan Duque <3428@holbertonsschool.com>
""" Define new class calling MyInt"""


class MyInt(int):
    """ Operator rebeld revert == to !="""

    def __ne__(self, value):
        """No is equal if retur True is reversed did not?"""
        return self.real == value

    def __eq__(self, value):
        """If is equal return True is False reversed did not?"""
        return self.real != value
