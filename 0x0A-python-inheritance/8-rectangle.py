#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """The class."""
    def area(self):
        """Instance."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines an instance."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Inst."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
