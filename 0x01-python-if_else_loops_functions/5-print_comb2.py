#!/usr/bin/python3
for i in range(99):
    print("{}{}".format('0' if i <= 9 else '', i), end=", ")
print('99'.format())
