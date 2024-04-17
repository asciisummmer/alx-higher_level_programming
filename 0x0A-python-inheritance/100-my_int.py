#!/usr/bin/python3
"""Module to re implement Int"""


class MyInt(int):
    """Class to represent integer"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if self.value == other:
            print("ho")
            print(other)
            return False
        else:
            return True

    def __ne__(self, other):
        if self.value != other:
            return False
        else:
            return True
