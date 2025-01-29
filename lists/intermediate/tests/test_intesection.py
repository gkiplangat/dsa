import unittest
# Import the function from list016_intersection.py
from list016_intersection import list_intersection


class TestListIntersection(unittest.TestCase):

    def test_intersection_common_elements(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [3, 4, 5, 6, 7]
        result = list_intersection(lst1, lst2)
        self.assertEqual(sorted(result), sorted(
            [3, 4, 5]), "Expected intersection: [3, 4, 5]")

    def test_intersection_no_common_elements(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        result = list_intersection(lst1, lst2)
        self.assertEqual(result, [], "Expected intersection: []")

    def test_intersection_empty_lst1(self):
        lst1 = []
        lst2 = [1, 2, 3]
        result = list_intersection(lst1, lst2)
        self.assertEqual(result, [], "Expected intersection: []")

    def test_intersection_empty_lst2(self):
        lst1 = [1, 2, 3]
        lst2 = []
        result = list_intersection(lst1, lst2)
        self.assertEqual(result, [], "Expected intersection: []")

    def test_intersection_both_empty(self):
        lst1 = []
        lst2 = []
        result = list_intersection(lst1, lst2)
        self.assertEqual(result, [], "Expected intersection: []")

    def test_intersection_subset(self):
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3, 4, 5]
        result = list_intersection(lst1, lst2)
        self.assertEqual(sorted(result), sorted(
            [1, 2, 3]), "Expected intersection: [1, 2, 3]")

    def test_intersection_identical_lists(self):
        lst1 = [10, 20, 30]
        lst2 = [10, 20, 30]
        result = list_intersection(lst1, lst2)
        self.assertEqual(sorted(result), sorted(
            [10, 20, 30]), "Expected intersection: [10, 20, 30]")

    def test_intersection_with_duplicates(self):
        lst1 = [1, 2, 2, 3, 4]
        lst2 = [2, 2, 3, 3, 4]
        result = list_intersection(lst1, lst2)
        self.assertEqual(sorted(result), sorted(
            [2, 3, 4]), "Expected intersection: [2, 3, 4]")


# Run the tests
if __name__ == '__main__':
    unittest.main()
