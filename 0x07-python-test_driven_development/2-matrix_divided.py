#!/usr/bin/python3

""" Module supplies function to divide matrix.

    Module to describe how to divide matrix
"""


def matrix_divided(matrix, div):
    """
    function to divide matrix by integer

    """
    result = []
    new_line = []
    try:
        if type(matrix) is not list or type(matrix[0]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        size_row = len(matrix[0])
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for line in matrix:
            if type(line) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
of integers/floats"
                    )
            if (len(line) is not size_row):
                raise TypeError("Each row of the matrix must \
have the same size")
            for cel in line:
                if type(cel) is not int and type(cel) is not float:
                    raise TypeError(
                        "matrix must be a matrix (list of lists) \
of integers/floats"
                    )
                new_line.append(round(cel / div, 2))
            result.append(new_line.copy())
            new_line.clear()
        return result
    except IndexError:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
