"""
Service layer for managing products.
"""

from typing import Optional
from bson import ObjectId

from hw_11.mongo_db.models.product import Product
from hw_11.mongo_db.repositories.product_repository import ProductRepository


class ProductService:
    """
    Handles business logic for products.

    This class is responsible for managing products in the store, including adding new products,
    retrieving product details, updating product stock, and removing unavailable products.
    """

    def __init__(self) -> None:
        """
        Initializes the ProductService instance.

        Sets up the repository for interacting with product data.
        """

        self.product_repo = ProductRepository()

    def add_product(self, name: str, price: float, category: str, stock: int) -> ObjectId:
        """
        Adds a new product to the store.

        This method creates a new product and saves it to the database.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            category (str): The category the product belongs to.
            stock (int): The quantity of the product in stock.

        Returns:
            ObjectId: The unique identifier for the newly added product.
        """

        product = Product(name, price, category, stock)

        return self.product_repo.insert_product(product)

    def get_product(self, product_id: str) -> Optional[Product]:
        """
        Retrieves a product by ID.

        This method fetches a product from the repository by its unique identifier.

        Args:
            product_id (str): The unique identifier of the product to be retrieved.

        Returns:
            Optional[Product]: The Product object if found, otherwise None.
        """

        return self.product_repo.get_product(ObjectId(product_id))

    def update_stock(self, product_id: str, quantity: int) -> bool:
        """
        Updates stock quantity for a product.

        This method updates the stock quantity of a specific product.

        Args:
            product_id (str): The unique identifier of the product.
            quantity (int): The new stock quantity to set for the product.

        Returns:
            bool: True if the stock was successfully updated, False otherwise.
        """

        return self.product_repo.update_stock(ObjectId(product_id), quantity)

    def remove_unavailable_products(self) -> int:
        """
        Removes products that are no longer available.

        This method deletes all products from the store that are marked as unavailable.

        Returns:
            int: The number of products that were deleted.
        """

        return self.product_repo.delete_unavailable_products()
