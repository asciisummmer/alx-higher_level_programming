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
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): value to check
            name (str): name of variable of value

        Returns:
            return value if integr greather than zero

        Raises:
            TypeError: if value not integer
            ValueError: if value less than zero
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be positive integer".format(name))
        else:
            return value
