#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): matrix to be divided
        div (int or float): number to divide the matrix by

    Returns:
        list of lists: new matrix with all elements divided by div

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        TypeError: matrix must have each row with the same size
        ZeroDivisionError: division by zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # check that the matrix is square
    if not all(len(row) == len(matrix) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(cell, (int, float))
               for row in matrix
               for cell in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    return [[round(num / div, 2) for num in row] for row in matrix]
