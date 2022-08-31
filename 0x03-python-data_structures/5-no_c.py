#!/usr/bin/python3

def no_c(my_string):
    for car in my_string:
        if car in "cC":
            my_string = my_string.replace(car, '')
    return my_string
