#!/usr/bin/python3
"""Module to create Square"""


class Square:
    """ Class to create Square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        """ Create new instance of square

        Args:
            size(int): Size of square
        """

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
           len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        for y in range(self.position[1]):
            print()
        for i in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
