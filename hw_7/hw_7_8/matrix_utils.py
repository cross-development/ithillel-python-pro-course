"""
This module provides functions for matrix operations:

- `matrix_multiply(matrix1, matrix2)`: Multiplies two matrices.
- `transpose_matrix(matrix)`: Transposes a given matrix.

Both functions include docstrings with doctests to demonstrate their usage and expected behavior.
"""

from typing import List


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Multiplies two matrices.

    Args:
        matrix1 (List[List[int]]): First matrix as a list of lists.
        matrix2 (List[List[int]]): Second matrix as a list of lists.

    Returns:
        List[List[int]]: Resulting matrix after multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied due to shape mismatch.

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[2, 0], [0, 2]], [[1, 2], [3, 4]])
    [[2, 4], [6, 8]]

    >>> matrix_multiply([[1]], [[2]])
    [[2]]

    >>> matrix_multiply([[1, 2]], [[3], [4]])
    [[11]]
    """

    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrix 1's columns must equal Matrix 2's rows")

    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transposes a matrix.

    Args:
        matrix (List[List[int]]): Matrix as a list of lists.

    Returns:
        List[List[int]]: Transposed matrix.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    >>> transpose_matrix([[7]])
    [[7]]

    >>> transpose_matrix([])
    []
    """

    return list(map(list, zip(*matrix)))
