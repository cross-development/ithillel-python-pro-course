"""
This module demonstrates a decorator for logging method calls in a class.

The `log_methods` decorator modifies a class by wrapping each of its methods
with a logging function. This allows you to track which methods are called
and with what arguments, providing insights into the object's behavior.

The `MyClass` class with `add` and `subtract` methods serves as an example
to demonstrate the usage of the `log_methods` decorator.
"""

import inspect


def log_methods(cls: type) -> type:
    """
    A decorator to log method calls in a class, including the method name and arguments.

    Args:
        cls (type): The class to be decorated.

    Returns:
        type: The decorated class with logged method calls.
    """

    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith("__") or not callable(method):
            continue

        def make_wrapper(method_name: str, original_method: callable) -> callable:
            """
            Creates a wrapper function that logs the call to the original method.

            Args:
                method_name (str): The name of the original method.
                original_method (callable): The original method to be wrapped.

            Returns:
                callable: The wrapper function.
            """

            def wrapper(self, *args, **kwargs) -> any:
                """
                Logs the call to the original method and then calls it.

                Args:
                    self: The instance of the class.
                    *args: Positional arguments for the original method.
                    **kwargs: Keyword arguments for the original method.

                Returns:
                    any: The return value of the original method.
                """
                print(f"Logging: {method_name} called with {args}, {kwargs}")
                return original_method(self, *args, **kwargs)

            return wrapper

        setattr(cls, name, make_wrapper(name, method))

    return cls


@log_methods
class MyClass:
    """
    A class with methods to add and subtract numbers.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts two numbers.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: The difference of the two numbers.
        """
        return a - b


obj = MyClass()

obj.add(5, 3)  # Logging: add called with (5, 3)
assert obj.add(5, 3) == 8, "Should return 8"

obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
assert obj.subtract(5, 3) == 2, "Should return 2"
