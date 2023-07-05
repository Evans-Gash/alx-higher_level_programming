def add_integer(a, b=98):
    """A function that adds two integers.
    Return the integer addition of a and b.
    Float arguments are cast to integers before addition is performed.
    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
