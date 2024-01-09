#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    :param filename: The name of the file to be read (default is an empty string).
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
read_file("example.txt")
