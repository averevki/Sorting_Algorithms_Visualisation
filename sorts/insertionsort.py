"""Insertion sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""

from time import sleep


def insertion_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with insertion sort algorithm."""
    arr_len = len(array)
    for i in range(1, arr_len):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]     # push elements by one position, until found key position
            visualize(["#C6D57E" if k == i or k == j + 1 else "#A2CDCD" for k in range(arr_len)], array)
            sleep(speed)
            j -= 1
        array[j + 1] = key  # insert element on his position
        visualize(["#D57E7E" if k == j + 1 else "#A2CDCD" for k in range(arr_len)], array)
        sleep(speed)
    return array  # return sorted array for unit tests
