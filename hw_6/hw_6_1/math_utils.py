def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    return 1 if n < 2 else n * factorial(n - 1)


def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """

    return a if b == 0 else gcd(b, a % b)
