#!/usr/bin/python3
""" defines a funtion that adds two integers"""

def add_integer(a, b=98):
    """ add two ints 
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

