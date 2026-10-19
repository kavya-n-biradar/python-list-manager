"""Unit tests for src/utils.py. Run with: python -m unittest discover tests"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from utils import add_item, format_list, remove_item, search_items  # noqa: E402


class TestUtils(unittest.TestCase):
    """Tests for the list utility functions."""

    def test_add_item(self):
        items = []
        self.assertTrue(add_item(items, "Buy milk"))
        self.assertEqual(items, ["Buy milk"])

    def test_add_empty_item(self):
        items = []
        self.assertFalse(add_item(items, "   "))
        self.assertEqual(items, [])

    def test_remove_item(self):
        items = ["a", "b", "c"]
        self.assertEqual(remove_item(items, 2), "b")
        self.assertEqual(items, ["a", "c"])

    def test_remove_invalid_position(self):
        items = ["a"]
        self.assertIsNone(remove_item(items, 0))
        self.assertIsNone(remove_item(items, 5))
        self.assertEqual(items, ["a"])

    def test_remove_from_empty_list(self):
        self.assertIsNone(remove_item([], 1))

    def test_search_items(self):
        items = ["Buy milk", "Call mom", "Buy bread"]
        self.assertEqual(search_items(items, "buy"), ["Buy milk", "Buy bread"])

    def test_search_no_match_or_empty_keyword(self):
        items = ["Buy milk"]
        self.assertEqual(search_items(items, "xyz"), [])
        self.assertEqual(search_items(items, ""), [])

    def test_format_list(self):
        self.assertEqual(format_list(["a", "b"]), "1. a\n2. b")

    def test_format_empty_list(self):
        self.assertEqual(format_list([]), "The list is empty.")


if __name__ == "__main__":
    unittest.main()