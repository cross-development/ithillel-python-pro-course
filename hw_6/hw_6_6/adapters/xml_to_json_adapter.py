"""
This module defines the XmlToJsonAdapter class, which adapts the XmlHandler and JsonHandler
presentation to enable seamless conversion of data between XML and JSON formats.

The XmlToJsonAdapter:

- Uses the XmlHandler to read data from an XML file.
- Uses the JsonHandler to write the data to a JSON file.
- Handles potential exceptions during the conversion process.

This adapter facilitates the integration of different data handling components
without requiring direct knowledge of their internal implementations.
"""

from hw_6.hw_6_6.handlers.xml_handler import XmlHandler
from hw_6.hw_6_6.handlers.json_handler import JsonHandler


class XmlToJsonAdapter:
    """
    Adapter to convert data from XML to JSON format.
    """

    def __init__(self, xml_handler: XmlHandler, json_handler: JsonHandler) -> None:
        """
        Initializes the XmlToJsonAdapter.

        Args:
            xml_handler (XmlHandler): An instance of the XmlHandler.
            json_handler (JsonHandler): An instance of the JsonHandler.
        """

        self.xml_handler = xml_handler
        self.json_handler = json_handler

    def convert_xml_to_json(self, xml_file: str, json_file: str) -> None:
        """
        Converts data from an XML file to a JSON file.

        Args:
            xml_file (str): The path to the XML file.
            json_file (str): The path to the JSON file.
        """

        try:
            data = self.xml_handler.read_xml(xml_file)
            self.json_handler.write_json(json_file, data)
        except Exception as e:
            print(f"Error converting XML to JSON: {e}")
