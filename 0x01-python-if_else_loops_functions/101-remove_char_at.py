#!/usr/bin/python3

def remove_char_at(str, n):
    copy_str = ""
    if n < 0 or n >= len(str):
        return str
    for i in range(0, len(str)):
        if i == n:
            continue
        copy_str += str[i]
    return copy_str
