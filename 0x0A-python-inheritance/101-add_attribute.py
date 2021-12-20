#!/usr/bin/python3
# 101-add_attribute.py
# Juan Duque <3428@holbertonschool.com>

""" function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """ If not is one dict of the hasattar return else of te othewise
    return setattr"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
