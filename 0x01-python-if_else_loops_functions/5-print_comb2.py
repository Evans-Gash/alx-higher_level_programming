#!/usr/bin/python3
def print_numbers():
    for number in range(0, 100):
        if number == 99:
            print("{}".format(number))
        else:
            print("{:02}".format(number), end=", ")


if __name__ == "__main__":
    print_numbers()
