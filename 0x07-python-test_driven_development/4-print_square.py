#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of '#' characters with the specified size.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float and is less than 0.
    - ValueError: If size is less than 0.

    Example:
    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(0)
    (prints nothing, as it's a square with size 0)
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

# Example usage:
print_square(3)
print_square(0)