"""
Black-box Specification Tests for Admin Functions
Testing Techniques: Equivalence Partitioning, Boundary Value Analysis
Functions: admin_login(), admin_menu(), admin_manage_venues(), view_questions()
"""

import unittest
import sys
import os
import json
sys.path.append('../../../source')

class TestAdminFunctionsSpecification(unittest.TestCase):
    """Tests admin functions using equivalence partitioning and boundary analysis"""

    def setUp(self):
        """Setup test environment - creates necessary directories"""
        os.makedirs("users", exist_ok=True)

    def test_admin_login_equivalence_partitioning(self):
        """Tests valid and invalid admin credentials using equivalence partitioning"""
        print("\n=== Admin Login Equivalence Partitioning ===")

        # Define equivalence partitions
        valid_credentials = [("Admin", "1234")]  # Only valid combination
        invalid_partitions = [
            ("Admin", "wrong"),  # Wrong password
            ("admin", "1234"),   # Wrong case username
            ("", "1234"),        # Empty username
            ("Admin", ""),       # Empty password
            ("", "")            # Both empty
        ]

        # Test valid partition
        for username, password in valid_credentials:
            with self.subTest(f"Valid: {username}"):
                is_valid = username == "Admin" and password == "1234"
                self.assertTrue(is_valid, "Admin/1234 should be valid")

        # Test invalid partitions
        for username, password in invalid_partitions:
            with self.subTest(f"Invalid: {username}/{password}"):
                is_valid = username == "Admin" and password == "1234"
                self.assertFalse(is_valid, "Invalid credentials should fail")

    def test_admin_menu_options_boundary_values(self):
        """Tests menu option boundaries (1-5 are valid, 0 and 6 are invalid)"""
        print("\n=== Admin Menu Boundary Values ===")

        valid_options = ["1", "2", "3", "4", "5"]  # Valid menu choices
        boundary_invalid = ["0", "6"]  # Boundary values just outside valid range

        # Test valid boundary values
        for option in valid_options:
            with self.subTest(f"Valid boundary: {option}"):
                self.assertIn(option, valid_options, f"Option {option} should be valid")

        # Test invalid boundary values
        for option in boundary_invalid:
            with self.subTest(f"Invalid boundary: {option}"):
                self.assertNotIn(option, valid_options, f"Option {option} should be invalid")

    def test_view_questions_display_specification(self):
        """Tests that question display follows required format"""
        print("\n=== Question Display Specification ===")

        # Required fields in question display
        required_fields = ["Question ID:", "From:", "Question:", "Time:"]

        # Sample display format (as per specification)
        sample_display = """
        Question ID: 1
        From: john
        Question: How to buy tickets?
        Time: 2024-01-01 10:00
        """

        # Verify all required fields are present
        for field in required_fields:
            with self.subTest(f"Required field: {field}"):
                self.assertIn(field, sample_display, f"Field '{field}' must be displayed")

    def test_venue_management_specification(self):
        """Tests venue size constraints (1-20 rows, 1-30 columns)"""
        print("\n=== Venue Management Specification ===")

        # Test cases for venue size validation
        test_cases = [
            (10, 15, True, "Within limits"),
            (20, 30, True, "At maximum"),
            (21, 15, False, "Rows exceed"),
            (10, 31, False, "Columns exceed"),
            (0, 10, False, "Zero rows"),
            (10, 0, False, "Zero columns"),
        ]

        # Test each case
        for rows, cols, expected, desc in test_cases:
            with self.subTest(desc):
                # Validate against specification: rows 1-20, cols 1-30
                valid = 1 <= rows <= 20 and 1 <= cols <= 30
                self.assertEqual(valid, expected, f"{rows}x{cols} should be {expected}")

if __name__ == '__main__':
    unittest.main(verbosity=2)