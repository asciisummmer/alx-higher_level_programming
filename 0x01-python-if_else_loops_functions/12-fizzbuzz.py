#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        result = i
        if i % 5 == 0:
            result = "Buzz"
        if i % 3 == 0:
            result = "Fizz"
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        print(f"{result} ", end="")
