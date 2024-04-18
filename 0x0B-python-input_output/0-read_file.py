#!/usr/bin/python3
"""Module to read in filename"""


def read_file(filename=""):
    """ Read file.

    Args:
        filename (str): path of filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
