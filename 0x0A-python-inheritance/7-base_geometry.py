#!/usr/bin/python3
"""Module to inherit class."""


class BaseGeometry:
    """Define class."""
    def area(self):
        """Methode to compute area

        Raises:
            Exception: not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Verify value is integer and greather than zero

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): value to check
            name (str): name of variable of value

        Returns:
            return value if integr greather than zero

        Raises:
            TypeError: if value not integer
            ValueError: if value less than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
