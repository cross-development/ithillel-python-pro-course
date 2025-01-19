class TypeCheckedMeta(type):
    """
    A metaclass that ensures type checking for attributes when they are set.
    """

    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        Creates a new class, and modifies the class dictionary to include a custom
        __setattr__ method that performs type checking on attribute assignments.

        Args:
            name (str): The name of the class being created.
            bases (tuple): The base classes of the class being created.
            dct (dict): The dictionary containing the class body, including its attributes and methods.

        Returns:
            type: The newly created class with the custom __setattr__ method.
        """
        original_setattr = dct.get('__setattr__')

        def custom_setattr(self, key: str, value: any) -> None:
            """
            Sets the attribute value, with type checking.

            Args:
                self: The instance of the class.
                key (str): The name of the attribute being set.
                value (any): The value being assigned to the attribute.

            Raises:
                TypeError: If the value type does not match the declared type in __annotations__.
            """
            if key in self.__annotations__:
                expected_type = self.__annotations__[key]

                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"'{key}' should be of type '{expected_type.__name__}', got '{type(value).__name__}'")

            if original_setattr:
                original_setattr(self, key, value)
            else:
                super(self.__class__, self).__setattr__(key, value)

        dct['__setattr__'] = custom_setattr

        return super().__new__(cls, name, bases, dct)


class Person(metaclass=TypeCheckedMeta):
    """
    A class representing a person with type-checked attributes.

    Attributes:
        name (str): The name of the person. Defaults to an empty string.
        age (int): The age of the person. Defaults to 0.
    """
    name: str = ""
    age: int = 0


p = Person()

p.name = "John"  # Все добре
assert p.name == "John", "Should be John"
assert p.age == 0, "Should be 0"

p.age = "30"  # Викличе помилку, очікується int
