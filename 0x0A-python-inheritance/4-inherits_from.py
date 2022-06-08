#!/usr/bin/python3
# File: 4-inherits_from.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
This module defines an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Returns:
        If obj is an inherited instance of a_class - True.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
