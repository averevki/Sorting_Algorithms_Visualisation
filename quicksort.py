from time import sleep
from typing import List, Callable
import logging
from logging import config

"""Quicksort algorithm.
Complexity: worst:   O(n^2)
            average: O(n log n)
            best:    O(n log n)
"""


def visualize_part(array: List, left: int, high: int, i: int, visualize: Callable, time_tick: float) -> None:
    """Reload columns and visualization colors"""
    colors = []
    for j in range(len(array)):
        if j == left or j == i:
            colors.append("#C6D57E")
        elif j == high:
            colors.append("#D57E7E")
        else:
            colors.append("#A2CDCD")
    visualize(colors, array)
    sleep(time_tick)


def partition(array: List, low: int, high: int, visualize: Callable, time_tick: float) -> int:
    """Quicksort partition algorithm"""
    left = low  # boarder
    pivot = array[high]  # pivot
    for i in range(low, high):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
        visualize_part(array, left, high, i, visualize, time_tick)  # visualization, reload colors
    array[left], array[high] = array[high], array[left]
    return left


def quicksort(array: List, low: int, high: int, visualize: Callable, time_tick: float) -> List:
    """Sort given array with quicksort algorithm"""
    if low < high:
        pindex = partition(array, low, high, visualize, time_tick)  # get partition index
        quicksort(array, low, pindex - 1, visualize, time_tick)     # sort left half
        quicksort(array, pindex + 1, high, visualize, time_tick)    # sort right half
    return array  # return sorted array for unit tests
