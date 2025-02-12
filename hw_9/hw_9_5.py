"""
Module for removing HTML tags from text using regular expressions.
"""

import re


def remove_html_tags(text: str) -> str:
    """
    Removes all HTML tags from the given text.

    Args:
        text (str): The text containing HTML tags.

    Returns:
        str: The cleaned text without HTML tags.
    """

    pattern = r"<.*?>"

    return re.sub(pattern, "", text)


if __name__ == "__main__":
    HTML_TEXT = "<p>Hello, <b>world</b>!</p>"

    print(remove_html_tags(HTML_TEXT))
