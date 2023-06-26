#!/usr/bin/python3

import sys


def print_integer_safely(value):
    """Prints an integer using str().

    If a ValueError occurs, an error message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if a TypeError or ValueError occurs.
    """
    try:
        print(str(value))
        return (True)
    except (TypeError, ValueError) as e:
        print("Error: {}".format(e), file=sys.stderr)
        return (False)
