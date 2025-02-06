"""
This module provides two mathematical functions:

- `is_even(n)`: Checks if the given integer `n` is even.
- `factorial(n)`: Calculates the factorial of the given integer `n`.

Both functions include docstrings with doctests to demonstrate their usage and expected behavior.
"""


def is_even(n: int) -> bool:
    """
    Checks if the given integer is even.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is even, False otherwise.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-5)
    False
    """

    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculates the factorial of the given integer.

    Args:
        n (int): The integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: Factorial is not defined for negative numbers
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n in (0, 1):
        return 1

    return n * factorial(n - 1)
