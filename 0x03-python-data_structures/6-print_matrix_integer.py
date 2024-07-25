#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        len_of_row = len(row)
        for i in range(len_of_row):
            print(
                "{:d}{}".format(
                    row[i], " "
                    if i + 1 != len_of_row else ""
                    ), end=""
                )
        print()
