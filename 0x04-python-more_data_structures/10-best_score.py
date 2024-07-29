#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == []:
        return None
    max_occu = [list(a_dictionary.keys())[0]]
    max_occu.append(a_dictionary[max_occu[0]])
    for key, value in a_dictionary.items():
        if value > max_occu[1]:
            max_occu[0] = key
            max_occu[1] = value
    return max_occu[0]
