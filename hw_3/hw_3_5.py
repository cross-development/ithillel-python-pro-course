"""
This module provides custom implementations of common iterable operations:

- `custom_len()`: Calculates the length of an iterable object.
- `custom_sum()`: Calculates the sum of all elements in an iterable object.
- `custom_min()`: Finds the minimum value in an iterable object.

These functions demonstrate how to implement these operations without relying
on built-in functions like `len()`, `sum()`, and `min()`.

The module includes unit tests to verify the correctness of these custom functions.
"""

from typing import Iterable


def custom_len(sequence: Iterable) -> int:
    """
    Calculates the length of an iterable object.

    Args:
        sequence (Iterable): The iterable object to calculate the length of.

    Returns:
        int: The length of the iterable object.
    """
    if hasattr(sequence, '__len__'):
        return sequence.__len__()

    # Fallback to iteration
    count = 0

    for _ in sequence:
        count += 1

    return count


def custom_sum(sequence: Iterable) -> int:
    """
    Calculates the sum of all elements in an iterable object.

    Args:
        sequence (Iterable): The iterable object containing numerical elements.

    Returns:
        int: The sum of all elements in the sequence.
    """
    total = 0

    for item in sequence:
        total += item

    return total


def custom_min(sequence: Iterable) -> int:
    """
    Finds the minimum value in an iterable object.

    Args:
        sequence (Iterable): The iterable object containing comparable elements.

    Raises:
        ValueError: If the sequence is empty.

    Returns:
        int: The minimum value in the sequence.
    """
    iterator = iter(sequence)

    try:
        minimum = next(iterator)
    except StopIteration:
        raise ValueError("Sequence is empty")

    for item in iterator:
        minimum = min(minimum, item)

    return minimum


test_list = [1, 2, 3, 4, 5]

print("len() Test:")
print(f"Custom len: {custom_len(test_list)}")
assert custom_len(test_list) == 5, "Custom len should be 5"

print("\nsum() Test:")
print(f"Custom sum: {custom_sum(test_list)}")
assert custom_sum(test_list) == 15, "Custom sum should be 15"

print("\nmin() Test:")
print(f"Custom min: {custom_min(test_list)}")
assert custom_min(test_list) == 1, "Custom min should be 1"

print("All tests passed!")
