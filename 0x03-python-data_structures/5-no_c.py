#!/usr/bin/python3

def no_c(my_string):
    return "".join([car for car in my_string if car not in "cC"])
