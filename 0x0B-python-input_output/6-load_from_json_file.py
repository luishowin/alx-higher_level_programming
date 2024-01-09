#!/usr/bin/python3
"""Import."""


import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file.
    :return: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Example usage:
loaded_object = load_from_json_file("input.json")

print("Loaded object:")
print(loaded_object)
