#!/usr/bin/python3
"""lookup function"""

def lookup(obj):
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

