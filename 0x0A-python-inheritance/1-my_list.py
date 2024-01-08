#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """Custom list class inheriting from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
my_list.print_sorted()
