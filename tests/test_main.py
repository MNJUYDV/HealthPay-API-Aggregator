import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
import sys
import os

# Add the parent directory of 'tests' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.main import app, coalesce_data

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)

    @patch('app.main.APIHandlerFactory.call_apis')
    def test_get_healthcare_info_success(self, mock_call_apis):
        
        mock_call_apis.return_value = [{"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}]

        
        response = self.client.get("/healthcare/123")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["oop_max"], 10000)
        
        
    

    @patch('app.main.APIHandlerFactory.call_apis')
    def test_get_healthcare_info_failure(self, mock_call_apis):
        mock_call_apis.side_effect = Exception("API Error")

        response = self.client.get("/healthcare/123")

        self.assertEqual(response.status_code, 500)
    
    
    def test_coalesce_data(self):
        responses = [
            {"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000},
            {"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}
        ]

        expected_data = {
            "oop_max": 10000,  # Expected mode of 10000 and 15000
            "remaining_oop_max": 9000,  # No unique mode, fallback to None
            "copay": 1000  # No unique mode, fallback to None
        }

        actual_data = coalesce_data(responses)

        self.assertEqual(actual_data["oop_max"], expected_data["oop_max"])
        self.assertEqual(actual_data["remaining_oop_max"], expected_data["remaining_oop_max"])
        self.assertEqual(actual_data["copay"], expected_data["copay"])


    
if __name__ == '__main__':
    unittest.main()
