"""
Module for extracting IPv4 addresses from text using regular expressions.
"""

import re
from typing import List


def extract_ip_addresses(text: str) -> List[str]:
    """
    Extracts all IPv4 addresses from the given text.

    Args:
        text (str): The text containing IPv4 addresses.

    Returns:
        List[str]: A list of found IPv4 addresses.
    """

    pattern = r"\b(?:[01]?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:[01]?\d\d?|2[0-4]\d|25[0-5])){3}\b"

    return re.findall(pattern, text)


if __name__ == "__main__":
    SAMPLE_TEXT = "Server logs: 192.168.1.1, 10.0.0.5, and 8.8.8.8. Incorrect IPv4: 266.0.0.0."

    print(extract_ip_addresses(SAMPLE_TEXT))
