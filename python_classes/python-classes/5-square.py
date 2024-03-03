#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """returns area of a square"""

        self.a = self.__size ** 2
        return (self.a)

    @property
    def size(self):
        """size of the siides of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the property for size

        Args:
            value: size of 1 side

        Raises:
            TypeError: int
            ValueError: > 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print square to stdout"""

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
