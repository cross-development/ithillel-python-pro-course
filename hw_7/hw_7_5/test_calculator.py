"""
This module contains unit tests for the `divide` function.

- `test_divide_valid`: Tests the function with valid input values.
- `test_divide_by_zero`: Tests the function's handling of division by zero.
- `test_divide_parametrized`: Tests the function with a parameterized set of inputs.
"""

import pytest

from hw_7.hw_7_5.calculator import divide


def test_divide_valid() -> None:
    """
    Tests the `divide` function with valid input values.
    """

    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(7, 1) == 7.0


def test_divide_by_zero() -> None:
    """
    Tests the `divide` function's handling of division by zero.
    """

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (-6, 2, -3.0),
    (0, 5, 0.0),
    (100, 10, 10.0)
])
def test_divide_parametrized(a: int, b: int, expected: float) -> None:
    """
    Tests the `divide` function with a parameterized set of inputs.

    Args:
        a (int): The dividend.
        b (int): The divisor.
        expected (float): The expected result of the division.
    """

    assert divide(a, b) == expected


if __name__ == "__main__":
    pytest.main()
