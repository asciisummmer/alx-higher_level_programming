#!/usr/bin/python3

from calculator_1 import add, mul, div, sub

if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} + {:d} = {}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {}".format(a, b, div(a, b)))
