#!/usr/bin/python3
""" defines a function that prints names """

def say_my_name(first_name, last_name=""):
    """prints name.

    Args:
        first_name.str of firstname
        last_name. str of the lastname
    Raises:
          Typeerrorif not str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
