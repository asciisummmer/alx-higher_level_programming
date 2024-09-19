#!/usr/bin/python3
""" Module to describe base of model

"""


class Base:
    """Class to define base of my class

    Args:
        id (int): identifier each instance

    Attributes:
        id (int): identifier each instance

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
