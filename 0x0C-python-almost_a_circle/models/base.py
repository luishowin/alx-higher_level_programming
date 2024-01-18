#!/usr/bin/python3
"""Defines a class Base."""


class Base:
    """Private class attribute."""
    __nb_objects = 0

    """Class constructor."""
    def __init__(self, id=None):
        """
        If id is not None, assign it to the public instance attribute id
        Otherwise, increment __nb_objects and assign the new value to id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

