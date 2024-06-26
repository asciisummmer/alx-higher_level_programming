#!/usr/bin/python3
"""Module to create Square"""


class Square:
    """ Class to create Square """
    def __init__(self, size=0):
        """ Create new instance of square

        Args:
            size(int): Size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
