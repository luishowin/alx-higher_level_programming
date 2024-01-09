#!/usr/bin/python3
"""Defines a function append_file."""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return the number of characters added.

    :param filename: The name of the file to be appended (default is an empty string).
    :param text: The string to be appended to the file (default is an empty string).
    :return: The number of characters added to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage:
filename = "example.txt"
text_to_append = "This is additional content."
characters_added = append_write(filename, text_to_append)

print(f"Number of characters added to {filename}: {characters_added}")
