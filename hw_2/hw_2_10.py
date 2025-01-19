class SingletonMeta(type):
    """
    A metaclass that implements the Singleton pattern, ensuring that only one instance
    of a class is created.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """
        Ensures that only one instance of the class is created. If an instance already exists,
        it returns the existing one.

        Args:
            *args: Positional arguments passed to the class constructor.
            **kwargs: Keyword arguments passed to the class constructor.

        Returns:
            object: The single instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    A class that uses SingletonMeta to ensure only one instance is created.
    """

    def __init__(self) -> None:
        """
        Initializes the Singleton instance. This method is called only once during the creation of the first instance.
        """
        print("Creating instance")


obj1 = Singleton()  # Creating instance
obj2 = Singleton()

print(obj1 is obj2)  # True
assert obj1 is obj2, "Should be equal (the same instance)"
