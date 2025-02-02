import csv
from typing import List, Dict


class CsvHandler:
    """
    Class for reading and writing CSV files.
    """

    def read_csv(self, file_path: str) -> List[Dict]:
        """
        Reads data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents a row in the CSV file.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: For any other errors during reading.
        """

        try:
            with open(file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")

    def write_csv(self, file_path: str, data: List[Dict]) -> None:
        """
        Writes data to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            data (List[Dict]): A list of dictionaries, where each dictionary represents a row to be written.

        Raises:
            Exception: For any errors during writing.
        """

        if not data:
            return

        try:
            with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise Exception(f"Error writing to CSV file: {e}")
