import unittest
from list02_length import list_length  # Import the function to test


class TestListLength(unittest.TestCase):

    def test_empty_list(self):
        # Test case for an empty list
        self.assertEqual(list_length([]), 0)

    def test_single_element(self):
        # Test case for a list with one element
        self.assertEqual(list_length([10]), 1)

    def test_multiple_elements(self):
        # Test case for a list with multiple elements
        self.assertEqual(list_length([1, 2, 3, 4, 5]), 5)

    def test_strings_in_list(self):
        # Test case for a list with string elements
        self.assertEqual(list_length(["apple", "banana", "cherry"]), 3)

    def test_mixed_data_types(self):
        # Test case for a list with mixed data types
        self.assertEqual(list_length([1, "apple", 3.14, True]), 4)

    def test_large_list(self):
        # Test case for a large list
        large_list = [i for i in range(1000)]
        self.assertEqual(list_length(large_list), 1000)


if __name__ == '__main__':
    unittest.main()

