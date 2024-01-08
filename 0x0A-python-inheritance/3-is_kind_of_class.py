#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of the specified class or its subclasses.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to compare with.

    Returns:
    bool: True if the object is an instance of the specified class or its subclasses, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False