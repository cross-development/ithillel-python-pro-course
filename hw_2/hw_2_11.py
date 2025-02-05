"""
This module demonstrates a metaclass that limits the number of attributes
a class can have.

The `LimitedAttributesMeta` metaclass checks the number of attributes
defined in a class during its creation. If the number of attributes
exceeds the maximum allowed limit, it raises a TypeError.

The `LimitedClass` class uses the `LimitedAttributesMeta` metaclass
to enforce a limit of 3 attributes.

This module provides an example of how to use metaclasses to control
the creation and structure of classes.
"""


class LimitedAttributesMeta(type):
    """
    A metaclass that ensures a class has a limited number of attributes.
    """

    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        This method checks the number of attributes of the class and raises an error
        if it exceeds the maximum allowed limit.

        Args:
            name (str): The name of the class being created.
            bases (tuple): A tuple of base classes.
            dct (dict): A dictionary of the class's attributes.

        Returns:
            type: The newly created class.

        Raises:
            TypeError: If the class has more attributes than allowed.
        """
        max_attributes = 3  # Maximum number of allowed attributes

        # Count the number of attributes in the class (excluding special methods like __init__)
        attribute_count = len([key for key in dct if not key.startswith('__')])

        if attribute_count > max_attributes:
            raise TypeError(f"Class {name} cannot have more than {max_attributes} attributes.")

        return super().__new__(cls, name, bases, dct)


class LimitedClass(metaclass=LimitedAttributesMeta):
    """
    A class that demonstrates the use of the LimitedAttributesMeta metaclass.
    This class is limited to having only 3 attributes.

    Attributes:
        attr1 (int): An integer attribute.
        attr2 (int): Another integer attribute.
        attr3 (int): A third integer attribute.
    """

    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку


obj = LimitedClass()
