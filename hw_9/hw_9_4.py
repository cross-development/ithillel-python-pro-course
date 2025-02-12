"""
Module for converting date format from DD/MM/YYYY to YYYY-MM-DD.
"""

import re


def format_date(date: str) -> str:
    """
    Converts a date from DD/MM/YYYY to YYYY-MM-DD format.

    Args:
        date (str): The date in DD/MM/YYYY format.

    Returns:
        str: The date in YYYY-MM-DD format.
    """

    pattern = r"(\d{2})/(\d{2})/(\d{4})"

    return re.sub(pattern, r"\3-\2-\1", date)


if __name__ == "__main__":
    dates = ["25/12/2023", "01/01/2024", "15/08/2022"]

    for d in dates:
        print(f"{d} -> {format_date(d)}")
