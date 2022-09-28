#!/usr/bin/python3
"""
contains read_file function
"""


def read_file(filename=""):
    """Use with to open and read a utf8 file and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
