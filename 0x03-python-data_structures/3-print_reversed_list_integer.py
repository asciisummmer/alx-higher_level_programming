#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    tmp = my_list[:]
    tmp.reverse()
    for i in tmp:
        print("{:d}".format(i))
