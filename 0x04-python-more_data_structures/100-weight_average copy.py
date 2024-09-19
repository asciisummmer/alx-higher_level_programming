#!/usr/bin/python3
from functools import reduce


def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    num = reduce(lambda x, y: (x[0] * x[1] + y[0] * y[1], 1), my_list)
    denom = reduce(lambda x, y: (0, x[1] + y[1]), my_list)
    return reduce(lambda x, y: x[0] / y[1], [num, denom])
