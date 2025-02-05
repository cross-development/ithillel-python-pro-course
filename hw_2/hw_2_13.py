"""
This module demonstrates a metaclass that automatically generates
getter and setter methods for class attributes.

The `AutoMethodMeta` metaclass dynamically creates `get_{attr_name}`
and `set_{attr_name}` methods for each attribute defined in the class.

The `Person` class uses the `AutoMethodMeta` metaclass to demonstrate
the automatic generation of getter and setter methods for its 'name' and 'age' attributes.

This module provides an example of how to use metaclasses to
enhance class functionality and reduce boilerplate code.
"""


class AutoMethodMeta(type):
    """
    A metaclass that automatically generates getter and setter methods for each attribute.
    """

    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        This method generates getter and setter methods for each attribute in the class.

        Args:
            name (str): The name of the class being created.
            bases (tuple): A tuple of base classes.
            dct (dict): A dictionary of the class's attributes.

        Returns:
            type: The newly created class with auto-generated methods.
        """

        # Create a new dictionary to store generated methods
        methods = {}

        for attr_name, _ in dct.items():
            if not attr_name.startswith("__"):
                # Create a getter method
                def getter(self, attr_name=attr_name):
                    return getattr(self, attr_name)

                # Create a setter method
                def setter(self, value, attr_name=attr_name):
                    setattr(self, attr_name, value)

                # Add the getter and setter methods to the methods dictionary
                methods[f'get_{attr_name}'] = getter
                methods[f'set_{attr_name}'] = setter

        # Update the class dictionary with generated methods
        dct.update(methods)

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=AutoMethodMeta):
    """
    A class representing a person with auto-generated getter and setter methods.

    Attributes:
        name (str): The name of the person. Defaults to "John".
        age (int): The age of the person. Defaults to 30.
    """
    name = "John"
    age = 30


# Test the functionality
p = Person()

print(p.get_name())  # Should print "John"
assert p.get_name() == "John", "Should return 'John'."

assert p.age == 30, "Should be 30."

p.set_age(31)  # Should set the age to 31
print(p.get_age())  # Should print "31"
assert p.get_age() == 31, "Should return 31."
