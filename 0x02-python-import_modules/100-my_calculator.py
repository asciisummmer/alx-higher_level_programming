#!/usr/bin/python3

import calculator_1
from sys import argv, exit
if __name__ == "__main__":
    len_arg = len(argv) - 1
    if len_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    result = 0
    a = int(argv[1])
    b = int(argv[3])
    match argv[2]:
        case "+":
            result = a + b
            print("{} + {} = {}".format(a, b, result))
        case "-":
            result = a - b
            print("{} - {} = {}".format(a, b, result))
        case "*":
            result = a * b
            print("{} * {} = {}".format(a, b, result))
        case "/":
            result = a / b
            print("{} / {} = {}".format(a, b, result))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
