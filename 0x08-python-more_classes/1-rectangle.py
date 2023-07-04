#!/usr/bin/python3
"""Defines a CustomRectangle class."""

class CustomRectangle:
    """Represent a rectangle with width and height."""
    def __init__(self, width=0, height=0):
        """Initialize a new CustomRectangle.

        Args:
            width (int): The width of the CustomRectangle.
            height (int): The height of the CustomRectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get or set the width of the CustomRectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the CustomRectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
