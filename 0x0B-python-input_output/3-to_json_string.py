#!/usr/bin/python3

"""Module to create json"""

import json


def to_json_string(my_obj):
    """Encoding object to json string.

    Args:
        my_obj (object): object to serialize
    Return:
        my_obj encoding
    """
    return json.dumps(my_obj)
