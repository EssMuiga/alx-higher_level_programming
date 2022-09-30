#!/usr/bin/python3
"""
Write object to a file using JSON
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to atext file using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
