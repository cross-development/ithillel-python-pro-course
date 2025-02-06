"""
This module provides a single function:

- `divide(a, b)`: Performs division of two integers. 
    Raises a ZeroDivisionError if the divisor is zero.
"""


def divide(a: int, b: int) -> float:
    """
    Performs division of two integers.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b
