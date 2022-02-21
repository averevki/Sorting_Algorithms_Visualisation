from time import sleep
from typing import List, Callable

"""Merge sort algorithm.
Complexity: worst:   O(n log n)
            average: O(n log n)
            best:    O(n log n)
"""


def visualize_merge(array: List, left_i: int, mid: int, right_i: int, visualize: Callable, speed: float, green_indexes,
                    red_indexes) -> None:
    """Reload columns and visualization colors"""
    colors = []
    for z in range(len(array)):
        if left_i <= z <= right_i:
            if z in green_indexes:
                colors.append("#C6D57E")    # green
            elif z in red_indexes:
                colors.append("#D57E7E")    # red
            else:
                if left_i <= z <= mid:
                    colors.append("#C6D57E")    # green
                else:
                    colors.append("#D57E7E")    # red
        else:
            colors.append("#A2CDCD")    # blue
    visualize(colors, array)
    sleep(speed)
    red_indexes.clear()
    green_indexes.clear()


def merge_sort(array: List, visualize: Callable, speed: float, left_i, right_i) -> List:
    """Sort given array with merge sort algorithm."""
    if left_i < right_i:
        green_indexes, red_indexes = [], []
        mid = (left_i + right_i) // 2  # Finding pseudo median
        merge_sort(array, visualize, speed, left_i, mid)
        merge_sort(array, visualize, speed, mid + 1, right_i)
        visualize_merge(array, left_i, mid, right_i, visualize, speed, green_indexes, red_indexes)  # visualization

        left_part = array[left_i:mid + 1]
        right_part = array[mid + 1: right_i + 1]
        i = j = 0
        for k in range(left_i, right_i + 1):
            if i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    array[k] = left_part[i]
                    i += 1
                    green_indexes.append(k)
                else:
                    array[k] = right_part[j]
                    j += 1
                    red_indexes.append(k)
            elif i < len(left_part):    # add left elements
                array[k] = left_part[i]
                i += 1
                green_indexes.append(k)
            else:
                array[k] = right_part[j]
                j += 1
                red_indexes.append(k)
        visualize_merge(array, left_i, mid, right_i, visualize, speed, green_indexes, red_indexes)
    return array  # return sorted array for unit tests
