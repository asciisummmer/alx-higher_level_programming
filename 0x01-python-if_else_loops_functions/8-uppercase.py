#!/usr/bin/python3
def uppercase(str):
    for value in str:
        ascii_value = ord(value)
        if 122 >= ascii_value >= 97:
            print("{}".format(chr(ascii_value - 32)), end="")
        else:
            print("{}".format(value), end="")
    print()
