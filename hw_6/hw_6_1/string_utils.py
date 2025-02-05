"""
This module provides two string utility functions:

- `to_upper(string)`: Converts a string to uppercase.
- `trim_whitespace(string)`: Removes leading and trailing whitespace from a string.
"""


def to_upper(string: str) -> str:
    """
    Converts a string to uppercase.

    Args:
        string (str): The input string.

    Returns:
        str: The input string converted to uppercase.
    """

    return string.upper()


def trim_whitespace(string: str) -> str:
    """
    Removes leading and trailing whitespace from a string.

    Args:
        string (str): The input string.

    Returns:
        str: The input string with leading and trailing whitespace removed.
    """

    return string.strip()
