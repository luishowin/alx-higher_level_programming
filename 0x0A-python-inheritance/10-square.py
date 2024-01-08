#!/usr/bin/python3
"""Def class BaseGeometry."""


class BaseGeometry:
    """Class."""
    def area(self):
        """Placeholder method for area calculation, to be implemented in subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the given value is an integer and greater than 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class rectangle."""
    def __init__(self, width, height):
        """Initializes the Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle in the specified format."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class square."""
    def __init__(self, size):
        """Initializes the Square instance with a size, calling the base class constructor."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """String representation of the square in the specified format."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
