#!/usr/bin/python3
import random
number = random.randint(-10, 10)

def check_number(number):
    if number > 0:
        return "{} is positive".format(number)
    elif number == 0:
        return "{} is zero".format(number)
    else:
        return "{} is negative".format(number)

if __name__ == "__main__":
    result = check_number(number)
    print(result)
