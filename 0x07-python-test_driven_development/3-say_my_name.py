#!/usr/bin/python3
#3-say_my_name.py
"""Module containing function that prints name"""


def say_my_name(first_name, last_name=""):
    """A function to print the first and last name

    Args:
    first_name (str): The first name to print
    last_name (str): The second name to print

    raises:
    TypeError if names are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
