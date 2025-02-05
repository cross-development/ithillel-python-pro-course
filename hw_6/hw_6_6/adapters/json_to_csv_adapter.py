"""
This module defines the JsonToCsvAdapter class, which adapts the JsonHandler and CsvHandler
interfaces to enable seamless conversion of data between JSON and CSV formats.

The JsonToCsvAdapter:

- Uses the JsonHandler to read data from a JSON file.
- Uses the CsvHandler to write the data to a CSV file.
- Handles potential exceptions during the conversion process.

This adapter facilitates the integration of different data handling components
without requiring direct knowledge of their internal implementations.
"""

from hw_6.hw_6_6.handlers.csv_handler import CsvHandler
from hw_6.hw_6_6.handlers.json_handler import JsonHandler


class JsonToCsvAdapter:
    """
    Adapter to convert data from JSON to CSV format.
    """

    def __init__(self, json_handler: JsonHandler, csv_handler: CsvHandler) -> None:
        """
        Initializes the JsonToCsvAdapter.

        Args:
            json_handler (JsonHandler): An instance of the JsonHandler.
            csv_handler (CsvHandler): An instance of the CsvHandler.
        """

        self.json_handler = json_handler
        self.csv_handler = csv_handler

    def convert_json_to_csv(self, json_file: str, csv_file: str) -> None:
        """
        Converts data from a JSON file to a CSV file.

        Args:
            json_file (str): The path to the JSON file.
            csv_file (str): The path to the CSV file.
        """

        try:
            data = self.json_handler.read_json(json_file)
            self.csv_handler.write_csv(csv_file, data)
        except Exception as e:
            print(f"Error converting JSON to CSV: {e}")
