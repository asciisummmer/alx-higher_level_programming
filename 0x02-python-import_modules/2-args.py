#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    size_arg = len(sys.argv[1:])
    if size_arg == 0:
        print("0 arguments.")
    elif size_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size_arg))
    for index in range(1, size_arg + 1):
        print("{}: {}".format(index, sys.argv[index]))
