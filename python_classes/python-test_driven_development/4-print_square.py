#!/usr/bin/python3
"""a function that prints a square """

def print_square(size):
    """ prints a square.

    Args:
        size- size of the sides of a square
    Raises:
          Typeerror
          valueerror
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
