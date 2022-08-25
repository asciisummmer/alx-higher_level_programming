#!/usr/bin/python3
for num_one in range(9):
    for num_two in range(num_one + 1,10):
        if num_one != 8 or num_two != 9:
            print(f"{num_one:d}{num_two:d}, ", end="")
        else:
            print(f"{num_one:d}{num_two:d}")
