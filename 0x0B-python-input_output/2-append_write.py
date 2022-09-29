#!/usr/bin/python3
"""
Contains append_write function
"""


def append_write(filename="", text=""):
    """returns number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.append(text)
