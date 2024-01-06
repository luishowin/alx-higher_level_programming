#1?usr/bin/python3
"""Defines a class named Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises a new Rectangle.

        Arguments:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """

        self._width = 0  # Private attribute with leading underscore
        self._height = 0  # Private attribute with leading underscore

        # Use the property setters to validate and set the initial values
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
         """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height) if self._width and self._height else 0
