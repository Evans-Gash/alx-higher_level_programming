#!/usr/bin/python3


""" Create a class named Square that provides a definition for a square,-
    -utilizing the code from the file "0-square.py"."""

class Square:
    """Reps a square."""

    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
            size (integer): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
