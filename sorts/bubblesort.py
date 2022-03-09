"""Bubble sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""

from time import sleep


def bubble_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with bubble sort algorithm."""
    array_len = len(array)
    for _ in range(array_len - 1):
        swapped = False
        for j in range(array_len - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            visualize(["#C6D57E" if i == j or i == j + 1 else "#A2CDCD" for i in range(array_len)], array)
            sleep(speed)
        if not swapped:
            break
    return array    # return sorted array for unit tests
