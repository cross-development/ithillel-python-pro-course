"""
This module demonstrates dynamic method calling in Python.

The `call_function` function allows you to dynamically call a method of an object
by providing the object, the method name as a string, and any arguments
the method requires.

The `Calculator` class provides simple arithmetic operations (addition and subtraction)
as an example to demonstrate the use of the `call_function`.

This module illustrates a technique for dynamically interacting with objects
and their methods at runtime.
"""

from typing import Optional


def call_function(obj: object, method_name: str, *args: float) -> Optional[float]:
    """
    Dynamically calls a method of an object by its name.

    Args:
        obj (object): The object on which to call the method.
        method_name (str): The name of the method as a string.
        *args (float): Variable-length argument list to be passed to the method.

    Returns:
        float: The result of the method call, or None if the method is not found.

    Raises:
        AttributeError: If the object does not have the specified method.
    """
    try:
        return getattr(obj, method_name)(*args)
    except AttributeError:
        print(f"{method_name} not found.")
        return None


class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts the second number from the first.

        Args:
            a (float): The first number (minuend).
            b (float): The second number (subtrahend).

        Returns:
            float: The difference between a and b.
        """
        return a - b


calc = Calculator()

print(call_function(calc, "add", 10, 5))  # 15
assert calc.add(10, 5) == 15, "Method add should return 15."

print(call_function(calc, "subtract", 10, 5))  # 5
assert calc.subtract(10, 5) == 5, "Method subtract should return 5."
