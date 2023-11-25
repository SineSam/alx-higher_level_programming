#!/usr/bin/python3
# 2-is_same_class.py

""" Module tthat contains the is_same_class method"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    otherwise False

    Args:
    obj: The object to be tested
    a_class: The class
    """
    return (type(obj) == a_class)
