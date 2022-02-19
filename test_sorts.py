#!/usr/bin/env python3

import unittest
from bubblesort import bubble_sort
from quicksort import quicksort
from mergesort import merge_sort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self) -> None:
        self.arr1 = [8, 9, 5, 10, 8, 1, 5, 6, 5, 1]
        self.arr2 = [7, 7, 4, 1, 5, 6, 10, 4, 7, 5]
        self.arr3 = [3, 9, 3, 0, 7, 7, 6, 6, 2, 5]
        self.arr4 = [75, 30, 20, 60, 91, 31, 20, 58, 86, 21, 13, 48, 53, 24, 55, 24, 82, 68, 53, 93]
        self.arr5 = [0]
        self.arr6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.arr7 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.arr8 = [100, 1]
        self.arr9 = [100, 50, 0]
        self.arr10 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        self.arr11 = []

    def test_bubble_sort(self):
        mockup_func = lambda a, b: None
        self.assertEqual(bubble_sort(self.arr1, mockup_func, 0), sorted(self.arr1))
        self.assertEqual(bubble_sort(self.arr2, mockup_func, 0), sorted(self.arr2))
        self.assertEqual(bubble_sort(self.arr3, mockup_func, 0), sorted(self.arr3))
        self.assertEqual(bubble_sort(self.arr4, mockup_func, 0), sorted(self.arr4))
        self.assertEqual(bubble_sort(self.arr5, mockup_func, 0), sorted(self.arr5))
        self.assertEqual(bubble_sort(self.arr6, mockup_func, 0), sorted(self.arr6))
        self.assertEqual(bubble_sort(self.arr7, mockup_func, 0), sorted(self.arr7))
        self.assertEqual(bubble_sort(self.arr8, mockup_func, 0), sorted(self.arr8))
        self.assertEqual(bubble_sort(self.arr9, mockup_func, 0), sorted(self.arr9))
        self.assertEqual(bubble_sort(self.arr10, mockup_func, 0), sorted(self.arr10))
        self.assertEqual(bubble_sort(self.arr11, mockup_func, 0), sorted(self.arr11))

    def test_quicksort(self):
        self.assertEqual(quicksort(self.arr1), sorted(self.arr1))
        self.assertEqual(quicksort(self.arr2), sorted(self.arr2))
        self.assertEqual(quicksort(self.arr3), sorted(self.arr3))
        self.assertEqual(quicksort(self.arr4), sorted(self.arr4))
        self.assertEqual(quicksort(self.arr5), sorted(self.arr5))
        self.assertEqual(quicksort(self.arr6), sorted(self.arr6))
        self.assertEqual(quicksort(self.arr7), sorted(self.arr7))
        self.assertEqual(quicksort(self.arr8), sorted(self.arr8))
        self.assertEqual(quicksort(self.arr9), sorted(self.arr9))
        self.assertEqual(quicksort(self.arr10), sorted(self.arr10))
        self.assertEqual(quicksort(self.arr11), sorted(self.arr11))

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.arr1), sorted(self.arr1))
        self.assertEqual(merge_sort(self.arr2), sorted(self.arr2))
        self.assertEqual(merge_sort(self.arr3), sorted(self.arr3))
        self.assertEqual(merge_sort(self.arr4), sorted(self.arr4))
        self.assertEqual(merge_sort(self.arr5), sorted(self.arr5))
        self.assertEqual(merge_sort(self.arr6), sorted(self.arr6))
        self.assertEqual(merge_sort(self.arr7), sorted(self.arr7))
        self.assertEqual(merge_sort(self.arr8), sorted(self.arr8))
        self.assertEqual(merge_sort(self.arr9), sorted(self.arr9))
        self.assertEqual(merge_sort(self.arr10), sorted(self.arr10))
        self.assertEqual(merge_sort(self.arr11), sorted(self.arr11))


if __name__ == '__main__':
    unittest.main()
