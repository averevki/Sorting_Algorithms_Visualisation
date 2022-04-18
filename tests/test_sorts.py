#!/usr/bin/env python3

"""Unit tests for algorithms implementation"""

import unittest

from ..sorts.bubblesort import bubble_sort
from ..sorts.quicksort import quicksort
from ..sorts.mergesort import merge_sort
from ..sorts.selectionsort import selection_sort
from ..sorts.heapsort import heapsort
from ..sorts.shellsort import shell_sort
from ..sorts.insertionsort import insertion_sort
from ..sorts.radixsort import radix_sort
from ..sorts.combsort import comb_sort
from ..sorts.cocktailsort import cocktail_sort


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
        self.mockup_func = lambda a, b: None

    def test_selection_sort(self) -> None:
        self.assertEqual(selection_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(selection_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(selection_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(selection_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(selection_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(selection_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(selection_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(selection_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(selection_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(selection_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(selection_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_bubble_sort(self) -> None:
        self.assertEqual(bubble_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(bubble_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(bubble_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(bubble_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(bubble_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(bubble_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(bubble_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(bubble_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(bubble_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(bubble_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(bubble_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_quicksort(self) -> None:
        self.assertEqual(quicksort(self.arr1, 0, len(self.arr1) - 1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(quicksort(self.arr2, 0, len(self.arr2) - 1, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(quicksort(self.arr3, 0, len(self.arr3) - 1, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(quicksort(self.arr4, 0, len(self.arr4) - 1, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(quicksort(self.arr5, 0, len(self.arr5) - 1, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(quicksort(self.arr6, 0, len(self.arr6) - 1, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(quicksort(self.arr7, 0, len(self.arr7) - 1, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(quicksort(self.arr8, 0, len(self.arr8) - 1, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(quicksort(self.arr9, 0, len(self.arr9) - 1, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(quicksort(self.arr10, 0, len(self.arr10) - 1, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(quicksort(self.arr11, 0, len(self.arr11) - 1, self.mockup_func, 0), sorted(self.arr11))

    def test_merge_sort(self) -> None:
        self.assertEqual(merge_sort(self.arr1, self.mockup_func, 0, 0, len(self.arr1) - 1), sorted(self.arr1))
        self.assertEqual(merge_sort(self.arr2, self.mockup_func, 0, 0, len(self.arr2) - 1), sorted(self.arr2))
        self.assertEqual(merge_sort(self.arr3, self.mockup_func, 0, 0, len(self.arr3) - 1), sorted(self.arr3))
        self.assertEqual(merge_sort(self.arr4, self.mockup_func, 0, 0, len(self.arr4) - 1), sorted(self.arr4))
        self.assertEqual(merge_sort(self.arr5, self.mockup_func, 0, 0, len(self.arr5) - 1), sorted(self.arr5))
        self.assertEqual(merge_sort(self.arr6, self.mockup_func, 0, 0, len(self.arr6) - 1), sorted(self.arr6))
        self.assertEqual(merge_sort(self.arr7, self.mockup_func, 0, 0, len(self.arr7) - 1), sorted(self.arr7))
        self.assertEqual(merge_sort(self.arr8, self.mockup_func, 0, 0, len(self.arr8) - 1), sorted(self.arr8))
        self.assertEqual(merge_sort(self.arr9, self.mockup_func, 0, 0, len(self.arr9) - 1), sorted(self.arr9))
        self.assertEqual(merge_sort(self.arr10, self.mockup_func, 0, 0, len(self.arr10) - 1), sorted(self.arr10))
        self.assertEqual(merge_sort(self.arr11, self.mockup_func, 0, 0, len(self.arr11) - 1), sorted(self.arr11))

    def test_heap_sort(self) -> None:
        self.assertEqual(heapsort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(heapsort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(heapsort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(heapsort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(heapsort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(heapsort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(heapsort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(heapsort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(heapsort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(heapsort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(heapsort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_shell_sort(self) -> None:
        self.assertEqual(shell_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(shell_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(shell_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(shell_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(shell_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(shell_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(shell_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(shell_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(shell_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(shell_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(shell_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_insertion_sort(self) -> None:
        self.assertEqual(insertion_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(insertion_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(insertion_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(insertion_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(insertion_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(insertion_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(insertion_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(insertion_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(insertion_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(insertion_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(insertion_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_radix_sort(self) -> None:
        self.assertEqual(radix_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(radix_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(radix_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(radix_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(radix_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(radix_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(radix_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(radix_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(radix_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertNotEqual(radix_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))    # only positive numbers
        self.assertEqual(radix_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_comb_sort(self) -> None:
        self.assertEqual(comb_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(comb_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(comb_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(comb_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(comb_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(comb_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(comb_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(comb_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(comb_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(comb_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(comb_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))

    def test_cocktail_sort(self) -> None:
        self.assertEqual(cocktail_sort(self.arr1, self.mockup_func, 0), sorted(self.arr1))
        self.assertEqual(cocktail_sort(self.arr2, self.mockup_func, 0), sorted(self.arr2))
        self.assertEqual(cocktail_sort(self.arr3, self.mockup_func, 0), sorted(self.arr3))
        self.assertEqual(cocktail_sort(self.arr4, self.mockup_func, 0), sorted(self.arr4))
        self.assertEqual(cocktail_sort(self.arr5, self.mockup_func, 0), sorted(self.arr5))
        self.assertEqual(cocktail_sort(self.arr6, self.mockup_func, 0), sorted(self.arr6))
        self.assertEqual(cocktail_sort(self.arr7, self.mockup_func, 0), sorted(self.arr7))
        self.assertEqual(cocktail_sort(self.arr8, self.mockup_func, 0), sorted(self.arr8))
        self.assertEqual(cocktail_sort(self.arr9, self.mockup_func, 0), sorted(self.arr9))
        self.assertEqual(cocktail_sort(self.arr10, self.mockup_func, 0), sorted(self.arr10))
        self.assertEqual(cocktail_sort(self.arr11, self.mockup_func, 0), sorted(self.arr11))


if __name__ == '__main__':
    unittest.main()
