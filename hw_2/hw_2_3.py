"""
This module provides a function to analyze a Python module.

The `analyze_module` function imports a specified module and
prints information about its functions and classes,
including their names and signatures.

This module demonstrates a simple way to introspect
and gather information about the contents of a Python module.
"""

import inspect
import importlib


def analyze_module(module_name: str) -> None:
    """
    Analyze a Python module and print its functions and classes with signatures.

    Args:
        module_name (str): Name of the module to analyze

    Returns:
        None: Prints analysis results

    Raises:
        ImportError: If module cannot be imported
    """
    try:
        module = importlib.import_module(module_name)

        print("Functions:")

        functions = inspect.getmembers(module, inspect.isfunction)

        if functions:
            for name, func in functions:
                print(f"- {name}{str(inspect.signature(func))}")
        else:
            print("- <No functions in this module>")

        print("\nClasses:")

        classes = inspect.getmembers(module, inspect.isclass)

        if classes:
            for class_name, _ in classes:
                print(f"- {class_name}")
        else:
            print("- <No classes in this module>")

    except ImportError:
        print(f"Module '{module_name}' not found.")


analyze_module("math")
