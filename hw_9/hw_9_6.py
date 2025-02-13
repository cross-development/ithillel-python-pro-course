"""
Module for validating passwords using regular expressions.
"""

import re


def is_strong_password(password: str) -> bool:
    """
    Checks if the given password is strong.

    A password is considered strong if it:
        - contains at least 8 characters,
        - contains at least one digit,
        - contains at least one uppercase letter and one lowercase letter,
        - contains at least one special character (@, #, $, %, &, etc.).

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is strong, False otherwise.
    """

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"

    return bool(re.match(pattern, password))


if __name__ == "__main__":
    passwords = ["Strong@123", "weakpass", "NoSpecial123", "Short1@"]

    for p in passwords:
        print(f"{p}: {is_strong_password(p)}")
