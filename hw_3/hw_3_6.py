import re


class User:
    """
    Represents a user with a first name, last name, and email address.

    Attributes:
        _first_name (str): The user's first name (private attribute).
        _last_name (str): The user's last name (private attribute).
        _email (str): The user's email address (private attribute).
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """
        Initializes a User object.

        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.

        Raises:
            ValueError: If the first name or last name is empty.
            ValueError: If the email address is invalid.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self) -> str:
        """
        Gets the user's first name.

        Returns:
            str: The user's first name.
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Sets the user's first name.

        Args:
            value (str): The new first name for the user.

        Raises:
            ValueError: If the first name is empty.
        """
        if not value.strip():
            raise ValueError("First name cannot be empty.")

        self._first_name = value.strip()

    @property
    def last_name(self) -> str:
        """
        Gets the user's last name.

        Returns:
            str: The user's last name.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """
        Sets the user's last name.

        Args:
            value (str): The new last name for the user.

        Raises:
            ValueError: If the last name is empty.
        """
        if not value.strip():
            raise ValueError("Last name cannot be empty.")

        self._last_name = value.strip()

    @property
    def email(self) -> str:
        """
        Gets the user's email address.

        Returns:
            str: The user's email address.
        """
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """
        Sets the user's email address.

        Args:
            value (str): The new email address for the user.

        Raises:
            ValueError: If the email address is invalid.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex, value):
            raise ValueError(f"Invalid email format: {value}")

        self._email = value.strip()


user = User("John", "Doe", "john.doe@example.com")
print(f"User created: {user.first_name} {user.last_name}, {user.email}")

user.first_name = "Jane"
print(f"First name updated: {user.first_name}")
assert user.first_name == "Jane", "First name should be Jane."

user.last_name = "Smith"
print(f"Last name updated: {user.last_name}")
assert user.last_name == "Smith", "Last name should be Smith."

user.email = "jane.smith@example.com"
print(f"Email updated: {user.email}")
assert user.email == "jane.smith@example.com", "Email should be jane.smith@example.com."

# user.email = "invalid_email"  # Should raise an error "Invalid email format"
# user.first_name = ""  # Should raise an error "First name cannot be empty"
# user.last_name = ""  # Should raise an error "Last name cannot be empty"

print("All tests passed!")
