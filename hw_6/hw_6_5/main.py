"""
This module provides functions for managing product data stored in an XML file:

- `load_products()`: Loads product data from the 'products.xml' file.
- `list_products()`: Lists all products with their quantities from the file.
- `update_product_quantity(product_name, new_quantity)`: Updates the quantity of \
                                                         a specific product in the file.

The script demonstrates the usage of these functions by:

1. Listing the initial products.
2. Prompting the user to enter the product name and new quantity.
3. Updating the product quantity in the file.
4. Listing the products again to show the updated information.
"""

import xml.etree.ElementTree as ET
from typing import Optional

FILENAME = "products.xml"


def load_products() -> Optional[ET.Element]:
    """
    Loads product data from an XML file.

    Returns:
        Optional[ET.Element]: The root element of the XML tree if loaded successfully, \
                              None otherwise.
    """

    try:
        tree = ET.parse(FILENAME)

        return tree.getroot()
    except FileNotFoundError:
        print("File not found!")

        return None
    except ET.ParseError:
        print("XML parsing error!")

        return None


def list_products() -> None:
    """
    Lists all products with their quantities from the XML file.
    """

    root = load_products()

    if root is None:
        return

    print("Products in the store:")

    for product in root.findall("product"):
        name = product.find("name").text
        quantity = product.find("quantity").text
        print(f"  - {name}: {quantity} pcs.")


def update_product_quantity(product_name: str, new_quantity: int) -> None:
    """
    Updates the quantity of a product in the XML file.

    Args:
        product_name (str): The name of the product to update.
        new_quantity (int): The new quantity for the product.
    """

    root = load_products()

    if root is None:
        return

    for product in root.findall("product"):
        name = product.find("name").text

        if name.lower() == product_name.lower():
            product.find("quantity").text = str(new_quantity)

            tree = ET.ElementTree(root)
            tree.write(FILENAME, encoding="utf-8", xml_declaration=True)

            print(f"Updated the quantity of '{name}' to {new_quantity} pcs.")
            return

    print(f"Product {product_name} not found!")


if __name__ == "__main__":
    list_products()

    PRODUCT_NAME = input("Enter the name of the product to update: ")
    NEW_QUANTITY = int(input("New quantity: "))

    update_product_quantity(PRODUCT_NAME, NEW_QUANTITY)

    list_products()
