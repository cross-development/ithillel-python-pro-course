"""
Repository for managing products in MongoDB.
"""

from typing import Optional
from bson import ObjectId
from pymongo import ASCENDING
from pymongo.collection import Collection

from hw_11.mongo_db.models.product import Product
from hw_11.mongo_db.mongo_client import MongoDBClient


class ProductRepository:
    """
    Handles CRUD operations for the 'products' collection in MongoDB.

    This repository provides methods to insert, retrieve, update, and delete products
    from the 'products' collection. It also creates an index on the 'category' field
    for efficient querying.
    """

    def __init__(self) -> None:
        """
        Initializes the ProductRepository instance.

        Connects to the 'products' collection in the MongoDB database and creates
        an ascending index on the 'category' field.
        """

        db = MongoDBClient().get_database()

        self.collection: Collection = db["products"]
        self.collection.create_index([("category", ASCENDING)])

    def insert_product(self, product: Product) -> ObjectId:
        """
        Insert a new product into the database.

        Args:
            product (Product): The product to insert.

        Returns:
            ObjectId: The inserted product's ID.
        """

        result = self.collection.insert_one(vars(product))

        return result.inserted_id

    def get_product(self, product_id: ObjectId) -> Optional[Product]:
        """
        Retrieve a product by its ID.

        Args:
            product_id (ObjectId): The product ID.

        Returns:
            Optional[Product]: The retrieved product or None if not found.
        """

        return self.collection.find_one({"_id": product_id})

    def update_stock(self, product_id: ObjectId, quantity: int) -> bool:
        """
        Update the stock quantity of a product.

        Args:
            product_id (ObjectId): The product ID.
            quantity (int): The new stock quantity.

        Returns:
            bool: True if the update was successful, False otherwise.
        """

        result = self.collection.update_one({"_id": product_id}, {"$set": {"stock": quantity}})

        return result.modified_count > 0

    def delete_unavailable_products(self) -> int:
        """
        Delete products with stock equal to 0.

        This method removes products from the collection where the stock quantity is 0.

        Returns:
            int: The number of deleted products.
        """

        result = self.collection.delete_many({"stock": 0})

        return result.deleted_count
