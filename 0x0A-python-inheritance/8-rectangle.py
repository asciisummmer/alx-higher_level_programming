#!/usr/bin/python3
"""Module to define Rectangle class."""


class Rectangle(BaseGeometry):
    """ Module to represent Rectangle

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
    """

    def __init__(self, width, height):
        
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)
        super().__init__()
