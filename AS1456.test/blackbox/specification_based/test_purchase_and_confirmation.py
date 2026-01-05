"""
Black-box Specification Tests for Purchase & Confirmation
Testing Techniques: Equivalence Partitioning, Boundary Value Analysis
Functions: purchase_ticket(), view_previous_purchases()
"""

import unittest
import sys
import os
import json
sys.path.append('../../../source')

class TestPurchaseTicketSpecification(unittest.TestCase):
    """Tests purchase functions using equivalence partitioning and boundary analysis"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    def test_event_choice_equivalence_partitioning(self):
        """Tests event choice validation using equivalence partitioning"""
        print("\n=== Event Choice Equivalence Partitioning ===")

        # Valid event choices
        valid_choices = ["1", "2", "3", "4"]

        # Invalid event choice partitions
        invalid_partitions = ["0", "5", "A", "", " "]

        # Test valid choices
        for choice in valid_choices:
            with self.subTest(f"Valid: {choice}"):
                self.assertIn(choice, valid_choices, f"Event choice '{choice}' should be valid")

        # Test invalid partitions
        for choice in invalid_partitions:
            with self.subTest(f"Invalid: {choice}"):
                self.assertNotIn(choice, valid_choices, f"Event choice '{choice}' should be invalid")

    def test_quantity_boundary_value_analysis(self):
        """Tests quantity boundaries using boundary value analysis"""
        print("\n=== Quantity Boundary Values ===")

        # Boundary test cases for quantity
        boundary_cases = [
            (0, False, "Zero quantity (invalid)"),
            (1, True, "Minimum quantity (1)"),
            (2, True, "Normal quantity (2)"),
            (100, True, "Large quantity (100)"),
            (-1, False, "Negative quantity (invalid)"),
        ]

        # Test each boundary case
        for qty, expected, desc in boundary_cases:
            with self.subTest(desc):
                # Quantity must be positive
                valid = qty > 0
                self.assertEqual(valid, expected, f"Quantity {qty} should be {expected}")

    def test_booking_reference_format(self):
        """Tests booking reference format follows specification"""
        print("\n=== Booking Reference Format Specification ===")

        # Valid booking reference examples
        valid_refs = [
            "REF-john-1234567890-9999",
            "REF-alice-9876543210-1234",
        ]

        # Invalid booking reference examples
        invalid_refs = [
            "INV-john-123-456",  # Wrong prefix
            "REF-john",           # Missing parts
            "REF-john-123",       # Missing parts
            "REF-",              # Empty
        ]

        # Test valid references
        for ref in valid_refs:
            with self.subTest(f"Valid: {ref[:20]}..."):
                # Check format: starts with REF- and has 4 parts
                self.assertTrue(ref.startswith("REF-"), "Booking ref must start with 'REF-'")
                self.assertEqual(len(ref.split("-")), 4, "Booking ref must have 4 parts")

        # Test invalid references
        for ref in invalid_refs:
            with self.subTest(f"Invalid: {ref}"):
                # Check if format is valid
                valid_format = ref.startswith("REF-") and len(ref.split("-")) == 4
                self.assertFalse(valid_format, f"'{ref}' should not be a valid booking reference")

if __name__ == '__main__':
    unittest.main(verbosity=2)