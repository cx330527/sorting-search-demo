import unittest

from main import binary_search, bubble_sort, linear_search


class AlgorithmTests(unittest.TestCase):
    def test_sort_handles_duplicates_and_keeps_input(self):
        numbers = [5, -1, 5, 2]
        self.assertEqual(bubble_sort(numbers), [-1, 2, 5, 5])
        self.assertEqual(numbers, [5, -1, 5, 2])

    def test_search_found_and_missing(self):
        self.assertEqual(linear_search([4, 7, 4], 4), 0)
        self.assertEqual(linear_search([], 4), -1)
        self.assertEqual(binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(binary_search([1, 3, 5, 7], 4), -1)


if __name__ == "__main__":
    unittest.main()
