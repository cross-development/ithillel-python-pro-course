"""
Module for validation email addresses using regular expressions.
"""

import re


def is_valid_email(email: str) -> bool:
    """
    Checks if the given email address is valid.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """

    pattern = r"^[a-zA-Z0-9](?:[a-zA-Z0-9.]*[a-zA-Z0-9])?@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"

    return bool(re.match(pattern, email))


if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "john.doe@domain.net",
        ".invalid@domain.com",
        "invalid.@domain.com",
        "user@domain",
        "user@domain.toolongtld"
    ]

    for e in test_emails:
        print(f"{e}: {is_valid_email(e)}")
