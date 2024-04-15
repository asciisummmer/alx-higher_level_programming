#!/usr/bin/python3
#!/usr/bin/python3
""" Module to use isinstance function"""


def inherits_from(obj, a_class):
    """ Verify class of object

    Args:
        obj: object to verify class
        a_class: class to verify

    Returns:
        True if is same class otherwise false
    """
    return isinstance(obj, a_class)
