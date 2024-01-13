#!/usr/bin/python3
"""Def matrix division func."""


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
    """
    # Check if matrix is a list of lists
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix(a list of lists) of"
                        "integers/floats")
    

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2), row) for row in matrix)])
        
