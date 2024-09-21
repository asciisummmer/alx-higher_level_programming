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
        elif w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Compute area of reactangle
        """
        return self.__width * self.__height

    def display(self):
        """ Display rectangle
        """
        for i in range(0, self.__y):
            print()

        line = "#" * self.__width
        line = " " * self.__x + line
        for i in range(0, self.__height):
            print(line)

    def __str__(self):
        res = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
        res += f"{self.__width}/{self.__height}"
        return res

    def update(self, *args, **kwargs):
        """ Update Rectangle values
        """
        if args is not None:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Class to dictionnary
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
