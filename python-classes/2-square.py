#!/usr/bin/python3

"""Task2 module for Holberton School Australia's OOP section.

The module contains one class, Square.

"""


class Square:
    """Represents a square.

        Attributes:
            __size: The size of the square.

        Methods:
            None

        Usage:
            from square import Square

            # Create a square object
            square = Square()
    """
    def __init__(self, size: int = 0):
        """Initializes a Square object.

        Args:
            size (int): The size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
