#!/usr/bin/python3
# File: 2-is_same_class.py

"""
This module contains the check function that identify if is_same_class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Returns:
        If obj is exactly an instance of a_class - True.
    """
    if type(obj) == a_class:
        return True
    return False
    