#!/usr/bin/python3
class LockedClass:
    """Locked class that lets the user create instance attribute 'first_name'"""
    __slots__ = ['first_name']
