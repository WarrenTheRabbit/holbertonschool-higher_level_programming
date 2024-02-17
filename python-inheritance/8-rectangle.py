#!/usr/bin/python3
"""Module for base_geometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry."""

    def __init__(self, width, height):
        """Method to initialize the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method to compute the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Method to compute the string representation of a rectangle."""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
