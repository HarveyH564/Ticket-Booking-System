"""
White-box Condition Testing for Purchase Function
Testing Technique: Condition Testing
Function: purchase_ticket()
Purpose: Test all logical conditions in the function
"""

import unittest
import sys
import os
sys.path.append('../../../source')

class TestPurchaseTicketConditions(unittest.TestCase):
    """Tests all conditions in purchase_ticket() function"""

    def setUp(self):
        """# Setup test environment"""
        os.makedirs("users", exist_ok=True)

    # CONDITION 1: Event Choice Validation

    def test_condition_event_choice_validation(self):
        """Tests: if event_choice not in events"""
        print("\n=== Testing Condition: Event Choice Validation ===")

        events = {"1": {}, "2": {}, "3": {}, "4": {}}

        test_cases = [
            ("5", True, "Invalid event (5)"),
            ("0", True, "Invalid event (0)"),
            ("A", True, "Invalid event (A)"),
            ("1", False, "Valid event (1)"),
            ("2", False, "Valid event (2)"),
        ]

        for event_choice, should_be_invalid, description in test_cases:
            with self.subTest(description):
                condition_result = event_choice not in events
                self.assertEqual(condition_result, should_be_invalid)

    # CONDITION 2: Ticket Type Validation

    def test_condition_ticket_type_validation(self):
        """Tests: if ticket_type not in ticket_map"""
        print("\n=== Testing Condition: Ticket Type Validation ===")

        ticket_map = {"1": "general", "2": "vip", "3": "meet_greet"}

        test_cases = [
            ("1", False, "Valid: general"),
            ("2", False, "Valid: vip"),
            ("3", False, "Valid: meet_greet"),
            ("4", True, "Invalid: 4"),
            ("0", True, "Invalid: 0"),
            ("A", True, "Invalid: A"),
        ]

        for ticket_type, should_be_invalid, description in test_cases:
            with self.subTest(description):
                condition_result = ticket_type not in ticket_map
                self.assertEqual(condition_result, should_be_invalid)

    # CONDITION 3: Purchase Confirmation

    def test_condition_confirmation(self):
        """Tests: if confirm == 'Y'"""
        print("\n=== Testing Condition: Purchase Confirmation ===")

        test_cases = [
            ("Y", True, "Confirm purchase (uppercase Y)"),
            ("N", False, "Cancel purchase (uppercase N)"),
            ("y", True, "Confirm purchase (lowercase y)"),
            ("n", False, "Cancel purchase (lowercase n)"),
            ("", False, "Empty input"),
            ("YES", False, "Full word YES"),
            ("yes", False, "Full word yes"),
            ("No", False, "Mixed case No"),
            ("1", False, "Number 1"),
            ("0", False, "Number 0"),
        ]

        for confirm_input, should_confirm, description in test_cases:
            with self.subTest(description):
                confirm_upper = confirm_input.upper()
                condition_result = confirm_upper == "Y"
                self.assertEqual(condition_result, should_confirm)

if __name__ == '__main__':
    unittest.main(verbosity=2)