#!/usr/bin/python3
"""Define a function write_file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters written.

    :param filename: The name of the file to be written (default is an empty string).
    :param text: The string to be written to the file (default is an empty string).
    :return: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Example usage:
filename = "example.txt"
text_to_write = "Hello, this is a sample text."
characters_written = write_file(filename, text_to_write)

print(f"Number of characters written to {filename}: {characters_written}")
