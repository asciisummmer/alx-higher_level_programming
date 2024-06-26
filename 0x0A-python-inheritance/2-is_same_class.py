#!/usr/bin/python3
""" Module to use type function"""


def is_same_class(obj, a_class):
    """ Verify class of object

    Args:
        obj: object to verify class
        a_class: class to verify

    Returns:
        True if is same class otherwise false
    """
    if type(obj) is a_class:
        return True
    return False
