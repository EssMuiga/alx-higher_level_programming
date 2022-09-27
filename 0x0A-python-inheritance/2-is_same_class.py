#!/usr/bin/python3
"""
Function for is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact a_class, otherwise false"""
    return True if type(obj) is a_class else False
