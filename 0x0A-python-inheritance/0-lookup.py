#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attributes and methods.
    """
    return dir(obj)

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
