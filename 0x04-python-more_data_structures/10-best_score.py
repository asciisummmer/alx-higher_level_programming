#!/usr/bin/python3

def best_score(a_dictionary):
    max_occu =[a_dictionary.keys()[0]]
    max_occu.append(a_dictionary[max_occu[0]])
    for key, value in a_dictionary.items():
        if value > max_occu[1]:
            max_occu[0] = key
            max_occu[1] = value
    return max_occu[0]
