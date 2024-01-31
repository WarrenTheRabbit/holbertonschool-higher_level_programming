#!/usr/bin/python3

"""Task1 module for Holberton School Australia's OOP section.

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
    def __init__(self, size):
        """Initializes a Square object.

        Args:
            size (unspecified): The size of the square.

        """
        self.__size = size
