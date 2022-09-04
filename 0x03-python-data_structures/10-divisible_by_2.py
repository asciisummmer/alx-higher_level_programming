#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    number_divisible_2 = []
    for elt in my_list:
        if elt % 2 == 0:
            number_divisible_2.append(True)
        else:
            number_divisible_2.append(False)
    return number_divisible_2
