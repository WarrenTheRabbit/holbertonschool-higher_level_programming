#!/usr/bin/python3
"""Task 0 module
"""


def add_integer(a, b):
    """Adds two integers together"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
