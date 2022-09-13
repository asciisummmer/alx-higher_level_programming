#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            n = my_list[i]
            print("{:d}".format(n), end="")
        except:
            print()
            return i
    print()
    return i + 1
