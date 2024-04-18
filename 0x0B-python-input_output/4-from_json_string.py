#!/usr/bin/python3

"""Module to load json"""

import json


def from_json_string(my_obj):
    """decoding object from json string.

    Args:
        my_obj (object): object to deserialize
    Return:
        my_obj to decoding
    """
    return json.loads(my_obj)
