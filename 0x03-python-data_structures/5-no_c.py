#!/usr/bin/pyhton3

def no_c(my_string):
    for car in my_string:
        if car in "cC":
            my_string.remove(car)
