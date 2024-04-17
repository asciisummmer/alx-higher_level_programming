#!/usr/bin/python3

"""Module to define Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class to represent square."""

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def area(self):
        return "[square] {}/{}".format(self.__size, self.__size)
