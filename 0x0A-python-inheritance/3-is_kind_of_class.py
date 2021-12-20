#!/usr/bin/python3
# 3-is_kind_of_class.py
# Juan Duque <3428@holbertonschool.com>
""" Write a function that returns True if the object is an
    instance of, or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """ Compare
        Return True if obj is insinstance of a_class  """
    if isinstance(obj, a_class):
        return True
    return False
