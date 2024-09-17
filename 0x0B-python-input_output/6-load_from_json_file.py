#!/usr/bin/python3

"""Module to load json"""

import json


def load_from_json_file(filename):
    """function to write in file

    Args:
        filename (str): path of file "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        x = json.load(f)
        return x
