"""
This module defines the SaveAsTxt class, a concrete implementation of the SaveStrategy interface.

The SaveAsTxt class provides functionality for saving content to a plain text (TXT) file.
"""

from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class SaveAsTxt(SaveStrategy):
    """
    Concrete class for saving content as a TXT file.
    """

    def save(self, content: str, filename: str) -> None:
        """
        Saves content as a TXT file.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"TXT-file has been saved: {filename}")
