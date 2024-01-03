#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the given first and last names.

    Args:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Alice")
    My name is Alice
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted string
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")

# Example usage:
say_my_name("John", "Doe")
say_my_name("Alice")