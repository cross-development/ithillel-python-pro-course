from math_utils import gcd, factorial
from string_utils import to_upper, trim_whitespace

if __name__ == "__main__":
    factorial_of_five = factorial(5)
    print(f"Factorial of five = {factorial_of_five}")
    assert factorial_of_five == 120, "Factorial of five should be equal to 120."

    gcd_of_four_and_two = gcd(4, 2)
    print(f"GCD of four and two = {gcd_of_four_and_two}")
    assert gcd_of_four_and_two == 2, "GCD of four and two should be 2."

    upper_text = to_upper("some text")
    print(f"Upper text = {upper_text}")
    assert upper_text == "SOME TEXT", "Upper text should be 'SOME TEXT' (upper case)."

    trimmed_text = trim_whitespace("   text   ")
    print(f"Trimmed text = {trimmed_text}")
    assert trimmed_text == "text", "Trimmed text should be 'text' (without whitespace)."
