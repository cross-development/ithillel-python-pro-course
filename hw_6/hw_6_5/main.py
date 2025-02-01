import xml.etree.ElementTree as ET
from typing import Optional

FILENAME = "products.xml"


def load_products() -> Optional[ET.Element]:
    """
    Loads product data from an XML file.

    Returns:
        Optional[ET.Element]: The root element of the XML tree if loaded successfully, None otherwise.
    """

    try:
        tree = ET.parse(FILENAME)

        return tree.getroot()
    except FileNotFoundError:
        print('File not found!')

        return None
    except ET.ParseError:
        print('XML parsing error!')

        return None


def list_products() -> None:
    """
    Lists all products with their quantities from the XML file.
    """

    root = load_products()

    if root is None:
        return

    print('Products in the store:')

    for product in root.findall('product'):
        name = product.find('name').text
        quantity = product.find('quantity').text
        print(f'  - {name}: {quantity} pcs.')


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

    for product in root.findall('product'):
        name = product.find('name').text

        if name.lower() == product_name.lower():
            product.find('quantity').text = str(new_quantity)

            tree = ET.ElementTree(root)
            tree.write(FILENAME, encoding='utf-8', xml_declaration=True)

            print(f'Updated the quantity of "{name}" to {new_quantity} pcs.')
            return

    print(f'Product {product_name} not found!')


if __name__ == '__main__':
    list_products()

    product_name = input('Enter the name of the product to update: ')
    new_quantity = int(input('New quantity: '))

    update_product_quantity(product_name, new_quantity)

    list_products()
