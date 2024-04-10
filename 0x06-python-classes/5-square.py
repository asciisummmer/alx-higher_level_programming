#!/usr/bin/python3
"""Module to create Square"""


class Square:
    """ Class to create Square """
    def __init__(self, size=0):
        self.size = size
        """ Create new instance of square

        Args:
            size(int): Size of square
        """

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
