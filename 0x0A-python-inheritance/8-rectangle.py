#!/usr/bin/python3
"""Module to define Rectangle class."""


class Rectangle(BaseGeometry):
    __width = 0
    __height = 0

    def __init__(self, width, height):
        __width = self.integer_validator(width, "width")
        __height = self.integer_validator(height, "height")

    def integer_validator(self, value, name):
        ''' Verify value is integer and greather than zero

        Note:
        Args:
            value (int):
            name (str): 
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be positive integer".format(name))
        else:
            return value
