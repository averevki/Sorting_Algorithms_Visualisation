from time import sleep

"""Insertion sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""


def insertion_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with insertion sort algorithm."""
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array  # return sorted array for unit tests
