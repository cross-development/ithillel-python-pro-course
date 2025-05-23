"""
This module defines the SaveAsCsv class, a concrete implementation
of the SaveStrategy interface.

The SaveAsCsv class provides functionality for saving content to a CSV file.
It writes the given content as a single row in the CSV file.
"""

import csv

from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class SaveAsCsv(SaveStrategy):
    """
    Concrete class for saving content as a CSV file.
    """

    def save(self, content: str, filename: str) -> None:
        """
        Saves content as a CSV file.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["HTML Content"])
            writer.writerow([content])

        print(f"CSV-file has been saved: {filename}")
