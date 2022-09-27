#!/usr/bin/python3
"""
Create a class that inherits from my list.
"""


class MyList(list):
    """Class MyList inherits from the list"""
    def __init__(self):
        """Initializing the object"""
        super().__init__()

    def print_sorted(self):
        """Printing the sorted list"""
        print(sorted(self))
