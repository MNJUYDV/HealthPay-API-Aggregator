import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

    def test_handle_api_errors_incorrect_data_type(self):
        # Test case for incorrect data type in 'oop_max'
        responses_incorrect_type = [{"oop_max": "10000", "remaining_oop_max": 9000, "copay": 1000}]
        with self.assertRaises(HTTPException) as cm:
            handle_api_errors(responses_incorrect_type)
        self.assertEqual(cm.exception.status_code, 500)
        self.assertEqual(cm.exception.detail, "Data type issue: Incorrect data type in API response")


    def test_handle_api_errors_inconsistent_structure(self):
        # Test case for inconsistent JSON structures
        responses_inconsistent_structure = [
            {"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000},  # Response 1
            {"oop_max": 15000, "remaining_oop_max": 9000},  # Response 2 missing 'copay'
            {"oop_max": 20000, "copay": 2000}  # Response 3 missing 'remaining_oop_max'
        ]
        with self.assertRaises(HTTPException) as cm:
            handle_api_errors(responses_inconsistent_structure)
        self.assertEqual(cm.exception.status_code, 500)
        self.assertEqual(cm.exception.detail, "Data coherence issue: Inconsistent JSON structures in API responses")

if __name__ == '__main__':
    unittest.main()
