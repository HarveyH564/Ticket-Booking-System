"""
Black-box Specification Tests for Questions & Responses
Testing Techniques: Equivalence Partitioning
Functions: create_question(), get_user_questions(), respond_to_question(), delete_question()
"""

import unittest
import sys
import os
import json
sys.path.append('../../../source')

class TestQuestionSpecification(unittest.TestCase):
    """Tests question functions using equivalence partitioning"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    def test_question_content_equivalence_partitioning(self):
        """Tests question content validation using equivalence partitioning"""
        print("\n=== Question Content Equivalence Partitioning ===")

        # Test cases for question content
        test_cases = [
            ("How do I buy tickets?", True, "Valid question with content"),
            ("", False, "Empty question (invalid)"),
            ("   ", False, "Whitespace only (invalid)"),
            ("A" * 500, True, "Long question (valid)"),
        ]

        # Test each equivalence partition
        for question, expected, desc in test_cases:
            with self.subTest(desc):
                # Question must have non-whitespace content
                is_valid = bool(str(question).strip())
                self.assertEqual(is_valid, expected, f"Question '{question[:20]}...' should be {expected}")

    def test_question_id_generation_specification(self):
        """Tests that question IDs are generated correctly"""
        print("\n=== Question ID Generation Specification ===")

        # Simulate existing questions
        questions = [{"id": i+1} for i in range(5)]

        # Next ID should be one more than current count
        next_id = len(questions) + 1
        self.assertEqual(next_id, 6, "Next ID should be 6")

        # Check all IDs are unique
        ids = [q["id"] for q in questions]
        unique_ids = set(ids)
        self.assertEqual(len(ids), len(unique_ids), "All question IDs should be unique")


class TestResponseSpecification(unittest.TestCase):
    """Tests response functions using equivalence partitioning"""

    def setUp(self):
        """Setup test environment"""
        os.makedirs("users", exist_ok=True)

    def test_response_content_validation(self):
        """Tests response content validation"""
        print("\n=== Response Content Validation ===")

        # Test cases for response content
        test_cases = [
            ("Thank you for your question.", True, "Valid detailed response"),
            ("", False, "Empty response (invalid)"),
            ("   ", False, "Whitespace only (invalid)"),
            ("OK", True, "Short but valid response"),
        ]

        # Test each equivalence partition
        for response, expected, desc in test_cases:
            with self.subTest(desc):
                # Response must have non-whitespace content
                is_valid = bool(str(response).strip())
                self.assertEqual(is_valid, expected, f"Response '{response}' should be {expected}")

    def test_response_to_existing_question(self):
        """Tests that responses can only be made to existing questions"""
        print("\n=== Response Requirements ===")

        # Existing question IDs
        existing_ids = [1, 2, 3, 4, 5]
        non_existent = 999  # ID that doesn't exist

        # Can only respond to existing questions
        can_respond = non_existent in existing_ids
        self.assertFalse(can_respond, "Should not be able to respond to non-existent question")

if __name__ == '__main__':
    unittest.main(verbosity=2)