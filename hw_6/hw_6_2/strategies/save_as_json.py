"""
This module defines the SaveAsJson class, a concrete implementation of the SaveStrategy interface.

The SaveAsJson class provides functionality for saving content to a JSON file.
It stores the content within a 'content' key within the JSON object.
"""

import json

from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class SaveAsJson(SaveStrategy):
    """
    Concrete class for saving content as a JSON file.
    """

    def save(self, content: str, filename: str) -> None:
        """
        Saves content as a JSON file.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        data = {"content": content}

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"JSON-file has been saved: {filename}")
