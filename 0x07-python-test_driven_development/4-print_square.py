#!/usr/bin/python3
""" Module supplies function to say my name.
    Module to describe how to say my name.
"""


def print_square(size):
    """
        Function to print square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    line = ["#" for i in range(0, size)]
    line = "".join(line)
    for i in range(0, size):
        print(line)
