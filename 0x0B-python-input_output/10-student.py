#!/usr/bin/python3

""" Create class
"""


class Student():
    """ Class to describe student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        result = {}
        if attrs is None:
            return self.__dict__
        else:
            value = self.__dict__
            for key in attrs:
                if key in value:
                    result[key] = value[key]
        return result
