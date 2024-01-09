#!/usr/bin/python3
"""Def class."""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation suitable for JSON serialization.

    :param obj: An instance of a Class with serializable attributes.
    :return: A dictionary describing the object for JSON serialization.
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Object must be an instance of a Class")

    json_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_data[key] = value

    return json_data

# Example usage:
class SampleClass:
    def __init__(self, name, age, data_list, is_active):
        self.name = name
        self.age = age
        self.data_list = data_list
        self.is_active = is_active

# Create an instance of SampleClass
sample_instance = SampleClass(name="John", age=30, data_list=[1, 2, 3], is_active=True)

# Convert the instance to a dictionary for JSON serialization
json_description = class_to_json(sample_instance)

print("Dictionary for JSON serialization:")
print(json_description)
