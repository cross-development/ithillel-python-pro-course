"""
This module demonstrates a Proxy pattern implementation.

The `Proxy` class intercepts method calls to another object and logs the
method name and arguments before delegating the call to the original object.

This provides a mechanism for observing and potentially modifying
method calls without changing the original object's code.

The `MyClass` and `Proxy` classes are used as an example to demonstrate
the usage of the Proxy pattern.
"""


class Proxy:
    """
    A Proxy class that intercepts method calls to another object, \
    logging the method name and arguments.
    """

    def __init__(self, o: object) -> None:
        """
        Initializes the Proxy with the object to be proxied.

        Args:
            o (object): The object to be proxied.
        """
        self._obj = o

    def __getattr__(self, name: str) -> callable:
        """
        Intercepts method calls and logs the method name and arguments \
        before calling the method on the original object.

        Args:
            name (str): The name of the method being called.

        Returns:
            callable: A wrapper function that logs the method call and arguments, \
                      then calls the original method.
        """

        method = getattr(self._obj, name)

        def wrapper(*args, **kwargs) -> any:
            """
            Wrapper function that logs method calls with arguments.

            Args:
                *args: Positional arguments passed to the method.
                **kwargs: Keyword arguments passed to the method.

            Returns:
                any: The result of the original method call.
            """
            print(f"Calling method:\n{name} with args: {args}")

            return method(*args, **kwargs)

        return wrapper


class MyClass:
    """
    A simple class with a method to greet a user.
    """

    def greet(self, name: str) -> str:
        """
        Greets the user with a message.

        Args:
            name (str): The name of the user.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))
assert proxy.greet("Alice") == "Hello, Alice!", "Should return 'Hello, Alice!'"
