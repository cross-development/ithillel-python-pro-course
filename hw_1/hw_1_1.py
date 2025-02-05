"""
This module provides a function to calculate the area of a circle.

The `calculate_circle_area` function takes the radius of a circle as input
and returns its area using the formula:

    Area = π * radius^2

The module also includes a simple example usage and unit tests
to demonstrate the functionality.
"""

import math


def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be a non-negative value.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return math.pi * radius ** 2


user_input = float(input("Enter the radius of a circle: "))

print(calculate_circle_area(user_input))

assert calculate_circle_area(2) == 12.566370614359172, "Calculated circle area is 12.56637061435917"
assert calculate_circle_area(0) == 0.0, "Calculated circle area is 0.0"
