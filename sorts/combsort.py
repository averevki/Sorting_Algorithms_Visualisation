"""Comb sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2 / 2^p) (p is number of increments)
            best:    O(n log n)
"""

from time import sleep


def get_next_gap(gap: int) -> int:
    gap = (gap * 10) // 13  # pick new gap with his formula
    return gap if gap >= 1 else 1


def comb_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with comb sort algorithm."""
    arr_len = len(array)
    gap = arr_len     # initialize gap size
    swapped = True
    while gap != 1 or swapped is True:
        gap = get_next_gap(gap)     # pick next gap
        swapped = False
        for i in range(arr_len - gap):  # check every 2 elements within inspected gap
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                visualize(["#D57E7E" if k == i or k == i + gap else "#A2CDCD" for k in range(arr_len)], array)
                sleep(speed)
                swapped = True
            visualize(["#C6D57E" if k == i or k == i + gap else "#A2CDCD" for k in range(arr_len)], array)
            sleep(speed)
    return array  # return sorted array for unit tests
