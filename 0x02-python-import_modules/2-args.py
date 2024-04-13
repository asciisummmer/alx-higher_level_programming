#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_arg = len(argv) - 1
    print("{} argument{plural}{punctuation}" .format(
        len_arg, plural="s" if len_arg == 0 or len_arg > 1 else "",
        punctuation="." if len_arg == 0 else ":"))
    for i in range(len_arg):
        print("{}: {}".format(i + 1, argv[i + 1]))
