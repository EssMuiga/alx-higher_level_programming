#!/usr/bin/python3
"""
has the class_to_json function
"""


def class_to_json(obj):
    """returns simple data structure for json serialization of an object"""
    return obj.__dict__
