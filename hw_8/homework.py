"""
This module demonstrates various Python concepts and features, including:

- **Function definitions and docstrings:** With type hints and doctests.
- **Filtering and mapping:** Using `filter()` and list comprehensions.
- **Type handling:** Using `Union`, `Optional`, and `TypeVar`.
- **Higher-order functions:** Using functions as arguments.
- **Decorators:** Using `@staticmethod` and `@abstractmethod`.
- **Abstract Base Classes (ABCs):** Defining and using ABCs.
- **Metaclasses:** Creating a custom metaclass to prevent inheritance.
- **TypedDict:** Defining a custom type for data structures.
- **Protocol definitions:** Defining a protocol for presentation.
- **Generic types:** Using TypeVar for generic types.
- **Asynchronous programming:** Using `asyncio` for asynchronous tasks.
- **Unit testing:** Using `doctest` and `pytest` for testing.

This module provides examples of these concepts and demonstrates their usage in various scenarios.
"""

import asyncio
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple, Union, Optional, TypeVar, Callable, \
    Protocol, TypedDict, Generic, Any, Awaitable


# ====================================
# TASK 1
# ====================================

def calculate_discount(price: float, discount: float) -> float:
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): Price to apply discount to.
        discount (float): Discount to apply discount to.

    Returns:
        float: Final price after discount.

    Examples:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50, 110)
        0.0
    """

    if discount >= 100:
        return 0.0

    return price * (1 - discount / 100)


print("=== TASK 1 ===")
print(calculate_discount(100, 20))  # 80.0
print(calculate_discount(50, 110))  # 0.0


# ====================================
# TASK 2
# ====================================

def filter_adults(people: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Filters out adults (18+) from a list of people.

    Args:
        people (List[Tuple[str, int]]): List of tuples (name, age).

    Returns:
        List[Tuple[str, int]]: List of tuples containing only adults.

    Examples:
        >>> filter_adults([("John", 25), ("Alice", 16), ("Bob", 19), ("Jane", 15)])
        [('John', 25), ('Bob', 19)]
    """

    return list(filter(lambda person: person[1] >= 18, people))


print("=== TASK 2 ===")
people_to_filter = [("John", 25), ("Alice", 16), ("Bob", 19), ("Jane", 15)]
print(filter_adults(people_to_filter))  # [('John', 25), ('Bob', 19)]


# ====================================
# TASK 3
# ====================================

def parse_input(value: Union[int, str]) -> Optional[int]:
    """
    Parses the input into an integer if possible.

    Args:
        value (Union[int, str]): An integer or string to convert.

    Returns:
        Optional[int]: Integer if conversion is successful, otherwise None.

    Examples:
        >>> parse_input(42)
        42
        >>> parse_input("100")
        100
        >>> parse_input("hello") is None
        True
    """

    if isinstance(value, int):
        return value

    try:
        return int(value)
    except ValueError:
        return None


print("=== TASK 3 ===")
print(parse_input(42))  # 42
print(parse_input("100"))  # 100
print(parse_input("hello"))  # None

# ====================================
# TASK 4
# ====================================

T = TypeVar('T')


def get_first(items: List[T]) -> Optional[T]:
    """
    Returns the first element of a list or None if the list is empty.

    Args:
        items (List[T]): List of any type.

    Returns:
        Optional[T]: First element of the list or None.

    Examples:
        >>> get_first([1, 2, 3])
        1
        >>> get_first(["a", "b", "c"])
        'a'
        >>> get_first([])

    """

    return items[0] if items else None


print("=== TASK 4 ===")
print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None


# ====================================
# TASK 5
# ====================================

def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    """
    Applies a given function to an integer.

    Args:
        x (int): The input integer.
        operation (Callable[[int], int]): A function that takes an integer and returns an integer.

    Returns:
        int: The result of applying `operation` to `x`.

    Examples:
        >>> apply_operation(5, square)
        25
        >>> apply_operation(5, double)
        10
    """

    return operation(x)


def square(x: int) -> int:
    """
    Calculates the square of an integer.

    Args:
        x (int): The integer to be squared.

    Returns:
        int: The square of the integer.

    Examples:
        >>> square(5)
        25
        >>> square(3)
        9
    """

    return x ** 2


def double(x: int) -> int:
    """
    Doubles an integer.

    Args:
        x (int): The integer to be doubled.

    Returns:
        int: The integer multiplied by 2.

    Examples:
        >>> double(5)
        10
        >>> double(3)
        6
    """

    return x * 2


print("=== TASK 5 ===")
print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10


# ====================================
# TASK 7
# ====================================

class User(TypedDict):
    """
    Represents a user with an ID, name, and admin status.
    """

    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    """
    Protocol for user database interactions.
    """

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve

        Returns:
            Optional[User]: The user if found, None otherwise
        """

    def save_user(self, user: User) -> None:
        """
        Save a user to the database.

        Args:
            user (User): The user to save
        """


class InMemoryUserDB(UserDatabase):
    """
    An in-memory implementation of the UserDatabase protocol.

    Attributes:
        _users (Dict[int, User]): A dictionary mapping IDs to Users.
    """

    def __init__(self) -> None:
        """
        Initializes an empty dictionary to store users.
        """

        self._users: Dict[int, User] = {}

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID from the in-memory database.

        Args:
            user_id (int): The ID of the user to retrieve

        Returns:
            Optional[User]: The user if found, None otherwise
        """

        return self._users.get(user_id, None)

    def save_user(self, user: User) -> None:
        """
        Save a user to the in-memory database.

        Args:
            user (User): The user to save
        """

        self._users[user["id"]] = user


