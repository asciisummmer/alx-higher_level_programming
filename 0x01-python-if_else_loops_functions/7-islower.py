#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if 122 >= ascii_value >= 97:
        return True
    else:
        return False
