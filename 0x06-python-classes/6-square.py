#!/usr/bin/python3

"""
A class Square is defined that represents a square object.
It includes methods for initializing a square, getting/setting its size and position,
calculating its area, and printing the square with the '#' character.
"""

class Square:
    """ Represents a square. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new Square object.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get/Set the current position of the square. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
            ValueError: If any value in the tuple is less than 0.

        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square using the '#' character. """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
