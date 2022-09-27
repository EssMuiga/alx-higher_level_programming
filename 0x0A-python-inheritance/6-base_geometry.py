#!/usr/bin/python3
"""
For class BaseGeometry
"""


class BaseGeometry:
    """It has a public area"""
    def area(self):
        """raises an exception when it is called"""
        raise Exception("area() is not implemented")
