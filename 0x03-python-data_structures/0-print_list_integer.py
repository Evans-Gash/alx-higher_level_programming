#!/usr/bin/python3


def print_list_integer(evans_list=[]):
    """Print all integers of a list."""
    for i in range(len(evans_list)):
        print("{:d}".format(evans_list[i]))


if __name__ == "__main__":
    evans_list = [1, 2, 3, 4, 5]
    print_list_integer(evans_list)
