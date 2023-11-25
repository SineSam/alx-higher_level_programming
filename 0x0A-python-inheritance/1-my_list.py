#!/usr/bin/python3
# 1-my_list.py

""" Module contains MyList class"""


class MyList(list):
    """
    a class MyList that inherits from list

    Args:
    list: list containing elements of int type
    """
    def print_sorted(self):
        """method for printing sorted list"""
        print(sorted(self))
