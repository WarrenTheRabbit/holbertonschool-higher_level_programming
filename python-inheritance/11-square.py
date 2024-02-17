#!/usr/bin/python3
"""Module for base_geometry class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class BaseGeometry."""

    def __init__(self, size):
        """Method to initialize the rectangle."""
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        """Method to compute the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Method to compute the string representation of a rectangle."""
        return "[Square] " + str(self.__width) + "/" + str(self.__height)
