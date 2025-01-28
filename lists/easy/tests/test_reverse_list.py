import unittest
from list01_reverse_list import reverse_list  # Import the function to test


class TestReverseList(unittest.TestCase):

    def test_standard_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_single_element_list(self):
        # A single element list should remain the same
        self.assertEqual(reverse_list([1]), [1])

    def test_empty_list(self):
        # An empty list should return an empty list
        self.assertEqual(reverse_list([]), [])

    def test_negative_numbers(self):
        self.assertEqual(reverse_list([-1, -2, -3, -4]), [-4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(reverse_list([1, 2, 2, 3, 3, 4]), [
                         4, 3, 3, 2, 2, 1])  # List with duplicates

    def test_mixed_data_types(self):
        self.assertEqual(reverse_list([1, "two", 3.0, True]), [
                         True, 3.0, "two", 1])  # Mixed types

    def test_large_numbers(self):
        self.assertEqual(reverse_list([1000000, 2000000, 3000000]), [
                         3000000, 2000000, 1000000])

    def test_large_list(self):
        large_list = list(range(1000000, 0, -1))  # List from 1 to 1000000
        # Should return a list from 1 to 1000000
        self.assertEqual(reverse_list(large_list), list(range(1, 1000001)))

    def test_strings_in_list(self):
        self.assertEqual(reverse_list(["apple", "banana", "cherry"]), [
                         "cherry", "banana", "apple"])


if __name__ == "__main__":
    unittest.main()
