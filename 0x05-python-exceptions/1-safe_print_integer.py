#!/usr/bin/python3

def print_integer_safely(num):
    """Print an integer safely using string conversion.

    Args:
        num (int): The integer to print.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if a TypeError or ValueError occurs.
    """
    try:
        print(str(num))
        return (True)
    except (TypeError, ValueError):
        return (False)
