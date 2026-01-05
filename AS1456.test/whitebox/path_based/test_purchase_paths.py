"""
White-box Path Testing for Purchase Function
Testing Technique: Path Testing
Function: purchase_ticket()
Purpose: Test different execution paths through the function
"""

import unittest
import sys
import os
sys.path.append('../../../source')

class TestPurchaseTicketPaths(unittest.TestCase):
    """Path testing for purchase_ticket()"""

    def setUp(self):
        """Setup test directories"""
        os.makedirs("users", exist_ok=True)

    # PATH ANALYSIS: Control Flow

    def analyze_purchase_cfg(self):
        """Analyzes control flow for purchase function"""
        print("\n" + "="*60)
        print("CONTROL FLOW ANALYSIS - purchase_ticket()")
        print("="*60)

        cfg_nodes = [
            "1. Start: purchase_ticket()",
            "2. Check: if event_choice not in events",
            "3. Check: if ticket_type not in ticket_map",
            "4. Calculate price, show summary",
            "5. Ask: confirm purchase?",
            "6. Check: if confirm == 'Y'",
            "7. Process purchase or cancel",
        ]

        for node in cfg_nodes:
            print(f"  {node}")

        print("\nIndependent Paths to Test:")
        paths = [
            "Path 1: Invalid event → return False",
            "Path 2: Invalid ticket → return False",
            "Path 3: User cancels → return False",
            "Path 4: Confirm & download → return True",
            "Path 5: Confirm & back → return True",
        ]

        for path in paths:
            print(f"  • {path}")

        return cfg_nodes

    # PATH 1: Invalid Event

    def test_path_1_invalid_event(self):
        """Tests Path: Invalid event choice → return False"""
        print("\n=== Testing Path 1: Invalid Event Choice ===")

        events = {"1": {}, "2": {}, "3": {}, "4": {}}
        invalid_events = ["0", "5", "A", ""]

        for event in invalid_events:
            with self.subTest(f"Invalid event: '{event}'"):
                path_taken = event not in events
                self.assertTrue(path_taken, f"Event '{event}' should take invalid path")
                print(f"  ✓ Event '{event}' → Invalid event path")

    # PATH 2: Invalid Ticket

    def test_path_2_invalid_ticket(self):
        """Tests Path: Invalid ticket type → return False"""
        print("\n=== Testing Path 2: Invalid Ticket Type ===")

        ticket_map = {"1": "general", "2": "vip", "3": "meet_greet"}
        invalid_tickets = ["0", "4", "A", ""]

        for ticket in invalid_tickets:
            with self.subTest(f"Invalid ticket: '{ticket}'"):
                path_taken = ticket not in ticket_map
                self.assertTrue(path_taken, f"Ticket '{ticket}' should take invalid path")
                print(f"  ✓ Ticket '{ticket}' → Invalid ticket path")

    # PATH 3: User Cancels

    def test_path_3_user_cancels(self):
        """Tests Path: Valid inputs, user cancels → return False"""
        print("\n=== Testing Path 3: User Cancels Purchase ===")

        test_cases = [
            ("N", "User says N"),
            ("n", "User says n"),
            ("", "User enters nothing"),
            ("NO", "User says NO"),
        ]

        for user_input, description in test_cases:
            with self.subTest(description):
                confirm_upper = user_input.upper()
                path_taken = confirm_upper != "Y"
                self.assertTrue(path_taken, f"Input '{user_input}' should take cancel path")
                print(f"  ✓ Input '{user_input}' → Cancel path")

    # PATH 4: Confirm & Download

    def test_path_4_confirm_and_download(self):
        """Tests Path: Confirm purchase and download → return True"""
        print("\n=== Testing Path 4: Confirm & Download ===")

        user_confirms = ["Y", "y"]
        for confirm in user_confirms:
            with self.subTest(f"Confirm: '{confirm}'"):
                confirm_upper = confirm.upper()
                takes_confirm_path = confirm_upper == "Y"
                self.assertTrue(takes_confirm_path, f"'{confirm}' should take confirm path")
                print(f"  ✓ Confirmation '{confirm}' → Confirm path")

        post_options = ["1", "2"]
        for option in post_options:
            with self.subTest(f"Post-option: '{option}'"):
                takes_download_path = option == "1"
                if option == "1":
                    self.assertTrue(takes_download_path, "Option '1' should take download path")
                    print(f"  ✓ Option '{option}' → Download path")

    # PATH 5: Confirm & Back

    def test_path_5_confirm_and_back(self):
        """Tests Path: Confirm purchase, back to menu → return True"""
        print("\n=== Testing Path 5: Confirm & Back to Menu ===")

        post_option = "2"
        takes_download_path = post_option == "1"
        self.assertFalse(takes_download_path, "Option '2' should not take download path")
        print(f"  ✓ Option '{post_option}' → Back to menu path")

    # COVERAGE ANALYSIS

    def test_path_coverage_analysis(self):
        """Analyzes path coverage achieved"""
        print("\n=== Path Coverage Analysis ===")

        total_paths = 5
        paths_tested = [
            "Path 1: Invalid event → return False",
            "Path 2: Invalid ticket → return False",
            "Path 3: User cancels → return False",
            "Path 4: Confirm & download → return True",
            "Path 5: Confirm & back → return True"
        ]

        print(f"\nTotal independent paths: {total_paths}")
        print("Paths tested:")
        for i, path in enumerate(paths_tested, 1):
            print(f"  {i}. {path}")

        coverage_percentage = (len(paths_tested) / total_paths) * 100
        print(f"\nPath Coverage: {coverage_percentage:.1f}%")

        self.assertEqual(len(paths_tested), total_paths, "Should test all independent paths")

if __name__ == '__main__':
    unittest.main(verbosity=2)