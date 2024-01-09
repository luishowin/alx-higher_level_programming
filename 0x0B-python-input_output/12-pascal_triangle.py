#!/usr/bin/python3
"""Def func pascals t."""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    :param n: The number of rows for Pascal's triangle.
    :return: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Example usage:
if __name__ == "__main__":
    # Generate Pascal's triangle up to the 5th row
    result = pascal_triangle(5)

    # Display the generated Pascal's triangle
    for row in result:
        print(row)
