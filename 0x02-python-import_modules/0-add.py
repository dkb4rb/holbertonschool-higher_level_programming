#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of the var a and b"""
    from add_0 import add

    a = 1
    b = 2
    rslt = add(a, b)
    print("{} + {} = {:d}".format(a, b, rslt))
