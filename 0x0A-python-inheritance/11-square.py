#!/usr/bin/python3
"""Def."""


class Rectangle:
    """Class."""
    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer and greater than 0.

        Args:
        - name (str): The name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(Rectangle):
    """De."""
    def __init__(self, size):
        """
        Initializes the Square instance with a size.

        Args:
        - size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
        - str: The square description.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
