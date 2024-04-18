#!/usr/bin/python3
"""Module to run function"""


def read_file(filename=""):
    """ Read file.

    Args:
        filename (str): path of filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
