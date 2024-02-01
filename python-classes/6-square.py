#!/usr/bin/python3

"""Task2 module for Holberton School Australia's OOP section.

The module contains one class, Square.

"""


class Square:
    """Represents a square.

        Attributes:
            __size: The size of the square.
            __position: The position of the square.

        Methods:
            None

        Usage:
            from square import Square

            # Create a square object
            square = Square()
    """
    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """Initializes a Square object.

        Args:
            size (int): The size of the square.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0
                or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("\n" * self.position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.size)
