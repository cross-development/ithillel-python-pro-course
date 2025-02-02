from hw_6.hw_6_6.handlers.csv_handler import CsvHandler
from hw_6.hw_6_6.handlers.json_handler import JsonHandler


class CsvToJsonAdapter:
    """
    Adapter to convert data from CSV to JSON format.
    """

    def __init__(self, csv_handler: CsvHandler, json_handler: JsonHandler) -> None:
        """
        Initializes the CsvToJsonAdapter.

        Args:
            csv_handler (CsvHandler): An instance of the CsvHandler.
            json_handler (JsonHandler): An instance of the JsonHandler.
        """

        self.csv_handler = csv_handler
        self.json_handler = json_handler

    def convert_csv_to_json(self, csv_file: str, json_file: str) -> None:
        """
        Converts data from a CSV file to a JSON file.

        Args:
            csv_file (str): The path to the CSV file.
            json_file (str): The path to the JSON file.
        """

        try:
            data = self.csv_handler.read_csv(csv_file)
            self.json_handler.write_json(json_file, data)
        except Exception as e:
            print(f"Error converting CSV to JSON: {e}")
