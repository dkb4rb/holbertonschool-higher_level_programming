#!/usr/bin/python3
# 0-safe_print_list.py


def safe_print_list(my_list=[], x=0):

    sum = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            sum += 1
        except IndexError:
            break
    print("")
    return (sum)
