"""
Module for extracting URLs from text using regular expressions.
"""

import re
from typing import List


def extract_urls(text: str) -> List[str]:
    """
    Extracts all URLs from the given text.

    Args:
        text (str): The text containing URLs.

    Returns:
        List[str]: A list of found URLs.
    """

    pattern = r"https?://(?:www\.)?\S+"

    return re.findall(pattern, text)


if __name__ == "__main__":
    SAMPLE_TEXT = "Check https://example.com and http://test.net for info."

    print(extract_urls(SAMPLE_TEXT))
