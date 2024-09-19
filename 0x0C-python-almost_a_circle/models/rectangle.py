#!/usr/bin/python3
""" Module to define Rectangle

"""

from .base import Base


class Rectangle(Base):
    """Class to define rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): position of rectangle
        y (int): position of rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): position of rectangle
        y (int): position of rectangle

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width():
        return self.__width

    @property
    def height():
        return self.__height

    @width.setter
    def width(w):
        self.__width = w

    @height.setter
    def height(h):
        self.__height = h
