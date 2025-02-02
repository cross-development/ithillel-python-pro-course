from hw_6.hw_6_6.handlers.csv_handler import CsvHandler
from hw_6.hw_6_6.handlers.xml_handler import XmlHandler
from hw_6.hw_6_6.handlers.json_handler import JsonHandler
from hw_6.hw_6_6.adapters.csv_to_json_adapter import CsvToJsonAdapter
from hw_6.hw_6_6.adapters.xml_to_json_adapter import XmlToJsonAdapter
from hw_6.hw_6_6.adapters.json_to_csv_adapter import JsonToCsvAdapter

if __name__ == "__main__":
    csv_file = "data/csv_file.csv"
    xml_file = "data/xml_file.xml"
    json_file = "data/json_file.json"

    csv_handler = CsvHandler()
    xml_handler = XmlHandler()
    json_handler = JsonHandler()

    XmlToJsonAdapter(xml_handler, json_handler).convert_xml_to_json(xml_file, json_file)
    JsonToCsvAdapter(json_handler, csv_handler).convert_json_to_csv(json_file, csv_file)
    CsvToJsonAdapter(csv_handler, json_handler).convert_csv_to_json(csv_file, json_file)

    print("All done!")
