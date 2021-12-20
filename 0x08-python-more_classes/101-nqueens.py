#!/usr/bin/python3

import sys


def __init__(argc, **argv):
    print("argc : {:d}".format(argc))
    print("argv : {:s}".format(argv))
    return (0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
