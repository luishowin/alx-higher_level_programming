#!/usr/bin/python3
"""Defines a class"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to compare with.

    Returns:
    bool: True if the object is an instance of a class that inherited from the specified class, otherwise False.
    """
    if type(obj) is a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False
