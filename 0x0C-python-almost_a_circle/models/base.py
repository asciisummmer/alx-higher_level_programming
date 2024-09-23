#!/usr/bin/python3
""" Module to describe base of model

"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None or list_objs == []:
            with open(f"{str(cls.__name__)}.json", "w") as f:
                f.write("[]")
        else:
            list_objs_dict = [elt.to_dictionary() for elt in list_objs]
            with open(f"{str(cls.__name__)}.json", "w") as f:
                f.write(cls.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or \
           json_string == '[]' or json_string == '':
            return []
        return json.loads(json_string)
