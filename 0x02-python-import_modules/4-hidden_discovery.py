#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for elt in dir(hidden_4):
        if not elt.startswith("__"):
            print(elt)
