#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

# Example usage:
class MyClass1(object):
    """Docstring: description of the class"""
    pass

class MyClass2(object):
    """Docstring: description of the class"""
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
