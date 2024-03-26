import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

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
    
if __name__ == '__main__':
    unittest.main()
