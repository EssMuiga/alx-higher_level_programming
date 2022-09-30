#!/usr/bin/python3
"""
It has the load_from_json_file function
"""


import json


def load_from_json_file(filename):
    """creates an object from json"""
    with open(filemname, 'r', encoding='utf-8') as f:
        return json.load(f)
