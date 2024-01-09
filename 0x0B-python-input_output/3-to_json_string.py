#!/usr/bin/python3
"""Import json."""


import json

def to_json_string(my_obj):
    """
    Return the JSON representation of the given object (string).

    :param my_obj: The object to be converted to JSON.
    :return: A JSON-formatted string representing the object.
    """
    return json.dumps(my_obj)

# Example usage:
my_object = {"name": "John", "age": 30, "city": "New York"}
json_string = to_json_string(my_object)

print("JSON representation:")
print(json_string)
