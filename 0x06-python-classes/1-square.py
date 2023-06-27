#!/usr/bin/python3

""" Create a class named Square that provides a definition for a square,-
   -utilizing the code from the file "0-square.py"."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (integer): The size of the square.
        """
        self.__size = size
