#!/usr/bin/python3
"""Def max int."""


def max_integer(input_list):
    """
    Returns the maximum integer from a list.

    Args:
    - input_list (list): A list of integers.

    Returns:
    - int or None: The maximum integer in the list. Returns None for an empty list.

    Raises:
    - TypeError: If the input is not a list or if the elements in the list are not integers.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")

    # Check if the list is empty
    if not input_list:
        return None

    # Check if all elements are integers
    if not all(isinstance(element, int) for element in input_list):
        raise TypeError("All elements in the list must be integers")

    # Return the maximum integer
    return max(input_list)