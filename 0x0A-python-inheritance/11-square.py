#!/usr/bin/python3
# File: 11-square.py

"""
This module defines a Rectangle subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Instantiation of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
