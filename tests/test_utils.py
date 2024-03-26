import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import coalesce_data

class TestUtils(unittest.TestCase):
    def test_coalesce_data(self):
        responses = [
            {"oop_max": 10000, "remaining_oop_max": 9000, "copay": 1000},
            {"oop_max": 15000, "remaining_oop_max": 8000, "copay": 1500}
        ]

        expected_data = {
            "oop_max": 10000,  
            "remaining_oop_max": 9000, 
            "copay": 1000 
        }

        actual_data = coalesce_data(responses)
        self.assertEqual(actual_data["oop_max"], expected_data["oop_max"])
        self.assertEqual(actual_data["remaining_oop_max"], expected_data["remaining_oop_max"])
        self.assertEqual(actual_data["copay"], expected_data["copay"])

if __name__ == '__main__':
    unittest.main()
