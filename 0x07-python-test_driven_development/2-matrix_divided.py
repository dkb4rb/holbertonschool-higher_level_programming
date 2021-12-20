#!/usr/bin/python3
# 0-add_integer.py
# Juan Duque <3428@holbertonschool.com>
"""Defines matrix integer addition function."""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l1 in matrix:
        if type(l1) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(l1)
        elif size != len(l1):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l1:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l1] for l1 in matrix]
