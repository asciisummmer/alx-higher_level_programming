#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    num = sum([val[0] * val[1] for val in my_list])
    denom = sum([val[1] for val in my_list])
    return num / denom
