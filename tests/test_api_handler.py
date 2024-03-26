import unittest
from unittest.mock import patch, MagicMock
from app.api_handler import call_api

class TestAPIHandler(unittest.TestCase):
    @patch('app.api_handler.requests.get')
    def test_call_api_success(self, mock_get):
        mock_response_1 = MagicMock()
        mock_response_1.status_code = 200
        mock_response_1.json.return_value = {"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}

        mock_response_2 = MagicMock()
        mock_response_2.status_code = 200
        mock_response_2.json.return_value = {"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}

        mock_get.side_effect = [mock_response_1, mock_response_2]

        responses = call_api(123)

        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0]["oop_max"], 10000)
        self.assertEqual(responses[1]["copay"], 1500)
    
    
    @patch('app.api_handler.requests.get')
    def test_call_api_failure(self, mock_get):
        mock_get.side_effect = Exception("API Error")

        responses = call_api(123)

        self.assertEqual(len(responses), 0)    

if __name__ == '__main__':
    unittest.main()
