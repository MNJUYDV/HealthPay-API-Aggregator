import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api_handler import APIHandlerFactory

class TestAPIHandlerFactory(unittest.TestCase):
    @patch('app.api_handler.APIHandlerFactory.create_api_handler')
    def test_call_apis_success(self, mock_create_api_handler):
        # Define mock responses
        mock_responses = [
            [{"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}],
            [{"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}],
            [],
            []
        ]
        
        mock_api_handler = MagicMock()
        mock_api_handler.call_api.side_effect = mock_responses
        mock_create_api_handler.return_value = mock_api_handler

        API_URLS = ["https://api1.com", "https://api2.com"]
        responses = APIHandlerFactory.call_apis(123)
        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0]["oop_max"], 10000)
        self.assertEqual(responses[1]["copay"], 1500)
        
    @patch('app.api_handler.APIHandlerFactory.create_api_handler')
    def test_call_apis_with_retries(self, mock_create_api_handler):
        mock_responses = [
            [],  # First call fails
            [],  # Second call fails
            [{"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}],  # Third call succeeds
            []
        ]
        
        mock_api_handler = MagicMock()
        mock_api_handler.call_api.side_effect = mock_responses
        mock_create_api_handler.return_value = mock_api_handler

        responses = APIHandlerFactory.call_apis(123, max_retries=3)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["copay"], 1500)

if __name__ == '__main__':
    unittest.main()
