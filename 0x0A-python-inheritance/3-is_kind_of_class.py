#!/usr/python3
# 3-is_kind_of_class.py

"""This modules uses the method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    otherwise False

    Args:
    onject: The object
    a_class: the class
    """
    return (isinstance(obj, a_class))
