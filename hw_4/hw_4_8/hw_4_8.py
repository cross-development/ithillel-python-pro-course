import json
from typing import Any, Dict


class ConfigManager:
    """
    A context manager for working with JSON configuration files.
    Automatically reads the configuration file on entry and writes changes back on exit.

    Attributes:
        file_path (str): Path to the JSON configuration file.
        config (Dict[str, Any]): Dictionary holding the configuration data.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initializes the ConfigManager with the path to the configuration file.

        Args:
            file_path (str): The path to the JSON configuration file.
        """
        self.file_path = file_path
        self.config: Dict[str, Any] = {}

    def __enter__(self) -> Dict[str, Any]:
        """
        Reads the configuration file and returns the configuration dictionary.

        Returns:
            Dict[str, Any]: The configuration data.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.config = json.load(file)

            print(f"Configuration loaded from '{self.file_path}'.")
        except FileNotFoundError:
            print(f"Configuration file '{self.file_path}' not found. Starting with an empty configuration.")
            self.config = {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{self.file_path}'. Starting with an empty configuration.")
            self.config = {}

        return self.config

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
        Writes the updated configuration back to the file.

        Args:
            exc_type (Any): The exception type if an exception was raised.
            exc_value (Any): The exception value if an exception was raised.
            traceback (Any): The traceback object if an exception was raised.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config, file, indent=4)

            print(f"Configuration saved to '{self.file_path}'.")
        except Exception as e:
            print(f"Failed to write configuration to '{self.file_path}': {e}")


config_file = "config.json"

with ConfigManager(config_file) as config:
    config["app_name"] = "My Application"
    config["version"] = "1.0.0"
    config["author"] = "Vitalii Derda"
    config["features"] = {
        "logging": True,
        "debug_mode": False
    }

print("All tests passed!")
