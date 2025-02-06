"""
This module contains unit tests for the matrix_utils module.

- `test_doctests`: Runs doctests for the functions defined in the module.
- `test_transpose_matrix`: Tests the `transpose_matrix` function with different matrix inputs.
- `test_matrix_multiply`: Tests the `matrix_multiply` function with various matrix combinations.
- `test_matrix_multiply_invalid`: Tests the `matrix_multiply` function with incompatible matrices.
"""

from typing import List
import doctest
import pytest

from hw_7.hw_7_8.matrix_utils import matrix_multiply, transpose_matrix


def test_doctests() -> None:
    """
    Runs doctests for the functions defined in the module.
    """

    results = doctest.testmod()

    assert results.failed == 0, f"Doctests failed: {results.failed}"


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[7]], [[7]]),
    ([], []),
])
def test_transpose_matrix(matrix: List[List[int]], expected: List[List[int]]) -> None:
    """
    Tests the `transpose_matrix` function with different matrix inputs.

    Args:
        matrix (List[List[int]]): The input matrix.
        expected (List[List[int]]): The expected transposed matrix.
    """

    assert transpose_matrix(matrix) == expected


@pytest.mark.parametrize("matrix1, matrix2, expected", [
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    ([[2, 0], [0, 2]], [[1, 2], [3, 4]], [[2, 4], [6, 8]]),
    ([[1]], [[2]], [[2]]),
])
def test_matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]], expected: List[List[int]]) -> None:
    """
    Tests the `matrix_multiply` function with various matrix combinations.

    Args:
        matrix1 (List[List[int]]): The first matrix.
        matrix2 (List[List[int]]): The second matrix.
        expected (List[List[int]]): The expected result of matrix multiplication.
    """

    assert matrix_multiply(matrix1, matrix2) == expected


def test_matrix_multiply_invalid() -> None:
    """
    Tests the `matrix_multiply` function with incompatible matrices.
    """

    with pytest.raises(ValueError, match="Matrix 1's columns must equal Matrix 2's rows"):
        matrix_multiply([[1, 2]], [[3, 4]])


if __name__ == "__main__":
    pytest.main()
