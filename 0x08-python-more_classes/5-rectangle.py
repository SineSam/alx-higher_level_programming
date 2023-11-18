#!/usr/bin/python3
"""
Module 3-rectangle
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
        self.width = width
        self.height = height

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

    def area(self):
        """method returns the area of the rectangle

        Args:
        height: int value height of the rectangle
        width: int value width of the rectangle

        Returns the product of height and width
        """
        return self.__height * self.__width

    def perimeter(self):
        """ method to calculate the perimeter of the rectangle

        Args:
        height: int value height of the rectangle
        width: int value, width of the rectangle

        Return: the sum of the sides of the rectangle
        """
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height) * 2 + (self.__width) * 2

    def __str__(self):
        """ method to print human readable string representing rectangle"""
        string = ""
        if self.__height != 0 and self.__width != 0:
            string += "\n".join(
                    "#" * self.__width for j in range(0, self.__height))
        return string

    def __repr__(self):
        """return spring reperesentation of a rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message when instance is deleted"""
        print("Bye rectangle...")
