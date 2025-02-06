"""
This module contains unit tests for the BankAccount class.

- `test_initial_balance`: Tests the initial balance of a newly created account.
- `test_deposit`: Tests the `deposit` method with various deposit amounts, including edge cases.
- `test_withdraw`: Tests the `withdraw` method with various withdrawal amounts, including edge cases
- `test_skip_withdraw`: Skips the test if the initial balance is less than 10.
- `test_mock_api_call`: Tests mocking the `get_balance` method for demonstration purposes.
"""

from unittest import mock
import pytest

from hw_7.hw_7_6.bank_account import BankAccount


@pytest.fixture(name="bank_account_fixture")
def _bank_account_fixture() -> BankAccount:
    """
    Creates a BankAccount instance with an initial balance of 100.0.

    Returns:
        BankAccount: A BankAccount instance.
    """

    return BankAccount(100.0)


def test_initial_balance(bank_account_fixture: BankAccount) -> None:
    """
    Tests the initial balance of a newly created account.

    Args:
        bank_account_fixture (BankAccount): A fixture providing a BankAccount instance.
    """

    assert bank_account_fixture.get_balance() == 100.0


@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (50, 150.0),
    (100, 200.0),
    (0, 100.0),
])
def test_deposit(bank_account_fixture: BankAccount, deposit_amount: float, expected_balance: float) -> None:
    """
    Tests the `deposit` method with various deposit amounts, including edge cases.

    Args:
        bank_account_fixture (BankAccount): A fixture providing a BankAccount instance.
        deposit_amount (float): The amount to deposit.
        expected_balance (float): The expected balance after the deposit.
    """

    if deposit_amount == 0:
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            bank_account_fixture.deposit(deposit_amount)
    else:
        bank_account_fixture.deposit(deposit_amount)

        assert bank_account_fixture.get_balance() == expected_balance


@pytest.mark.parametrize("withdraw_amount, expected_balance", [
    (50, 50.0),
    (100, 0.0),
    (150, 100.0),
])
def test_withdraw(bank_account_fixture: BankAccount, withdraw_amount: float, expected_balance: float) -> None:
    """
    Tests the `withdraw` method with various withdrawal amounts, including edge cases.

    Args:
        bank_account_fixture (BankAccount): A fixture providing a BankAccount instance.
        withdraw_amount (float): The amount to withdraw.
        expected_balance (float): The expected balance after the withdrawal.
    """

    if withdraw_amount > bank_account_fixture.get_balance():
        with pytest.raises(ValueError, match="Insufficient funds"):
            bank_account_fixture.withdraw(withdraw_amount)
    else:
        bank_account_fixture.withdraw(withdraw_amount)

        assert bank_account_fixture.get_balance() == expected_balance


@pytest.mark.skip(reason="Skip test in case a balance less than 10")
def test_skip_withdraw(bank_account_fixture: BankAccount) -> None:
    """
    Tests the `withdraw` method with a skip condition.
    This test will be skipped if the initial balance is less than 10.

    Args:
        bank_account_fixture (BankAccount): A fixture providing a BankAccount instance.
    """

    if bank_account_fixture.get_balance() < 10:
        pytest.skip("Insufficient balance for withdrawal test")

    bank_account_fixture.withdraw(10)

    assert bank_account_fixture.get_balance() == 90.0


def test_mock_api_call(bank_account_fixture: BankAccount) -> None:
    """
    Tests mocking the `get_balance` method for demonstration purposes.

    Args:
        bank_account_fixture (BankAccount): A fixture providing a BankAccount instance.
    """

    with mock.patch.object(bank_account_fixture, "get_balance", return_value=500.0):
        assert bank_account_fixture.get_balance() == 500.0


if __name__ == "__main__":
    pytest.main()
