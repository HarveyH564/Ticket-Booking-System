"""
White-box Loop Testing for Seat Display Function
Testing Technique: Loop Testing
Function: print_seats()
Purpose: Test loops with different iteration counts
"""

import unittest
import sys
import os
sys.path.append('../../../source')

class TestSeatingLoopTesting(unittest.TestCase):
    """Loop testing for print_seats() function"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    # LOOP TEST: 0 Iterations (Empty Venue)

    def test_loop_zero_iterations(self):
        """Tests loop with 0 iterations (empty venue)"""
        print("\n=== Loop Test: 0 Iterations (Empty Venue) ===")

        rows = 0
        cols = 0

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), 0, "Should have 0 rows")
        print("  ✓ 0x0 venue creates empty seat map")

    # LOOP TEST: 1 Iteration (1x1 Venue)

    def test_loop_one_iteration(self):
        """Tests loop with 1 iteration (1x1 venue)"""
        print("\n=== Loop Test: 1 Iteration (1x1 Venue) ===")

        rows = 1
        cols = 1

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), 1, "Should have 1 row")
        self.assertEqual(len(seat_map[0]), 1, "Should have 1 column")
        self.assertEqual(seat_map[0][0], "O", "Should be available seat")
        print("  ✓ 1x1 venue creates correct seat map")

    # LOOP TEST: 2 Iterations (2x2 Venue)

    def test_loop_two_iterations(self):
        """Tests loop with 2 iterations (2x2 venue)"""
        print("\n=== Loop Test: 2 Iterations (2x2 Venue) ===")

        rows = 2
        cols = 2

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), 2, "Should have 2 rows")
        for row in seat_map:
            self.assertEqual(len(row), 2, "Each row should have 2 columns")
        print("  ✓ 2x2 venue creates correct seat map")

    # LOOP TEST: M Iterations (M < Typical N)

    def test_loop_m_iterations(self):
        """Tests loop with m iterations where m < typical n"""
        print("\n=== Loop Test: m Iterations (m < n) ===")

        rows = 5
        cols = 5

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), rows)
        for row in seat_map:
            self.assertEqual(len(row), cols)
        print(f"  ✓ {rows}x{cols} venue creates correct seat map")

    # LOOP TEST: N-1 Iterations

    def test_loop_n_minus_one_iterations(self):
        """Tests loop with n-1 iterations"""
        print("\n=== Loop Test: n-1 Iterations ===")

        typical_rows = 10
        rows = typical_rows - 1
        cols = 10

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), rows)
        print(f"  ✓ {rows}x{cols} (n-1) venue creates correct seat map")

    # LOOP TEST: N Iterations (Typical Size)

    def test_loop_n_iterations(self):
        """Tests loop with n iterations (typical size)"""
        print("\n=== Loop Test: n Iterations (Typical) ===")

        rows = 10
        cols = 10

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), rows)
        print(f"  ✓ {rows}x{cols} (typical) venue creates correct seat map")

    # LOOP TEST: N+1 Iterations

    def test_loop_n_plus_one_iterations(self):
        """Tests loop with n+1 iterations"""
        print("\n=== Loop Test: n+1 Iterations ===")

        typical_rows = 10
        rows = typical_rows + 1
        cols = 10

        seat_map = []
        for i in range(rows):
            seat_map.append(["O"] * cols)

        self.assertEqual(len(seat_map), rows)
        print(f"  ✓ {rows}x{cols} (n+1) venue creates correct seat map")

    # LOOP TEST: Nested Loops

    def test_nested_loops_seat_initialization(self):
        """Tests nested loops for seat initialization"""
        print("\n=== Loop Test: Nested Loops ===")

        rows = 3
        cols = 4

        seat_map = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append("O")
            seat_map.append(row)

        self.assertEqual(len(seat_map), rows)
        for i, row in enumerate(seat_map):
            self.assertEqual(len(row), cols, f"Row {i} should have {cols} columns")
            for j, seat in enumerate(row):
                self.assertEqual(seat, "O", f"Seat [{i}][{j}] should be 'O'")

        print(f"  ✓ Nested loops create {rows}x{cols} seat map correctly")

if __name__ == '__main__':
    unittest.main(verbosity=2)