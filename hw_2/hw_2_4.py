"""
This module demonstrates dynamic class creation in Python.

The `create_class` function allows you to dynamically create a new class
with a given name and a dictionary of methods. This provides a flexible way
to define classes at runtime.

The module includes an example of creating a dynamic class with
`say_hello` and `say_goodbye` methods, demonstrating the usage of the
`create_class` function.
"""


def create_class(class_name: str, class_methods: dict[str, callable]) -> type:
    """
    Create a class dynamically with the given class name and methods.

    Args:
        class_name (str): The name of the class to create.
        class_methods (dict[str, callable]): A dictionary where the keys are method names
                        and the values are functions to be used as methods.

    Returns:
        type: A new class with the given methods.
    """
    return type(class_name, (object,), class_methods)


def say_hello(self) -> str:
    """
    Say hello.

    Returns:
        str: Greeting message.
    """
    return "Hello!"


def say_goodbye(self) -> str:
    """
    Say goodbye.

    Returns:
        str: Farewell message.
    """
    return "Goodbye!"


methods = {
    "say_hello": say_hello,
    "say_goodbye": say_goodbye
}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()

print(obj.say_hello())  # Hello!
assert obj.say_hello() == "Hello!", "Method say_hello should return 'Hello!'"

print(obj.say_goodbye())  # Goodbye!
assert obj.say_goodbye() == "Goodbye!", "Method say_goodbye should return 'Goodbye!'"
