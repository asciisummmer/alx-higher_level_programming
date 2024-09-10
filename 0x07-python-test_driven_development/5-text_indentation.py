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
    text_translation = str.maketrans({
        '. ': '.\n\n', '? ': '?\n\n', ': ': ':\n\n',
        '.': '.\n\n', '?': '?\n\n', ':': ':\n\n'})
    translated_text = text.translate(text_translation)
    print(translated_text)
