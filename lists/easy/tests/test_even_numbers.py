import unittest
# Import the function from your file
from list013_even_numbers import even_numbers


class TestEvenNumbers(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_only_even_numbers(self):
        self.assertEqual(even_numbers([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_only_odd_numbers(self):
        self.assertEqual(even_numbers([1, 3, 5, 7, 9]), [])

    def test_negative_and_positive_numbers(self):
        self.assertEqual(even_numbers([-4, -2, 0, 2, 4]), [-4, -2, 0, 2, 4])

    def test_duplicates(self):
        self.assertEqual(even_numbers(
            [2, 2, 3, 4, 4, 6, 6]), [2, 2, 4, 4, 6, 6])

    def test_empty_list(self):
        self.assertEqual(even_numbers([]), [])

    def test_single_even_number(self):
        self.assertEqual(even_numbers([8]), [8])

    def test_single_odd_number(self):
        self.assertEqual(even_numbers([7]), [])


if __name__ == '__main__':
    unittest.main()
