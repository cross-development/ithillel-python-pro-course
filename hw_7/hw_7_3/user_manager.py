"""
This module defines the UserManager class, which provides methods \
for managing a collection of users.

- `add_user(name, age)`: Adds a new user to the collection. \
                         Raises ValueError if the user already exists.
- `remove_user(name)`: Removes a user from the collection. \
                       Raises ValueError if the user is not found.
- `get_all_users()`: Returns a list of all users and their ages.
"""


class UserManager:
    """
    A class for managing a collection of users.
    """

    def __init__(self) -> None:
        """
        Initializes an empty dictionary to store users.
        """

        self.users: dict[str, int] = {}

    def add_user(self, name: str, age: int) -> None:
        """
        Adds a new user to the collection.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.

        Raises:
            ValueError: If a user with the same name already exists.
        """

        if name in self.users:
            raise ValueError("User already exists.")

        self.users[name] = age

    def remove_user(self, name: str) -> None:
        """
        Removes a user from the collection.

        Args:
            name (str): The name of the user to remove.

        Raises:
            ValueError: If the user is not found.
        """

        if name not in self.users:
            raise ValueError("User not found.")

        del self.users[name]

    def get_all_users(self) -> list[tuple[str, int]]:
        """
        Returns a list of all users and their ages.

        Returns:
            list[tuple[str, int]]: A list of tuples, where each tuple contains \
                                   the user's name and age.
        """

        return list(self.users.items())
