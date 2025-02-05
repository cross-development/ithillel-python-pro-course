"""
This module demonstrates the usage of the MessageDispatcher, MessageSender adapters,
and underlying communication services.

It includes two test functions:

- `test_success_case`:
    - Creates and configures adapters with valid credentials.
    - Sends a test message through the MessageDispatcher.
    - Verifies successful message delivery by printing simulated messages.

- `test_failure_case`:
    - Creates and configures adapters with invalid credentials.
    - Sends a test message through the MessageDispatcher.
    - Verifies that errors are raised for adapters with invalid credentials.

This script provides a comprehensive test of the message dispatching system,
including both successful and failure scenarios.
"""

from hw_6.hw_6_7.adapters.sms_adapter import SmsAdapter
from hw_6.hw_6_7.adapters.push_adapter import PushAdapter
from hw_6.hw_6_7.adapters.email_adapter import EmailAdapter
from hw_6.hw_6_7.services.sms_service import SmsService
from hw_6.hw_6_7.services.push_service import PushService
from hw_6.hw_6_7.services.email_service import EmailService
from hw_6.hw_6_7.dispatchers.message_dispatcher import MessageDispatcher


def test_success_case(sms_service: SmsService, push_service: PushService, email_service: EmailService) -> None:
    """
    Tests the MessageDispatcher functionality in a successful scenario.

    This function creates instances of SmsAdapter, EmailAdapter, and PushAdapter
    using the provided services. It then creates a MessageDispatcher instance
    and adds the adapters to it. Finally, it sends a test message using the
    dispatcher and verifies that the messages are sent successfully to all
    adapters (by printing simulated messages).

    Args:
       sms_service (SmsService): An SMS service instance.
       push_service (PushService): A push notification service instance.
       email_service (EmailService): An email service instance.
    """

    sms_adapter = SmsAdapter(sms_service, "+380123456789")
    email_adapter = EmailAdapter(email_service, "user@example.com")
    push_adapter = PushAdapter(push_service, "device123")

    dispatcher = MessageDispatcher()

    dispatcher.add_adapter(sms_adapter)
    dispatcher.add_adapter(email_adapter)
    dispatcher.add_adapter(push_adapter)

    dispatcher.send_message_to_all("Hello! This is a test message")


def test_failure_case(sms_service: SmsService, push_service: PushService, email_service: EmailService) -> None:
    """
    Tests the MessageDispatcher functionality in a failure scenario.

    This function creates a MessageDispatcher instance and adds adapters with
    invalid credentials (phone number, email address, and device ID) to it.
    It then sends a message using the dispatcher and verifies that errors are
    raised for the invalid adapters (by printing simulated errors).

    Args:
        sms_service (SmsService): An SMS service instance (not used).
        push_service (PushService): A push notification service instance (not used).
        email_service (EmailService): An email service instance (not used).
    """

    sms_adapter = SmsAdapter(sms_service, "invalid_phone")
    email_adapter = EmailAdapter(email_service, "invalid_email")
    push_adapter = PushAdapter(push_service, "invalid_device")

    dispatcher = MessageDispatcher()

    dispatcher.add_adapter(sms_adapter)
    dispatcher.add_adapter(email_adapter)
    dispatcher.add_adapter(push_adapter)

    dispatcher.send_message_to_all("This message is broken")


if __name__ == "__main__":
    sms_service = SmsService()
    email_service = EmailService()
    push_service = PushService()

    # Test with success
    test_success_case(sms_service, push_service, email_service)

    print("*" * 20)

    # Testing with failure
    test_failure_case(sms_service, push_service, email_service)

    print("*" * 20)
    print("All done!")
