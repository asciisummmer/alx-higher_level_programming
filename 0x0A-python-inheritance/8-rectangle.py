#!/usr/bin/python3
"""Module to define Rectangle class."""


class Rectangle(BaseGeometry):
    """ Module to represent Rectangle

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
    """

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
