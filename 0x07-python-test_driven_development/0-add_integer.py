#!/usr/bin/python3

""" Module supplies function to add two integer.

    Module to describe how to add two integer with
    function add_integer
"""

def add_integer(a, b=98):
    """Return add of a and b.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
