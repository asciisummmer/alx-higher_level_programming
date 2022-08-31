#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        l = [str(x) for x in line]
        print(" ".join(l))
