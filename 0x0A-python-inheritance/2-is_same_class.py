#!/usr/bin/python3
# 2-is_same_class.py
# Juan Duque <3428@holbertonschool.com>
""" Define new function """


def is_same_class(obj, a_class):
    """ Verify if obj is instance of the a_class"""
    if type(obj) is a_class:
        return True
    return False
