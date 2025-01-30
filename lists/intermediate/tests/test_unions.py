import unittest
from list017_unions import union_of_lists


class TestUnionOfLists(unittest.TestCase):
    def test_basic_union(self):
        self.assertEqual(union_of_lists([1, 2, 3], [3, 4, 5]), {1, 2, 3, 4, 5})

    def test_one_empty_list(self):
        self.assertEqual(union_of_lists([], [1, 2, 3]), {1, 2, 3})
        self.assertEqual(union_of_lists([1, 2, 3], []), {1, 2, 3})

    def test_both_empty_lists(self):
        self.assertEqual(union_of_lists([], []), set())

    def test_identical_lists(self):
        self.assertEqual(union_of_lists([1, 2, 3], [1, 2, 3]), {1, 2, 3})

    def test_mixed_data_types(self):
        self.assertEqual(union_of_lists(
            [1, "a", 3.5], ["a", 2, 3.5]), {1, "a", 3.5, 2})

    def test_lists_with_duplicates(self):
        self.assertEqual(union_of_lists(
            [1, 1, 2, 3], [3, 3, 4, 4]), {1, 2, 3, 4})


if __name__ == "__main__":
    unittest.main()
