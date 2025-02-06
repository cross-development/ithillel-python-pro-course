"""
This module contains unit tests for the WebService class.

- `test_successful_request`: Tests successful data retrieval from the web service.
- `test_error_request`: Tests handling of HTTP errors during data retrieval.
"""

import unittest
from unittest.mock import patch, Mock
import requests

from hw_7.hw_7_2.web_service import WebService


class TestWebService(unittest.TestCase):
    """
    Unit tests for the WebService class.
    """

    def setUp(self) -> None:
        """
        Sets up the test environment by creating a WebService instance.
        """

        self.web_service = WebService()

    @patch('requests.get')
    def test_successful_request(self, mock_get: Mock) -> None:
        """
        Tests successful data retrieval from the web service.

        Args:
            mock_get (Mock): A mock object for the requests.get function.
        """

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = self.web_service.get_data('https://example.com')
        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with('https://example.com')

    @patch('requests.get')
    def test_error_request(self, mock_get: unittest.mock.Mock) -> None:
        """
        Tests handling of HTTP errors during data retrieval.

        Args:
            mock_get (Mock): A mock object for the requests.get function.
        """

        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError()

        mock_get.return_value = mock_response

        with self.assertRaises(requests.HTTPError):
            self.web_service.get_data('https://example.com/not_found')


if __name__ == '__main__':
    unittest.main()
