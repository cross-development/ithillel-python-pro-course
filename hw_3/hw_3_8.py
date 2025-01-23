"""
The Price class is well-suited for integration into a PaymentGateway as it ensures accuracy in financial calculations,
encapsulates monetary operations, and enforces data integrity. By rounding values to two decimal places and providing
a clean API for addition, subtraction, and comparison, it simplifies handling key financial components like order totals,
fees, and discounts. Its design also prevents common issues with floating-point arithmetic, making it a reliable
foundation for processing transactions in a consistent and precise manner.
"""


class Price:
    """
    Represents a monetary value with an amount and currency.

    Attributes:
        amount (float): The amount of money.
        currency (str): The currency code (default: 'USD').
    """

    def __init__(self, amount: float, currency: str = 'USD'):
        """
        Initializes a Price object.

        Args:
            amount (float): The amount of money.
            currency (str): The currency code (default: 'USD').

        Raises:
            ValueError: If the amount is less than zero.
        """
        if amount < 0:
            raise ValueError("Price should not be negative.")

        self.amount = round(amount, 2)
        self.currency = currency

    def __str__(self) -> str:
        """
        Returns a string representation of the Price object.

        Returns:
            str: The price in the format "{amount:.2f} {currency}".
        """
        return f"{self.amount:.2f} {self.currency}"

    def __add__(self, other: "Price") -> "Price":
        """
        Adds two Price objects.

        Args:
            other (Price): The other Price object to add.

        Raises:
            ValueError: If the currencies of the two Price objects are different.

        Returns:
            Price: The sum of the two Price objects.
        """
        if self.currency != other.currency:
            raise ValueError("Cannot add prices in different currencies")

        return Price(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Price") -> "Price":
        """
        Subtracts one Price object from another.

        Args:
            other (Price): The Price object to subtract.

        Raises:
            ValueError: If the currencies of the two Price objects are different.

        Returns:
            Price: The difference between the two Price objects.
        """
        if self.currency != other.currency:
            raise ValueError("Cannot subtract prices in different currencies")

        return Price(self.amount - other.amount, self.currency)

    def __eq__(self, other: "Price") -> bool:
        """
        Checks if two Price objects are equal.

        Args:
            other (Price): The other Price object to compare.

        Returns:
            bool: True if both the amount and currency are equal, False otherwise.
        """
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: "Price") -> bool:
        """
        Compares the amounts of two Price objects.

        Args:
            other (Price): The other Price object to compare.

        Raises:
            ValueError: If the currencies of the two Price objects are different.

        Returns:
            bool: True if the amount of this Price is less than the amount of the other Price object, False otherwise.
        """
        if self.currency != other.currency:
            raise ValueError("Cannot compare prices in different currencies")

        return self.amount < other.amount

    def __gt__(self, other: "Price") -> bool:
        """
        Compares the amounts of two Price objects.

        Args:
            other (Price): The other Price object to compare.

        Raises:
            ValueError: If the currencies of the two Price objects are different.

        Returns:
            bool: True if the amount of this Price is greater than the amount of the other Price object, False otherwise.
        """
        if self.currency != other.currency:
            raise ValueError("Cannot compare prices in different currencies")

        return self.amount > other.amount


p1 = Price(100.50)
p2 = Price(50.50)
p3 = Price(20, "EUR")

print(f"p1: {p1}")
assert str(p1) == "100.50 USD", "Price for p1 should be 100.50 USD"
assert p1.amount == 100.50, "Price amount for p1 should be 100.50"
assert p1.currency == "USD", "Price currency for p1 should be USD"

print(f"p2: {p2}")
assert str(p2) == "50.50 USD", "Price for p2 should be 50.50 USD"
assert p2.amount == 50.50, "Price amount for p2 should be 50.50"
assert p2.currency == "USD", "Price currency for p2 should be USD"

print(f"p3: {p3}")
assert str(p3) == "20.00 EUR", "Price for p3 should be 20.00 EUR"
assert p3.amount == 20.00, "Price amount for p3 should be 20.00"
assert p3.currency == "EUR", "Price currency for p3 should be EUR"

print(f"p1 + p2: {p1 + p2}")
assert str(p1 + p2) == "151.00 USD", "Sum of p1 + p2 should be 151.00 USD"

print(f"p1 - p2: {p1 - p2}")
assert str(p1 - p2) == "50.00 USD", "Difference of p1 - p2 should be 50.00 USD"

print(f"p1 > p2: {p1 > p2}")
assert (p1 > p2) == True, "p1 should be greater then p2"

print(f"p1 < p2: {p1 < p2}")
assert (p1 < p2) == False, "p2 should not be greater then p1"

print("All tests passed!")
