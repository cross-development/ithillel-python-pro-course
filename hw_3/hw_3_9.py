"""
For this task, the @property approach is the most convenient. It provides a clean and intuitive way to work with
attributes while requiring minimal additional code. Descriptors are better suited for more complex scenarios where
reusable or specialized behavior is needed across multiple classes.
"""


class ProductWithGetSet:
    """
    Represents a product with a name and price using traditional getter and setter methods.

    * Advantages: Simple and easy to understand, suitable for small projects.
    * Disadvantages: Verbose code; requires explicit calls to get_price and set_price, making the syntax less convenient.

    Attributes:
        name (str): The name of the product.
        _price (float): The internal price attribute (private).
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initializes a ProductWithGetSet object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        self.name = name
        self.set_price(price)

    def get_price(self) -> float:
        """
        Gets the price of the product.

        Returns:
            float: The price of the product.
        """
        return self._price

    def set_price(self, value: float) -> None:
        """
        Sets the price of the product.

        Args:
            value (float): The new price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value


class ProductWithProperty:
    """
    Represents a product with a name and price using a property with a setter.

    * Advantages: Cleaner code, more intuitive syntax for accessing attributes. Validation is handled automatically.
    * Disadvantages: Limited to simpler use cases; not ideal for reusable logic across multiple classes.

    Attributes:
        name (str): The name of the product.
        _price (float): The internal price attribute (private).
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Initializes a ProductWithProperty object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """
        Gets the price of the product.

        Returns:
            float: The price of the product.
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Sets the price of the product.

        Args:
            value (float): The new price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value


class PriceDescriptor:
    """
    A descriptor class for managing the price attribute of a product.

    Raises:
        ValueError: If the price is negative.
    """

    def __get__(self, instance: "ProductWithDescriptor", owner: type) -> float:
        """
        Gets the price of the product.

        Args:
            instance (ProductWithDescriptor): The product instance.
            owner (type): The class that owns the descriptor.

        Returns:
            float: The price of the product.
        """
        return instance._price

    def __set__(self, instance: "ProductWithDescriptor", value: float) -> None:
        """
        Sets the price of the product.

        Args:
            instance (ProductWithDescriptor): The product instance.
            value (float): The new price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("Price cannot be negative")

        instance._price = value


class ProductWithDescriptor:
    """
    Represents a product with a name and price using a descriptor class.

    * Advantages: Flexible and powerful. Reusable logic that can be shared across multiple classes.
    * Disadvantages: More complex to understand and implement, especially for beginners.

    Attributes:
        name (str): The name of the product.
        price: A PriceDescriptor instance for managing the price.
    """

    price = PriceDescriptor()

    def __init__(self, name: str, price: float) -> None:
        """
        Initializes a ProductWithDescriptor object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        self.name = name
        self.price = price


# Testing ProductWithGetSet
product1 = ProductWithGetSet("Book", 20.0)
assert product1.get_price() == 20.0, "Initial price should be 20.0"

product1.set_price(30.0)
assert product1.get_price() == 30.0, "Updated price should be 30.0"

print("ProductWithGetSet passed all tests")

# product1.set_price(-10.0)  # Should raise ValueError


# Testing ProductWithProperty
product2 = ProductWithProperty("Pen", 15.0)
assert product2.price == 15.0, "Initial price should be 15.0"

product2.price = 25.0
assert product2.price == 25.0, "Updated price should be 25.0"

print("ProductWithProperty passed all tests")

# product2.price = -5.0  # Should raise ValueError


# Testing ProductWithDescriptor
product3 = ProductWithDescriptor("Laptop", 1000.0)
assert product3.price == 1000.0, "Initial price should be 1000.0"

product3.price = 1200.0
assert product3.price == 1200.0, "Updated price should be 1200.0"

print("ProductWithDescriptor passed all tests")

# product3.price = -500.0  # Should raise ValueError

print("All tests passed!")
