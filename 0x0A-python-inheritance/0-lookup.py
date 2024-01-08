#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attributes and methods.
    """
    return dir(obj)

# Example usage:
class ExampleClass:
    def __init__(self):
        self.attribute1 = 42

    def method1(self):
        return "Hello, World!"

obj_instance = ExampleClass()
result = lookup(obj_instance)
print(result)
