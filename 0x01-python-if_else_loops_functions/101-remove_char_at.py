#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    final_str = ""
    for i, value in enumerate(str):
        if i != n:
            final_str += value
    return final_str
