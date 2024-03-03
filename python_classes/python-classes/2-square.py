#!/usr/bin/python3

"""define a class o a square"""


class Square:
    """class defining a square"""

    def __init__(self, size=0):

        """Initializes a new Square object.
        Args:
        size (int): Optional size of the square (default is 0).
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """

        self.___size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.___size = size
            """size attribute"""
