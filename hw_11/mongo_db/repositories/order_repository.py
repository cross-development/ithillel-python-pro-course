"""
Repository for managing orders in MongoDB.
"""

from typing import List
from datetime import datetime, timedelta, UTC
from bson import ObjectId
from pymongo.collection import Collection

from hw_11.mongo_db.models.order import Order
from hw_11.mongo_db.mongo_client import MongoDBClient


class OrderRepository:
    """
    Handles CRUD operations for the 'orders' collection in MongoDB.

    This repository provides methods to insert and retrieve orders from the 'orders'
    collection in MongoDB. It also offers functionality to fetch recent orders based
    on a time threshold.
    """

    def __init__(self) -> None:
        """
        Initializes the OrderRepository instance.

        Connects to the 'orders' collection in the MongoDB database.
        """

        db = MongoDBClient().get_database()

        self.collection: Collection = db["orders"]

    def insert_order(self, order: Order) -> ObjectId:
        """
        Insert a new order into the database.

        Args:
            order (Order): The order to insert.

        Returns:
            ObjectId: The inserted order's ID.
        """

        order_dict = vars(order)
        order_dict["items"] = [vars(item) for item in order.items]
        result = self.collection.insert_one(order_dict)

        return result.inserted_id

    def get_recent_orders(self) -> List[Order]:
        """
        Retrieve all orders from the last 30 days.

        This method fetches orders where the 'created_at' field is within the last 30 days.

        Returns:
            List[Order]: List of recent orders created in the past 30 days.
        """

        time_threshold = datetime.now(UTC) - timedelta(days=30)
        orders = self.collection.find({"created_at": {"$gte": time_threshold}})

        return [Order(**order) for order in orders]
