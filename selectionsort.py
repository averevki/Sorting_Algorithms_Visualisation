from time import sleep
from typing import List, Callable

"""Selection sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n^2)
"""


def visualize_selection(array: List, i: int, j: int, min_i: int, visualize: Callable, speed: float) -> None:
    """Reload columns and visualization colors"""
    colors = []
    for index in range(len(array)):
        if index == i:
            colors.append("#D57E7E")    # red
        elif index == min_i or index == j:
            colors.append("#C6D57E")    # green
        else:
            colors.append("#A2CDCD")    # blue
    visualize(colors, array)
    sleep(speed)


def selection_sort(array: List, visualize: Callable, speed: float) -> List:
    """Sort given array with selection sort algorithm."""
    arr_len = len(array)
    for i in range(arr_len):
        min_i = i
        visualize(["#D57E7E" if k == i else "#A2CDCD" for k in range(arr_len)], array)
        sleep(speed)
        for j in range(i + 1, arr_len):
            if array[min_i] > array[j]:     # set pointer element as new minimum if it's lesser than current min
                min_i = j
            visualize_selection(array, i, j, min_i, visualize, speed)
        array[i], array[min_i] = array[min_i], array[i]     # swap first element with minimum element
    return array  # return sorted array for unit tests
