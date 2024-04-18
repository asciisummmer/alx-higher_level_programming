#!/usr/bin/python3
"""Module to write in filename"""


def write_file(filename="", text=""):
    """function to write in file

    Args:
        filename (str): path of file "".
        text (str): text to write in file.

    Returns:
        int: number of character writting
    """
    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
        return nb_characters
