#!/usr/bin/python3

# File: 101-safe_function.py
# Author: Juan Duque

import sys


def safe_function(fct, *args):
    try:
        rslt = fct(*args)
        return (rslt)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
