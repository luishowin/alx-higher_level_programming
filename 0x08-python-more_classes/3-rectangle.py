#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialise a new rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.width = width # Private attribute with leading underscore
        self.height = height # Private attribute with leading underscore

    @property
    def width (self):
        """Get or set the width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >=0")
        self.__width = value

    @property
    def height(self, value):
        """Get/set the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """Return the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))
