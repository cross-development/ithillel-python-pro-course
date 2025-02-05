"""
This module defines a Rectangle class that represents a rectangle shape.

The Rectangle class provides methods to:

- Calculate the area of the rectangle.
- Calculate the perimeter of the rectangle.
- Check if the rectangle is a square.
- Resize the rectangle to new dimensions.

The module also includes example usage and unit tests to demonstrate the class functionality.
"""


class Rectangle:
    """
    A class representing a rectangle shape.

    Class Attributes:
        width (float): The width of the rectangle\n
        height (float): The height of the rectangle
    """

    width: float = 0
    height: float = 0

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a new Rectangle instance with given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle

        Returns:
            None
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """
        Check if the rectangle is a square.

        Returns:
            bool: True if the rectangle is a square (width equals height), False otherwise
        """
        return self.width == self.height

    def resize(self, new_width: float, new_height: float) -> None:
        """
        Resize the rectangle with new dimensions.

        Args:
            new_width (float): The new width to set
            new_height (float): The new height to set

        Returns:
            None
        """
        self.width = new_width
        self.height = new_height


rect = Rectangle(4, 6)

print(f"Instance of Rectangle class: {rect}")
assert isinstance(rect, Rectangle) is True, "rect is an instance of Rectangle"

print(f"Area: {rect.area()}")
assert rect.area() == 24, "Area: 24"

print(f"Perimeter: {rect.perimeter()}")
assert rect.perimeter() == 20, "Perimeter: 20"

print(f"Is square: {rect.is_square()}")
assert rect.is_square() is False, "Is square: False"

rect.resize(5, 5)

print(f"New dimensions: width={rect.width}, height={rect.height}")
assert rect.width == 5, "Resized width: 5"
assert rect.height == 5, "Resized height: 5"

print(f"Area (after resizing): {rect.area()}")
assert rect.area() == 25, "Area (after resizing): 25"

print(f"Perimeter (after resizing): {rect.perimeter()}")
assert rect.perimeter() == 20, "Perimeter (after resizing): 20"

print(f"Is square (after resizing): {rect.is_square()}")
assert rect.is_square() is True, "Is square (after resizing): True"
