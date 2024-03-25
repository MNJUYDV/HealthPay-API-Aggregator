# test_error_handler.py
import unittest
from app.error_handler import handle_api_errors
from fastapi import HTTPException

class TestErrorHandler(unittest.TestCase):
    
    def test_handle_api_errors_success(self):
        responses_success = [{"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000}]
        self.assertIsNone(handle_api_errors(responses_success))

    def test_handle_api_errors_failure(self):
        responses_empty = []
        with self.assertRaises(HTTPException) as cm:
            handle_api_errors(responses_empty)
        self.assertEqual(cm.exception.status_code, 500)

if __name__ == '__main__':
    unittest.main()
