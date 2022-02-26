from time import sleep
from typing import List, Callable

"""Cocktail shaker sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""


def cocktail_sort(array: List, visualize: Callable, speed: float) -> List:
    """Sort given array with cocktail shaker sort algorithm."""
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped is True:
        # reset the swapped flag on entering the loop, because it might be true from a previous iteration.
        swapped = False
        # loop from left to right same as the bubble sort
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # if nothing moved, then array is sorted.
        if swapped is False:
            break
        # otherwise, reset the swapped flag so that it can be used in the next stage
        swapped = False
        # move the end point back by one, because item at the end is in its rightful spot
        end = end - 1
        # from right to left, doing the same comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        # increase the starting point,
        # because the last stage would have moved the next smallest number to its rightful spot.
        start = start + 1
    return array  # return sorted array for unit tests
