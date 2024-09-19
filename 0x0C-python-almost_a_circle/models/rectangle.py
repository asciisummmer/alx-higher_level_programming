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
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, w):
        self.__width = w

    @height.setter
    def height(self, h):
        self.__height = h

    @x.setter
    def cord_x(self, x):
        self.__x = x

    @y.setter
    def cord_y(self, y):
        self.__y = y
