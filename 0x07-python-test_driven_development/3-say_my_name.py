#!/usr/bin/python3

""" Module supplies function to divide matrix.

    Module to describe how to divide matrix.
"""


def say_my_name(first_name, last_name=""):
    """
        Fuction to display name

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
