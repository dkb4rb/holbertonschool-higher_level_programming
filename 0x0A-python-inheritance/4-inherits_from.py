#!/usr/bin/python3
# 4-inherits_from.py
# Juan Duque <3428@holbertonschool.com>
""" Define New Function
    returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """ Evaluate if type of the obj is one subclass of the a_class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
