import xml.etree.ElementTree as ET
from typing import List, Dict


class XmlHandler:
    """
    Class for reading and writing XML files.
    """

    def read_xml(self, file_path: str) -> List[Dict]:
        """
        Reads data from an XML file.

        Args:
            file_path (str): The path to the XML file.

        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents an XML element.

        Raises:
            FileNotFoundError: If the file does not exist.
            ET.ParseError: If the XML data is invalid.
            Exception: For any other errors during reading.
        """

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            return [{child.tag: child.text for child in item} for item in root]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")
        except ET.ParseError:
            raise ET.ParseError(f"Invalid XML format in file {file_path}.")
        except Exception as e:
            raise Exception(f"Error reading XML file: {e}")

    def write_xml(self, file_path: str, data: List[Dict]) -> None:
        """
        Writes data to an XML file.

        Args:
            file_path (str): The path to the XML file.
            data (List[Dict]): A list of dictionaries to be written to the XML file.

        Raises:
            Exception: For any other errors during writing.
        """

        try:
            root = ET.Element("data")

            for item in data:
                element = ET.SubElement(root, "item")

                for key, value in item.items():
                    child = ET.SubElement(element, key)
                    child.text = value

            tree = ET.ElementTree(root)
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
        except Exception as e:
            raise Exception(f"Error writing to XML file: {e}")
