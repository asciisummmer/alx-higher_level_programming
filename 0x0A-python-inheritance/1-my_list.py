#!/usr/bin/python3
""" Inherit list class"""

class MyList(list):
    """Class to use list"""
    def print_sorted(self):
        """Print sorted list
        """
        print(sorted(self))