print("=== TASK 7 ===")

db = InMemoryUserDB()

db.save_user({"id": 1, "name": "Alice", "is_admin": False})
print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
print(db.get_user(2))  # None

db.save_user({"id": 2, "name": "Bob", "is_admin": True})
print(db.get_user(2))  # {"id": 2, "name": "Bob", "is_admin": True}

# ====================================
# TASK 8
# ====================================

V = TypeVar('V')


class Processor(Generic[T]):
    """
    A generic processor class that applies a transformation function to a list of items.
    """

    def __init__(self, data: List[T]) -> None:
        """
        Initializes the Processor with a list of items.

        Args:
            data (List[T]): The list of items to process.
        """

        self.data = data

    def apply(self, func: Callable[[T], T]) -> List[T]:
        """
        Applies a transformation function to each item in the data list.

        Args:
            func (Callable[[T], T]): A function that takes an item of type T \
                                     and returns a transformed item of type T.

        Returns:
            List[T]: A new list containing the transformed items.
        """

        return [func(item) for item in self.data]


def to_upper(s: str) -> str:
    """
    Converts the input string to uppercase.

    Args:
        s (str): The input string.

    Returns:
        str: The uppercase version of the input string.

    Examples:
        >>> to_upper("hello")
        'HELLO'
        >>> to_upper("WoRlD")
        'WORLD'
    """

    return s.upper()


print("=== TASK 8 ===")

p1 = Processor([1, 2, 3])
print(p1.apply(double))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(to_upper))  # ["HELLO", "WORLD"]

p3 = Processor([1, 2, 3])
print(p3.apply(lambda x: x * 2))  # [2, 4, 6]


# ====================================
# TASK 9
# ====================================

class FinalMeta(type):
    """
    A metaclass that prevents inheritance from classes marked as final.
    """

    def __new__(cls, name: str, bases: Tuple, class_dict: Dict) -> type:
        """
        Creates a new class using the metaclass logic.

        Args:
            name (str): The name of the class being created.
            bases (tuple): The base classes of the class being created.
            class_dict (dict): The class dictionary of the class being created.

        Returns:
            type: The newly created class.

        Raises:
            TypeError: If a class attempts to inherit from a final class.
        """

        for base in bases:
            if isinstance(base, FinalMeta):
                raise TypeError(f"Class '{name}' cannot inherit from final class '{base.__name__}'")

        return super().__new__(cls, name, bases, class_dict)


class Config(metaclass=FinalMeta):
    """
    A final configuration class that cannot be inherited.

    Attributes:
        settings (Dict[str, Any]): A dictionary to store configuration settings.
    """

    def __init__(self) -> None:
        """
        Initializes the Config instance with an empty settings dictionary.
        """

        self.settings: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """
        Sets a configuration value for a given key.

        Args:
            key (str): The configuration key.
            value (Any): The configuration value to set.
        """

        self.settings[key] = value

    def get(self, key: str) -> Any:
        """
        Retrieves the configuration value for a given key.

        Args:
            key (str): The configuration key.

        Returns:
            Any: The configuration value associated with the key, or None if the key does not exist.
        """

        return self.settings.get(key)


class BaseRepository(ABC):
    """
    An abstract base class for repositories.
    """

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """
        Saves data to the repository.

        Args:
            data (Dict[str, Any]): The data to save.
        """


class SQLRepository(BaseRepository):
    """
    A concrete implementation of BaseRepository for saving data to an SQL database.
    """

    def save(self, data: Dict[str, Any]) -> None:
        """
        Saves data to the SQL database.

        Args:
            data (Dict[str, Any]): The data to save.
        """

        print("Saving data to SQL database:", data)


print("=== TASK 9 ===")

repo = SQLRepository()

repo.save({"name": "Product1", "price": 10.5})

try:
    class DerivedConfig(Config):
        """
        A derived configuration class that cannot be inherited.
        """
except TypeError as e:
    print(e)


# ====================================
# TASK 10
# ====================================

class AsyncFetcher:
    """
    A class for fetching data asynchronously.
    """

    async def fetch(self, url: str) -> Awaitable[Dict[str, Any]]:
        """
        Fetches data from a given URL asynchronously.

        Args:
           url (str): The URL to fetch data from.

        Returns:
           Dict[str, Any]: A dictionary containing the fetched data.
        """

        print(f"Fetching data from {url}...")

        async def task():
            """
            A simulated asynchronous task that returns sample data.

            Returns:
                Dict[str, Any]: A dictionary containing the sample response.
            """

            return {"url": url, "data": "Sample response"}

        await asyncio.sleep(1)

        return await asyncio.create_task(task())


async def main() -> None:
    """
    Demonstrates the usage of AsyncFetcher by fetching data from a sample URL.
    """

    fetcher = AsyncFetcher()
    result = await fetcher.fetch("https://example.com/api")

    print(result)


print("=== TASK 10 ===")

asyncio.run(main())

if __name__ == "__main__":
    pass
