#!/usr/bin/python3
""" Module to use isinstance function"""


def is_same_class(obj, a_class):
    """ Verify class of object

    Args:
        obj: object to verify class
        a_class: class to verify

    Returns:
        True if is same class otherwise false
    """
    if type(obj) == a_class:
        return True
    return False

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
