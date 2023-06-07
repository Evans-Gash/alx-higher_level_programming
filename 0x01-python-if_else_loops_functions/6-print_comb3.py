#!/usr/bin/python3
def print_combinations():
    for digit1 in range(0, 10):
        for digit2 in range(digit1 + 1, 10):
            print("{}{}".format(digit1, digit2), end=", ")
    print("89")


if __name__ == "__main__":
    print_combinations()
