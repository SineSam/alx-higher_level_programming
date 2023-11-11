#!/usr/bin/python3
"""This is a module that will define the rectangle class"""


class Rectangle:
    """
    This class defines the methods for rectangle
    """
    def __init__(self, width=0, height=0):
        """Constructor method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The getter/setter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter/setter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
