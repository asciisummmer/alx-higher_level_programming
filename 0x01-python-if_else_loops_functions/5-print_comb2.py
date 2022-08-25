#!/usr/bin/python3
for num in range(100):
    if num != 99:
        if num > 9:
            output = "{}, "
        else:
            output = "0{}, "
        print(output.format(num), end="")
    else:
        print(num)
