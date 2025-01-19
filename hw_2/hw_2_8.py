import inspect


def analyze_inheritance(cls: type) -> None:
    """
    Analyzes the inheritance of a class and prints the methods inherited from its base classes.

    Args:
        cls (type): The class to analyze.
    """
    print(f"Class {cls.__name__} inherits:")

    # Get all methods from the base classes
    for base in cls.__mro__[1:]:  # Skip the class itself, start from base classes
        for name, method in inspect.getmembers(base, inspect.isfunction):
            print(f"- {name} from {base.__name__}")


class Parent:
    """
    A base class that defines a method for its subclasses to inherit.
    """

    def parent_method(self) -> None:
        """
        A method that does nothing but can be inherited by subclasses.
        """
        pass


class Child(Parent):
    """
    A child class that inherits from Parent and adds its own method.
    """

    def child_method(self) -> None:
        """
        A method specific to the Child class.
        """
        pass


analyze_inheritance(Child)
