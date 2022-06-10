#!/usr/bin/python3
# File: 7-base_geometry.py

"""
This module defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
