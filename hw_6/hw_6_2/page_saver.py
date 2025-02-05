"""
This module defines the PageSaver class, which provides a flexible mechanism
for saving downloaded web page content using different save strategies.

The PageSaver:

- Encapsulates a specific SaveStrategy instance.
- Allows dynamic switching of the save strategy at runtime.
- Provides a consistent interface for saving content regardless of the chosen strategy.

This class promotes code flexibility and maintainability by decoupling the
page saving logic from the specific file format used for storage.
"""

from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class PageSaver:
    """
    Class for saving downloaded web page content using different strategies.
    """

    def __init__(self, strategy: SaveStrategy) -> None:
        """
        Initializes the PageSaver with a given save strategy.

        Args:
            strategy (SaveStrategy): The initial save strategy to use.
        """

        self.strategy = strategy

    def set_strategy(self, strategy: SaveStrategy) -> None:
        """
        Sets a new save strategy.

        Args:
            strategy (SaveStrategy): The new save strategy to use.
        """

        self.strategy = strategy

    def save(self, content: str, filename: str) -> None:
        """
        Saves the given content using the current save strategy.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        self.strategy.save(content, filename)
