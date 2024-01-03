def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a specified number.

    Parameters:
    - matrix (list of lists): The input matrix of integers or floats.
    - div (int or float): The number by which each element of the matrix will be divided.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
               if each row of the matrix does not have the same size, or
               if div is not a number.
    ZeroDivisionError: If div is equal to 0.

    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> divisor = 2
    >>> matrix_divided(matrix, divisor)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

# Example usage:
matrix_input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

divisor = 2

result = matrix_divided(matrix_input, divisor)
print(result)
