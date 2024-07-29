#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n_list = []
    for indice, value in enumerate(my_list):
        if my_list[indice] == search:
            n_list.append(replace)
        else:
            n_list.append(my_list[indice])
    return n_list
