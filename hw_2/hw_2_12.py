"""
This module demonstrates a metaclass that adds logging functionality
to attribute access and modification in a class.

The `LoggingMeta` metaclass intercepts attribute access and modification
operations and logs them to the console.

The `MyClass` class uses the `LoggingMeta` metaclass to demonstrate
the logging behavior.

This module provides an example of how to use metaclasses to modify
the behavior of classes in powerful ways.
"""


class LoggingMeta(type):
    """
    A metaclass that adds logging functionality to attribute access and modification in a class.
    """

    def __new__(cls, name: str, bases: tuple, dct: dict) -> type:
        """
        Create a new class with logging capabilities.

        Args:
            name (str): The name of the class being created
            bases (tuple): Base classes
            dct (dict): Dictionary of class attributes

        Returns:
            type: A new class type with logging functionality
        """

        def logged_getattribute(self, attr: str) -> any:
            """
            Logs access to non-special and non-service attributes of the object.

            Args:
                self: The instance of the class.
                attr (str): The name of the attribute being accessed.

            Returns:
                any: The value of the accessed attribute.
            """
            # Log access only for non-special and non-service attributes
            if not attr.startswith('_'):
                print(f"Logging: accessed '{attr}'")

            return super(result, self).__getattribute__(attr)

        def logged_setattr(self, attr: str, value: any) -> None:
            """
            Logs modification of non-special and non-service attributes of the object,
            excluding initialization.

            Args:
                self: The instance of the class.
                attr (str): The name of the attribute being modified.
                value (any): The new value to be assigned to the attribute.
            """
            # Skip logging for special, service attributes and during initialization
            initializing = self.__dict__.get('_initializing', False)

            if not attr.startswith('_') and not initializing:
                print(f"Logging: modified '{attr}'")

            super(result, self).__setattr__(attr, value)

        # Modify __init__ to add initialization flag
        original_init = dct.get('__init__')

        def __init__(self, *args, **kwargs) -> None:
            """
            Initializes the object and sets the initialization flag.

            Args:
                *args: Positional arguments passed to the original __init__ method.
                **kwargs: Keyword arguments passed to the original __init__ method.
            """
            self._initializing = True
            original_init(self, *args, **kwargs)
            self._initializing = False

        # Add logging methods to the class
        dct['__getattribute__'] = logged_getattribute
        dct['__setattr__'] = logged_setattr
        dct['__init__'] = __init__

        # Create the class
        result = super().__new__(cls, name, bases, dct)
        return result


class MyClass(metaclass=LoggingMeta):
    """
    A class with logging for attribute access and modification.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the object with a name attribute.

        Args:
            name (str): The name to be assigned to the object.
        """
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
