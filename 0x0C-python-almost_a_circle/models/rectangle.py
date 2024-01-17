#!/usr/bin/python3
'''Implementation.'''
from models.base import Base


class Rectangle(Base):
    '''A rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        '''Width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        '''Height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        '''X of the rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        '''Y of rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value