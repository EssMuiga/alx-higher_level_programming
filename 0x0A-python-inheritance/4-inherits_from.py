#!/usr/bin/python3
"""
It contains the inherits_from functiuon
"""


def inherits_from(obj, a_class):
    """returns True if obj is a subclass of a_class, else False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
