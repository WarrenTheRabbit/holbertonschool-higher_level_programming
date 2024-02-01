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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
