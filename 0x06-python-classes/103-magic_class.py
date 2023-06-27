#!/usr/bin/python3

"""Define a MagicClass that represents a circle."""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self._radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        """Calculate the area of the MagicClass."""
        return self._radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass."""
        return (2 * math.pi * self._radius)
