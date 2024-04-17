#!/usr/bin/python3
"""Module to define Rectangle class."""


class Rectangle(BaseGeometry):
    """ Module to represent Rectangle

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        __width = super().integer_validator(width, "width")
        __height = self().integer_validator(height, "height")
