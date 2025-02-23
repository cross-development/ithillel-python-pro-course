"""
Service for aggregating sales statistics.
"""

from datetime import datetime
from pymongo.collection import Collection

from hw_11.mongo_db.mongo_client import MongoDBClient


class StatisticsService:
    """
    Provides aggregated sales statistics from the 'orders' collection.

    This service is responsible for calculating various sales statistics,
    such as the total number of products sold and the total amount spent by a customer.
    """

    def __init__(self) -> None:
        """
        Initializes the StatisticsService instance.

        Connects to the 'orders' collection in the MongoDB database.
        """

        db = MongoDBClient().get_database()

        self.collection: Collection = db["orders"]

    def total_products_sold(self, start_date: datetime, end_date: datetime) -> int:
        """
        Calculate the total number of products sold in a given period.

        This method aggregates the total quantity of products sold between the
        specified start and end dates by unwinding the 'items' array in the orders.

        Args:
            start_date (datetime): The start date of the period.
            end_date (datetime): The end date of the period.

        Returns:
            int: The total number of products sold in the given period. Returns 0 if no data is found.
        """

        pipeline = [
            {"$match": {"created_at": {"$gte": start_date, "$lte": end_date}}},
            {"$unwind": "$items"},
            {"$group": {"_id": None, "total_sold": {"$sum": "$items.quantity"}}}
        ]
        result = list(self.collection.aggregate(pipeline))

        return result[0]["total_sold"] if result else 0

    def total_spent_by_customer(self, customer: str) -> float:
        """
        Calculate the total amount spent by a specific customer.

        This method aggregates the total price of all orders placed by the given customer.

        Args:
            customer (str): The name of the customer whose total spending is to be calculated.

        Returns:
            float: The total amount spent by the customer. Returns 0 if no data is found.
        """

        pipeline = [
            {"$match": {"customer": {"$regex": f"^{customer}$", "$options": "i"}}},
            {"$group": {"_id": None, "total_spent": {"$sum": "$total_price"}}}
        ]
        result = list(self.collection.aggregate(pipeline))

        return result[0]["total_spent"] if result else 0
