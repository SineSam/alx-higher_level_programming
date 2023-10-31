#!/usr/bin/python3
#0-add_integer.py
"""
Module add_integer
Adds two integers

"""
def add_integer(a, b=98):
    """Return the addition of integers a and b.
    Args:
    a (int or float): First number.
    b (int or float): Second number.

    Returns:
    int: sum of the two numbers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
