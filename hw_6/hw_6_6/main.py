"""
This module demonstrates the usage of the adapters defined in the project.

It performs the following data conversions:

1. Converts data from XML_FILE to JSON_FILE using the XmlToJsonAdapter.
2. Converts data from JSON_FILE to CSV_FILE using the JsonToCsvAdapter.
3. Converts data from CSV_FILE back to JSON_FILE using the CsvToJsonAdapter.

This script showcases how the adapters can be used to easily
convert data between different file formats.
"""

from hw_6.hw_6_6.handlers.csv_handler import CsvHandler
from hw_6.hw_6_6.handlers.xml_handler import XmlHandler
from hw_6.hw_6_6.handlers.json_handler import JsonHandler
from hw_6.hw_6_6.adapters.csv_to_json_adapter import CsvToJsonAdapter
from hw_6.hw_6_6.adapters.xml_to_json_adapter import XmlToJsonAdapter
from hw_6.hw_6_6.adapters.json_to_csv_adapter import JsonToCsvAdapter

if __name__ == "__main__":
    CSV_FILE = "data/csv_file.csv"
    XML_FILE = "data/xml_file.xml"
    JSON_FILE = "data/json_file.json"

    csv_handler = CsvHandler()
    xml_handler = XmlHandler()
    json_handler = JsonHandler()

    XmlToJsonAdapter(xml_handler, json_handler).convert_xml_to_json(XML_FILE, JSON_FILE)
    JsonToCsvAdapter(json_handler, csv_handler).convert_json_to_csv(JSON_FILE, CSV_FILE)
    CsvToJsonAdapter(csv_handler, json_handler).convert_csv_to_json(CSV_FILE, JSON_FILE)

    print("All done!")
