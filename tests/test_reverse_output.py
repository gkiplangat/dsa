import unittest
from reverse_output import reverse_list  # Import the function to test


class TestReverseList(unittest.TestCase):
    def test_standard_list(self):
        """Test reversing a standard list"""
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_single_element(self):
        """Test reversing a single-element list"""
        self.assertEqual(reverse_list([42]), [42])

    def test_empty_list(self):
        """Test reversing an empty list"""
        self.assertEqual(reverse_list([]), [])

    def test_duplicates(self):
        """Test reversing a list with duplicate elements"""
        self.assertEqual(reverse_list([1, 2, 2, 3]), [3, 2, 2, 1])

    def test_mixed_data_types(self):
        """Test reversing a list with mixed data types"""
        self.assertEqual(reverse_list([1, "two", 3.0, True]), [
                         True, 3.0, "two", 1])

    def test_negative_numbers(self):
        """Test reversing a list with negative numbers"""
        self.assertEqual(reverse_list([-1, -2, -3]), [-3, -2, -1])


if __name__ == "__main__":
    unittest.main()
