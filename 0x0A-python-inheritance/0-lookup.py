#!/usr/bin/python3
# 0-lookup.py

"""Module containing method to lookup available attributes and methods"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods of an object

    Args:
    obj: Object to be analysed
    """
    return ([obj.__dict__])
