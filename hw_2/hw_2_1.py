"""
This module demonstrates object introspection in Python.

The `analyze_object` function provides a basic inspection of a given object.
It prints the object's type and a list of its attributes and methods.

The `MyClass` class is a simple example class used to demonstrate the
object introspection functionality.

This module provides a basic example of how to explore the structure
and attributes of Python objects.
"""


def analyze_object(o: object) -> None:
    """
    Analyze object and print its type, attributes, and methods.

    Args:
        o (object): Any Python object

    Returns:
        None: Prints analysis results
    """
    print(f"Object type: {type(o)}")
    print("Attributes and methods:")

    for name in dir(o):
        if not name.startswith("__"):
            attr = getattr(o, name)
            print(f"- {name}: {type(attr)}")


class MyClass:
    """
    A simple class with a single attribute and a method.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a MyClass object with the given value.

        Args:
            value (str): The string value to assign to the 'value' attribute.
        """
        self.value = value

    def say_hello(self) -> str:
        """
        Returns a greeting message.

        Returns:
            str: A string containing the greeting message.
        """
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
