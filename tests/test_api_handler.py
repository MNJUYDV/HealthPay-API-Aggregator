import unittest
from unittest.mock import patch, MagicMock
from app.api_handler import call_api

class TestAPIHandler(unittest.TestCase):
    @patch('app.api_handler.requests.get')
    def test_call_api_success(self, mock_get):
        # Define mock responses
        mock_response_1 = MagicMock()
        mock_response_1.status_code = 200
        mock_response_1.json.return_value = {"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}

        mock_response_2 = MagicMock()
        mock_response_2.status_code = 200
        mock_response_2.json.return_value = {"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}

        # Set side effect for the mock requests.get function
        mock_get.side_effect = [mock_response_1, mock_response_2]

        # Call the function under test
        responses = call_api(123)

        # Assertions
        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0]["oop_max"], 10000)
        self.assertEqual(responses[1]["copay"], 1500)

if __name__ == '__main__':
    unittest.main()
