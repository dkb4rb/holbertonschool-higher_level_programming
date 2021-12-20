#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    arfg = "argument"
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} {}s.".format(argc, arfg))
    elif argc == 1:
        print("{} {}:".format(argc, arfg))
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
