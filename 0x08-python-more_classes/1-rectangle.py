#!/usr/bin/python3
"""
Definning a Rectangle class.
"""


class Rectangle:
    """
    Representation of a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializing New Rectangle.
        Arguments:
            width:  The width of the new rectangle as an integer.
            height: The height of the new rectangle as an integer.
        Raises:
            TypeError   (Width): Must be an integer.
            ValueError  (Width): must be >= 0.
            TypeError  (Height): Must be an integer.
            ValueError (Height): Must be >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Setting the width of the new rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Setting the height of the new rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mst be >= 0")
        self.__height = value
