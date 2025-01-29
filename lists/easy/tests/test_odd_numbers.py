import unittest
from list014_odd_numbers import odd_numbers  # Import function from your module


class TestOddNumbers(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(odd_numbers([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_only_odd_numbers(self):
        self.assertEqual(odd_numbers([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_only_even_numbers(self):
        self.assertEqual(odd_numbers([2, 4, 6, 8, 10]), [])

    def test_negative_and_positive_numbers(self):
        self.assertEqual(odd_numbers(
            [-5, -3, -1, 0, 1, 3, 5]), [-5, -3, -1, 1, 3, 5])

    def test_duplicates(self):
        self.assertEqual(odd_numbers(
            [1, 1, 2, 3, 3, 4, 5, 5]), [1, 1, 3, 3, 5, 5])

    def test_empty_list(self):
        self.assertEqual(odd_numbers([]), [])

    def test_single_odd_number(self):
        self.assertEqual(odd_numbers([7]), [7])

    def test_single_even_number(self):
        self.assertEqual(odd_numbers([8]), [])


if __name__ == '__main__':
    unittest.main()
