#!/usr/bin/python3
"""Class MyInt."""


class MyInt(int):
    """S."""
    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
        - other: The object to compare.

        Returns:
        - bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
        - other: The object to compare.

        Returns:
        - bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
