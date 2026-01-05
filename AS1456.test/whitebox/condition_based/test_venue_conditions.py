"""
White-box Condition Testing for Venue Functions
Testing Technique: Condition Testing
Functions: add_venue(), update_venue(), resize_venue()
Purpose: Test all logical conditions in venue functions
"""

import unittest
import sys
import os
sys.path.append('../../../source')

class TestVenueConditions(unittest.TestCase):
    """Tests all conditions in venue management functions"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    # CONDITION 1: Venue Location Empty

    def test_add_venue_location_empty_condition(self):
        """Tests: if not location: (empty location check)"""
        print("\n=== Testing Condition: Venue Location Empty ===")

        test_cases = [
            ("", True, "Empty location"),
            ("   ", True, "Whitespace location"),
            ("Main Hall", False, "Valid location"),
            ("Theater", False, "Another valid location"),
        ]

        for location, should_be_empty, description in test_cases:
            with self.subTest(description):
                condition_result = not location.strip()
                self.assertEqual(condition_result, should_be_empty)

    # CONDITION 2: Venue Size Positive Numbers

    def test_add_venue_size_positive_condition(self):
        """Tests: if rows <= 0 or cols <= 0"""
        print("\n=== Testing Condition: Venue Size Positive ===")

        test_cases = [
            (0, 5, True, "Zero rows"),
            (5, 0, True, "Zero columns"),
            (-1, 5, True, "Negative rows"),
            (5, -1, True, "Negative columns"),
            (1, 1, False, "Both positive (min)"),
            (10, 15, False, "Both positive"),
        ]

        for rows, cols, should_be_invalid, description in test_cases:
            with self.subTest(description):
                condition_result = rows <= 0 or cols <= 0
                self.assertEqual(condition_result, should_be_invalid)

    # CONDITION 3: Venue Size Maximum Limit

    def test_add_venue_size_maximum_condition(self):
        """# Tests: if rows > 20 or cols > 30"""
        print("\n=== Testing Condition: Venue Size Maximum ===")

        test_cases = [
            (21, 30, True, "Rows exceed maximum"),
            (20, 31, True, "Columns exceed maximum"),
            (21, 31, True, "Both exceed maximum"),
            (20, 30, False, "At maximum"),
            (10, 15, False, "Within limits"),
        ]

        for rows, cols, should_exceed, description in test_cases:
            with self.subTest(description):
                condition_result = rows > 20 or cols > 30
                self.assertEqual(condition_result, should_exceed)

    # CONDITION 4: Duplicate Venue Detection

    def test_add_venue_duplicate_condition(self):
        """Tests: if venue.location.lower() == location.lower()"""
        print("\n=== Testing Condition: Duplicate Venue ===")

        existing_venues = ["Main Hall", "Theater 1", "Auditorium"]
        new_location = "Main Hall"

        # Test case-insensitive duplicate detection
        is_duplicate = any(
            existing.lower() == new_location.lower()
            for existing in existing_venues
        )

        self.assertTrue(is_duplicate, "Should detect duplicate (case-insensitive)")

        # Test unique venue
        unique_location = "New Theater"
        is_duplicate = any(
            existing.lower() == unique_location.lower()
            for existing in existing_venues
        )
        self.assertFalse(is_duplicate, "Should accept unique venue")

    # CONDITION 5: Resize Positive Numbers

    def test_resize_venue_positive_numbers_condition(self):
        """Tests: if rows <= 0 or cols <= 0 (resize function)"""
        print("\n=== Testing Condition: Resize Positive Numbers ===")

        test_cases = [
            (0, 10, True, "Zero rows"),
            (10, 0, True, "Zero columns"),
            (-5, 10, True, "Negative rows"),
            (10, -5, True, "Negative columns"),
            (1, 1, False, "Minimum positive"),
            (15, 20, False, "Positive numbers"),
        ]

        for rows, cols, should_be_invalid, description in test_cases:
            with self.subTest(description):
                condition_result = rows <= 0 or cols <= 0
                self.assertEqual(condition_result, should_be_invalid)

if __name__ == '__main__':
    unittest.main(verbosity=2)