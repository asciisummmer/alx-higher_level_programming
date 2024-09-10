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
    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size_row = len(matrix[0])
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for line in matrix:
        if type(line) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (len(line) != size_row):
            raise TypeError("Each row of the matrix must have the same size")
        for cel in line:
            if type(cel) != int and type(cel) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_line.append(round(cel / div, 2))
        result.append(new_line.copy())
        new_line.clear()
    return result
