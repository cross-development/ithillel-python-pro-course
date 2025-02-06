"""
This module contains unit tests for the UserManager class.

- `test_add_user`: Tests the `add_user` method by adding a new user and verifying its presence.
- `test_remove_user`: Tests the `remove_user` method by removing a user and verifying its absence.
- `test_get_all_users`: Tests the `get_all_users` method by verifying \
                        that it returns all users correctly.
- `test_skip_if_few_users`: Tests a condition that should be skipped \
                            if there are fewer than 3 users.
"""

import pytest

from hw_7.hw_7_3.user_manager import UserManager


@pytest.fixture(name="user_manager_fixture")
def _user_manager_fixture() -> UserManager:
    """
    Creates a UserManager instance with two sample users.

    Returns:
        UserManager: A UserManager instance with two sample users.
    """

    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 20)

    return um


def test_add_user(user_manager_fixture: UserManager) -> None:
    """
    Tests the `add_user` method by adding a new user and verifying its presence.

    Args:
        user_manager_fixture (UserManager): A fixture providing a UserManager instance.
    """

    user_manager_fixture.add_user("John", 40)

    assert ("John", 40) in user_manager_fixture.get_all_users()


def test_remove_user(user_manager_fixture: UserManager) -> None:
    """
    Tests the `remove_user` method by removing a user and verifying its absence.

    Args:
        user_manager_fixture (UserManager): A fixture providing a UserManager instance.
    """

    user_manager_fixture.remove_user("Alice")

    assert ("Alice", 30) not in user_manager_fixture.get_all_users()


def test_get_all_users(user_manager_fixture: UserManager) -> None:
    """
    Tests the `get_all_users` method by verifying that it returns all users correctly.

    Args:
        user_manager_fixture (UserManager): A fixture providing a UserManager instance.
    """

    users = user_manager_fixture.get_all_users()

    assert ("Alice", 30) in users
    assert ("Bob", 20) in users


@pytest.mark.skipif(len(UserManager().get_all_users()) < 3, reason="Too few users.")
def test_skip_if_few_users(user_manager_fixture: UserManager) -> None:
    """
    Tests a condition that should be skipped if there are fewer than 3 users.

    Args:
        user_manager_fixture (UserManager): A fixture providing a UserManager instance.
    """

    assert len(user_manager_fixture.get_all_users()) >= 3


if __name__ == "__main__":
    pytest.main()
