"""
Service layer for managing orders.
"""

from typing import List, Dict
from bson import ObjectId

from hw_11.mongo_db.models.order import Order, OrderItem
from hw_11.mongo_db.repositories.order_repository import OrderRepository
from hw_11.mongo_db.repositories.product_repository import ProductRepository


class OrderService:
    """
    Handles business logic for orders.

    This class is responsible for managing orders, including creating new orders,
    updating product stock, and retrieving recent orders.
    """

    def __init__(self) -> None:
        """
        Initializes the OrderService instance.

        Sets up the repositories for orders and products.
        """

        self.order_repo = OrderRepository()
        self.product_repo = ProductRepository()

    def create_order(self, order_number: str, customer: str, items: List[Dict]) -> ObjectId:
        """
        Creates a new order.

        This method deducts product stock based on the order, calculates the total price,
        and creates an order document. The stock is updated after the order is created.

        Args:
            order_number (str): The unique identifier for the order.
            customer (str): The name of the customer placing the order.
            items (List[Dict]): A list of dictionaries, each containing product information
                                 (product_id and quantity) for the order.

        Raises:
            ValueError: If there is not enough stock for a product.

        Returns:
            ObjectId: The unique identifier for the created order.
        """

        order_items = []
        total_price = 0
        product_cache = {}

        for item in items:
            product_id = ObjectId(item["product_id"])

            if product_id not in product_cache:
                product_cache[product_id] = self.product_repo.get_product(product_id)

            product = product_cache[product_id]

            if not product or product["stock"] < item["quantity"]:
                raise ValueError(f"Not enough stock for product {item['product_id']}")

            total_price += product["price"] * item["quantity"]
            order_items.append(OrderItem(product_id, item["quantity"]))

        order = Order(order_number, customer, order_items, total_price)
        order_id = self.order_repo.insert_order(order)

        for item in order_items:
            product = product_cache[item.product_id]
            new_stock = product["stock"] - item.quantity
            self.product_repo.update_stock(item.product_id, new_stock)

        return order_id

    def get_recent_orders(self) -> List[Order]:
        """
        Retrieves all orders from the last 30 days.

        This method queries the order repository to get orders placed within the past 30 days.

        Returns:
            List[Order]: A list of Order instances representing the recent orders.
        """

        return self.order_repo.get_recent_orders()
