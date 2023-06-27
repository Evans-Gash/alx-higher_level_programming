#!/usr/bin/python3

"""
A class Square is defined that represents a square object.
It includes methods for initializing a square, getting/setting its size,
calculating its area, and printing the square with the '#' character.
"""

class Square:
    """ Represents a square. """

    def __init__(self, size=0):
        """ Initializes a new Square object.

        Args:
            size (int): The size of the square.

        """
        self.__size = size

    @property
    def size(self):
        """ Get/Set the current size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using the '#' character. """
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
