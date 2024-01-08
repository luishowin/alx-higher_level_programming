#!/usr/bin/python3
"""Def add attribute."""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Raises a TypeError if the object can't have new attributes.

    Args:
    - obj: The object to which the attribute is added.
    - name (str): The name of the attribute.
    - value: The value of the attribute.

    Raises:
    - TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and not type(obj).__slots__):
        # If the object has a __dict__ attribute or its type has empty __slots__
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
