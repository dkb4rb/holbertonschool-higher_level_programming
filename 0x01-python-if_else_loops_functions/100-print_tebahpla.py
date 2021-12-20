#!/usr/bin/python3
for x in range(122, 96, -1):
    number = x
    if number % 2 != 0:
        number -= 32
    print("{}".format(chr(number)), end="")
