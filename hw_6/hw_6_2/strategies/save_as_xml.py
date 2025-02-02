import xml.etree.ElementTree as ET

from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class SaveAsXml(SaveStrategy):
    """
    Concrete class for saving content as an XML file.
    """

    def save(self, content: str, filename: str) -> None:
        """
        Saves content as an XML file.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        root = ET.Element("root")
        page_content = ET.SubElement(root, "content")
        page_content.text = content

        tree = ET.ElementTree(root)

        with open(filename, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)

        print(f"XML-file has been saved: {filename}")
