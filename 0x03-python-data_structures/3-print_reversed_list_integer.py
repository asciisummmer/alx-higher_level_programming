#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    max = len(my_list) - 1
    while max >= 0:
        print("{:d}".format(my_list[max]))
        max -= 1
