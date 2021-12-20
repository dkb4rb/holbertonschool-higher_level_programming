#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p = "Last digit of"
i = "is"
less = "and is less than 6 and not 0"
greater = "and is greater than 5"
zero = "and is 0"
mod = abs(number) % 10

if number < 0:
    mod = -mod
if mod > 5:
    print(p, number, i, mod, greater)
elif mod == 0:
    print(p, number, i, mod, zero)
else:
    print(p, number, i, mod, less)
