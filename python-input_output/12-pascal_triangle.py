#!/usr/bin/python3

"""Module contains a basic pascal triangle function."""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    the Pascal's triangle of n"""
    if n <= 0:
        return []
    return [[1]] + [list(map(lambda x, y: x + y,
                    lst + [0], [0] + lst))
                    for lst in pascal_triangle(n - 1)]
