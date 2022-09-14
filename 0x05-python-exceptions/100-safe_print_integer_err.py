#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """prints an integer
            args:
                value
            output:
                integers
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
