#!/usr/bin/python3

"""Module to load json"""

import json


def save_to_json_file(my_obj, filename):
    """function to write in file

    Args:
        filename (str): path of file "".
        my_obj (str): object to write in file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
