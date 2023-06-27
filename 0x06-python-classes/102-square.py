#!/usr/bin/python3

"""Define a class Square that represents a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self._size = size

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate the current square's area."""
        return self._size ** 2

    def __eq__(self, other):
        """Define the == comparison for a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison for a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison for a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison for a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison for a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison for a Square."""
        return self.area() >= other.area()
