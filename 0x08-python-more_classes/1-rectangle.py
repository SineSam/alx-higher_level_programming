#!/usr/bin/python3
"""
Module 1-rectangle
This is a module that will define the rectangle class
"""


class Rectangle:
    """
    This class defines the methods for rectangle
    """

    def __init__(self, width=0, height=0):
        """Constructor method, initialises rectangle instance

        Args:
        width: width of the rectangle
        heigh: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a triangle instance

        Args:
        value: value of width, which must be a positive integer
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of a rectangle at a instance

        Args:
        value: the value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
