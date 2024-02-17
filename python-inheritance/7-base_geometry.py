#!/usr/bin/python3

"""Module for base_geometry class."""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """Method to compute the area of a geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate the value."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
