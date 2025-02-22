"""Utils module with different helper functions."""

import uuid


def generate_session_token() -> str:
    """Generate a session token.

    Returns:
        str: The generated session token.
    """

    return str(uuid.uuid4())
