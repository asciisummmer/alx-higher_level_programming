#!/usr/bin/python3
def print_last_digit(number):
    result =  number % 10 if number >= 0 else -number % 10
    print(f"{result:d}", end="")
    return result
