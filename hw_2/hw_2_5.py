"""
This module defines a MutableClass that allows dynamic modification of its attributes.

The MutableClass provides methods to:

- Add new attributes to the object dynamically.
- Remove existing attributes from the object dynamically.

This demonstrates a mechanism for changing the object's structure at runtime.
"""


class MutableClass:
    """
    A class that allows dynamic addition and removal of attributes during execution.
    """

    def add_attribute(self, name: str, value: any) -> None:
        """
        Add an attribute to the object dynamically.

        Args:
            name (str): The name of the attribute to add.
            value (any): The value to assign to the attribute.
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """
        Remove an attribute from the object dynamically.

        Args:
            name (str): The name of the attribute to remove.
        """
        if hasattr(self, name):
            delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python
assert obj.name == "Python", "Returns value 'Python'"

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений
