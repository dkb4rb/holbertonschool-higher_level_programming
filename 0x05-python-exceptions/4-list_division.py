#!/usr/bin/python3
# File: 4-list-division.py
# Author: Juan Duque


def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(0, list_length):
        try:
            rslt_D = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
            rslt_D = 0
        except (ZeroDivisionError):
            print("division by 0")
            rslt_D = 0
        except (IndexError):
            print("out of range")
            rslt_D = 0
        finally:
            new_list.append(rslt_D)
    return (new_list)
