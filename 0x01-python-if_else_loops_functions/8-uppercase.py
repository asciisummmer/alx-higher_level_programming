#!/usr/bin/python3
def uppercase(str):
    for character in str:
        print("{}".format((chr(ord(character) - 32) if
                           ord(character) >= 97 and ord(character) <= 122 else 
                           character)), end="")
    print()
