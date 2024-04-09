#!/usr/bin/python3

"""Module to create Square"""


class Square:
    """ Class to create Square """

    def __init__(self, size=0):
        """Initialize  square

        Args:
            size (int): Size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
