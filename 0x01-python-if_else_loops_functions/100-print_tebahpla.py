#!/usr/bin/python3

def print_tebahpla():
    value = ord('z')
    while(value >= ord('a')):
        if value % 2 == 0:
            value_to_print = chr(value)
        else:
            value_to_print = chr(value - 32)
        print("{}".format(value_to_print), end="")
        value -= 1
