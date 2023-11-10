#!/usr/bin/python3
"""Define class Square"""


class Square:
    """This defines the Square class

    This class has no public attributes

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
