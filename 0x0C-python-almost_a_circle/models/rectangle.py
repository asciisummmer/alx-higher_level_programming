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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(w) is not int:
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise TypeError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise TypeError("y must be >= 0")
        else:
            self.__y = value
