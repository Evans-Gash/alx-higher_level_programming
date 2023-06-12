#!/usr/bin/python3


def print_reversed_list_integer(gash_list=[]):
    """Print all integers of a list in reverse order."""
    if isinstance(gash_list, list):
        reversed_list = gash_list[::-1]
        for i in reversed_list:
            print("{:d}".format(i))


if __name__ == "__main__":
    gash_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(gash_list)
