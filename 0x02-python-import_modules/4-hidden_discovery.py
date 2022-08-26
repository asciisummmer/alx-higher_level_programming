#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    symboles = dir(hidden_4)
    for symbole in symboles:
        if symbole[:2] != "__":
            print(symbole)
