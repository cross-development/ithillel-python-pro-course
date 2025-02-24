"""
Data models for MongoDB documents.
"""

from typing import List
from datetime import datetime, UTC
from bson import ObjectId


class OrderItem:
    """
    Order item model representing a product in an order.
    """

    def __init__(self, product_id: ObjectId, quantity: int) -> None:
        """
        Initialize an OrderItem instance.

        Args:
            product_id (ObjectId): The unique identifier for the product being ordered.
            quantity (int): The quantity of the product in the order.
        """

        self.product_id = product_id
        self.quantity = quantity


class Order:
    """
    Order model for the MongoDB 'orders' collection.
    """

    def __init__(self, order_number: str, customer: str, items: List[OrderItem],
                 total_price: float, created_at=None, _id=None) -> None:
        """
        Initialize an Order instance.

        Args:
            order_number (str): The order number.
            customer (str): The name of the customer who placed the order.
            items (List[OrderItem]): A list of OrderItem representing the products in the order.
            total_price (float): The total price of the order.
            created_at (datetime, optional): The date and time the order was created. \
                                             If not provided, the current time is used.
            _id (ObjectId, optional): The unique identifier for the order. \
                                      If not provided, a new ObjectId is generated.
        """

        self._id = _id or ObjectId()
        self.order_number = order_number
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.created_at = created_at or datetime.now(UTC)

    def __str__(self) -> str:
        """
        Return a string representation of the Order instance.

        Returns:
           str: A string representation of the order, including its attributes.
        """

        return (f"Order id: {self._id}, "
                f"order number: {self.order_number}, "
                f"customer: {self.customer}, "
                f"total price: {self.total_price}, "
                f"created at: {self.created_at.strftime('%Y-%m-%d %H:%M')}")

    def __repr__(self) -> str:
        """
        Return a more concise string representation of the Order instance.

        Returns:
            str: A concise string representation of the order, including its id and order number.
        """

        return f"Order id: {self._id}, order number: {self.order_number}"
