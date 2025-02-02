from hw_6.hw_6_7.adapters.message_sender import MessageSender
from hw_6.hw_6_7.services.sms_service import SmsService


class SmsAdapter(MessageSender):
    """
    Adapter class to send messages via SMS service.
    """

    def __init__(self, sms_service: SmsService, phone_number: str) -> None:
        """
        Initializes the SmsAdapter.

        Args:
            sms_service (SmsService): An SMS service instance.
            phone_number (str): The phone number to send SMS messages to.
        """

        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """
        Sends a message via SMS.

        Args:
            message (str): The message to send.

        Raises:
            Exception: For any errors during sending SMS.
        """

        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Error sending SMS: {e}")
