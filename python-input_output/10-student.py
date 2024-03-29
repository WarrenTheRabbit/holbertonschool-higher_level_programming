#!/usr/bin/python3
"""Module contains a basic student class."""


class Student:
    """Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the JSON representation of an object (string)"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
