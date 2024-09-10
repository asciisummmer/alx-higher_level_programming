#!/usr/bin/python3

""" Module supplies function print text.
    Module to describe how to print text.
"""


def text_indentation(text):
    """
        Function to transform text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    translated_text = text.replace("?", "?\n\n")
    translated_text = translated_text.replace(".", ".\n\n")
    translated_text = translated_text.replace(":", ":\n\n")

    translated_text = translated_text.replace("?\n\n ", "?\n\n")
    translated_text = translated_text.replace(":\n\n ", ":\n\n")
    translated_text = translated_text.replace(".\n\n ", ".\n\n")

    print(translated_text)
