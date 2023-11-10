#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    A class representing the square
    """
    def __init__(self, size=0):
        """
        This method initiates the Square

        Args:
        size (int): defines the size of the square
        Validated with try/except

        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This method returns the area of the square
        """
        return (self.__size ** 2)
