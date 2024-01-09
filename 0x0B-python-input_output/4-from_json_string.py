#!/usr/bin/python3
"""Import."""


import json

def from_json_string(my_str):
    """
    Return the Python object represented by the given JSON string.

    :param my_str: The JSON-formatted string to be converted to a Python object.
    :return: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

# Example usage:
json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_object = from_json_string(json_string)

print("Python object:")
print(python_object)
