#!/usr/bin/python3
# 4-print_square.py
"""This module contains a method that prints a square"""


def print_square(size):
    """ Method that prints a square with the '#' character

    Args:
    size (integer): Length of a square

    raises:
    TypeError: size is not an integer
    ValueError: size is less than zero
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
