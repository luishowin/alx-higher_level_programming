#!/usr/bin/python3
"""Defines a class BaseGeometry"""

class BaseGeometry:
    """Class."""
    def area(self):
        """Raise."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Def func int validator."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Init class Rect."""
    def __init__(self, width, height):
        """Define init."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Def instance area."""
        return self.__width * self.__height

    def __str__(self):
        """Def."""
        return f"[Rectangle] {self.__width}/{self.__height}"
