#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """Custom list class inheriting from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
