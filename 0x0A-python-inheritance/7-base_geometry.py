#!/usr/bin/pythhon3
"""Defines a class BaseGeometry"""

class BaseGeometry:
    """Defines a class BaseGeometry."""
    def area(self):
        """Public instance method that raises an Exception.

        Raises:
        - Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates an integer value.

        Args:
        - name (str): The name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        