#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(0, len(line)):
            if i + 1 == len(line):
                print(line[i], end="")
            else:
                print(line[i], end=" ")
        print()
