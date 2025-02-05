"""
This module defines the JsonHandler class, providing methods for reading and
writing data to JSON files.

Key functionalities:

- `read_json(file_path)`: Reads data from a JSON file and returns it as a list of dictionaries.
- `write_json(file_path, data)`: Writes a list of dictionaries to a JSON file.

The class includes robust error handling for potential issues during file operations
and JSON data processing.
"""

import json
from typing import List, Dict


class JsonHandler:
    """
    Class for reading and writing JSON files.
    """

    def read_json(self, file_path: str) -> List[Dict]:
        """
        Reads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            List[Dict]: A list of dictionaries representing the data read from the JSON file.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
            Exception: For any other errors during reading.
        """

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format in file {file_path}.", e.doc, e.pos)
        except Exception as e:
            raise Exception(f"Error reading JSON file: {e}")

    def write_json(self, file_path: str, data: List[Dict]) -> None:
        """
        Writes data to a JSON file.

        Args:
            file_path (str): The path to the JSON file.
            data (List[Dict]): A list of dictionaries to be written to the JSON file.

        Raises:
            Exception: For any errors during writing.
        """

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise Exception(f"Error writing to JSON file: {e}")
