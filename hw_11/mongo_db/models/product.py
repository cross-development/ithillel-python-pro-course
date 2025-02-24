"""
Data models for MongoDB documents.
"""

from bson import ObjectId


class Product:
    """
    Product model for the MongoDB 'products' collection.
    """

    def __init__(self, name: str, price: float, category: str, stock: int, _id=None) -> None:
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            category (str): The category of the product.
            stock (int): The quantity of the product in stock.
            _id (ObjectId, optional): The unique identifier for the product. \
                                      If not provided, a new ObjectId is generated.

        """

        self._id = _id or ObjectId()
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def __str__(self) -> str:
        """
        Return a string representation of the Product instance.

        Returns:
            str: A string representation of the product, including its attributes.
        """

        return (f"Product id: {self._id}, "
                f"name: {self.name}, "
                f"price: {self.price}, "
                f"category: {self.category}, "
                f"stock: {self.stock}")

    def __repr__(self) -> str:
        """
        Return a more concise string representation of the Product instance.

        Returns:
            str: A concise string representation of the product, including its id and name.
        """

        return f"Product id: {self._id}, name: {self.name}"
