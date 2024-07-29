#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_unique_list = []
    for elt in my_list:
        if elt not in new_unique_list:
            new_unique_list.append(elt)
    return sum(new_unique_list)
