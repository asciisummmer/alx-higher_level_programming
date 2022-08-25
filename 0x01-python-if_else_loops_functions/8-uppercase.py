#!/usr/bin/python3
def uppercase(str):
    for value in str:
        ascii_value = ord(value)
        char = value
        if 122 >= ascii_value >= 97:
            char = chr(ascii_value - 32)
        print("{}".format(char), end="")
    print()
