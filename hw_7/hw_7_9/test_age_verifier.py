"""
This module contains unit tests for the AgeVerifier class.

- `test_is_adult`: Tests the `is_adult` method with various age values using parametrization.
- `test_is_adult_negative_age`: Tests the `is_adult` method with negative age values (skipped).
- `test_is_adult_extreme_age`: Tests the `is_adult` method with an unrealistic age (skipped).
"""

import pytest

from hw_7.hw_7_9.age_verifier import AgeVerifier

UNREALISTIC_AGE = 121
MAX_AGE = 120
NEGATIVE_AGE = -1


@pytest.mark.parametrize("age, expected", [
    (17, False),
    (18, True),
    (25, True),
    (0, False),
    (120, True)
])
def test_is_adult(age: int, expected: bool) -> None:
    """
    Tests the `is_adult` method with various age values.

    Args:
        age (int): The age to be checked.
        expected (bool): The expected return value (True if adult, False otherwise).
    """

    assert AgeVerifier.is_adult(age) == expected


@pytest.mark.skip(reason="Skipping test for negative age values")
def test_is_adult_negative_age() -> None:
    """
    Tests the `is_adult` method with negative age values.

    This test is skipped to avoid testing unrealistic scenarios.
    """

    with pytest.raises(ValueError, match="Age cannot be negative"):
        AgeVerifier.is_adult(NEGATIVE_AGE)


@pytest.mark.skipif(UNREALISTIC_AGE > MAX_AGE, reason="Unrealistic age, skipping the test")
def test_is_adult_extreme_age() -> None:
    """
    Tests the `is_adult` method with an unrealistic age.

    This test is skipped as the condition is always False.
    """

    assert AgeVerifier.is_adult(UNREALISTIC_AGE) is False


if __name__ == '__main__':
    pytest.main()
