#!/usr/bin/python3

def perform_magic_calculation(a, b):
    """
    Perform a magic calculation using given values a and b.

    Args:
        a (int): The first value.
        b (int): The second value.

    Returns:
        The result of the magic calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Invalid value for a')
            else:
                result += a ** b / i
        except ValueError:
            result = b + a
            break
    return (result)
