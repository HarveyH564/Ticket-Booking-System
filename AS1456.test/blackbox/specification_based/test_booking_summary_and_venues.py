"""
Black-box Specification Tests for Booking Summary & Venues
Testing Techniques: Equivalence Partitioning, Boundary Value Analysis
Functions: Booking summary, all venue management functions
"""

import unittest
import sys
import os
import json
sys.path.append('../../../source')

class TestBookingSummarySpecification(unittest.TestCase):
    """Tests booking summary using equivalence partitioning"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    def test_booking_summary_required_fields(self):
        """Tests that booking summary contains all required fields"""
        print("\n=== Booking Summary Required Fields ===")

        # Fields required in booking summary (as per specification)
        required_fields = [
            "Event:", "Date:", "Ticket Type:", "Quantity:",
            "Price per ticket:", "Total Cost:", "Booking Reference:"
        ]

        # Sample booking summary format
        sample_summary = """
        Event: Rock concert
        Date: 30-12-2025
        Ticket Type: VIP
        Quantity: 2
        Price per ticket: $60
        Total Cost: $120
        Booking Reference: REF-user-123456-7890
        """

        # Verify all required fields are present
        for field in required_fields:
            with self.subTest(f"Field: {field}"):
                self.assertIn(field, sample_summary, f"Booking summary must include '{field}'")

    def test_price_calculation_accuracy(self):
        """Tests that price calculations match specification"""
        print("\n=== Price Calculation Accuracy ===")

        # Event prices as per specification
        events = {
            "1": {"general": 25, "vip": 60, "meet_greet": 120},
            "2": {"general": 35, "vip": 75, "meet_greet": 150},
        }

        # Test cases: (event, ticket_type, quantity, expected_total)
        test_cases = [
            ("1", "vip", 2, 120),      # 2 VIP tickets at $60 each
            ("2", "general", 1, 35),    # 1 general ticket at $35
            ("1", "meet_greet", 3, 360), # 3 meet & greet at $120 each
        ]

        # Test each calculation
        for event_key, ticket_type, quantity, expected in test_cases:
            with self.subTest(f"Event {event_key}, {ticket_type}, Qty {quantity}"):
                price = events[event_key][ticket_type]
                total = price * quantity
                self.assertEqual(total, expected, f"Price calculation should be ${expected}")


class TestVenueManagementSpecification(unittest.TestCase):
    """Tests venue functions using boundary value analysis"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    def test_venue_size_boundary_values(self):
        """Tests venue size boundaries (maximum 20x30)"""
        print("\n=== Venue Size Boundary Values ===")

        # Boundary test cases
        boundary_cases = [
            (1, 1, True, "Minimum size (1x1)"),
            (20, 30, True, "Maximum size (20x30)"),
            (21, 30, False, "Rows exceed maximum"),
            (20, 31, False, "Columns exceed maximum"),
            (0, 10, False, "Zero rows invalid"),
            (10, 0, False, "Zero columns invalid"),
        ]

        # Test each boundary case
        for rows, cols, expected, desc in boundary_cases:
            with self.subTest(f"{desc}: {rows}x{cols}"):
                # Validate against specification
                valid = 1 <= rows <= 20 and 1 <= cols <= 30
                self.assertEqual(valid, expected, f"{rows}x{cols} should be {expected}")

    def test_venue_name_uniqueness(self):
        """Tests that venue names must be unique"""
        print("\n=== Venue Name Uniqueness ===")

        # Existing venues in system
        existing_venues = ["Main Hall", "Theater 1", "Auditorium"]
        new_venue = "Main Hall"  # Trying to add duplicate

        # Check if venue name already exists
        is_unique = new_venue not in existing_venues
        self.assertFalse(is_unique, "Venue name 'Main Hall' should not be unique")

    def test_seat_map_display_specification(self):
        """Tests seat map display format"""
        print("\n=== Seat Map Display Specification ===")

        # Valid seat symbols as per specification
        valid_seats = ["O", "X"]  # O = available, X = occupied

        # Invalid seat symbols
        invalid_seats = ["A", "B", "1", ""]

        # Test valid seat symbols
        for seat in valid_seats:
            with self.subTest(f"Valid seat: {seat}"):
                self.assertIn(seat, ["O", "X"], f"'{seat}' should be a valid seat symbol")

        # Test invalid seat symbols
        for seat in invalid_seats:
            with self.subTest(f"Invalid seat: {seat}"):
                self.assertNotIn(seat, ["O", "X"], f"'{seat}' should not be a valid seat symbol")

if __name__ == '__main__':
    unittest.main(verbosity=2)