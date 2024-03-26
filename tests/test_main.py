# test_main.py

import unittest
from unittest.mock import patch
from app.main import app
from fastapi.testclient import TestClient

class TestMain(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)

    @patch('app.main.call_api')
    def test_get_healthcare_info_success(self, mock_call_api):
        mock_call_api.return_value = [{"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}]

        response = self.client.get("/healthcare/123")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["oop_max"], 10000)

    @patch('app.main.call_api')
    def test_get_healthcare_info_failure(self, mock_call_api):
        mock_call_api.side_effect = Exception("API Error")

        response = self.client.get("/healthcare/123")

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
