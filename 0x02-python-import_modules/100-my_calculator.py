#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    len_arg = len(argv) - 1
    if len_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    match argv[2]:
        case "+":
            print("{:d} + {:d} = {}".format(a, b, add(a, b)))
        case "-":
            print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{:d} / {:d} = {}".format(a, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
