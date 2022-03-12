"""Quicksort algorithm.
Complexity: worst:   O(n^2)
            average: O(n log n)
            best:    O(n log n)
"""

from time import sleep


def visualize_part(array: list, left: int, high: int, i: int, visualize: callable, speed: float) -> None:
    """Reload columns and visualization colors"""
    colors = []
    for j in range(len(array)):
        if j == left or j == i:
            colors.append("#C6D57E")    # green
        elif j == high:
            colors.append("#D57E7E")    # red
        else:
            colors.append("#A2CDCD")    # blue
    visualize(colors, array)
    sleep(speed)


def partition(array: list, low: int, high: int, visualize: callable, speed: float) -> int:
    """Quicksort partition algorithm"""
    left = low  # boarder
    pivot = array[high]  # pivot
    for i in range(low, high):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
        visualize_part(array, left, high, i, visualize, speed)  # visualization, reload colors
    array[left], array[high] = array[high], array[left]
    return left


def quicksort(array: list, low: int, high: int, visualize: callable, speed: float) -> list:
    """Sort given array with quicksort algorithm"""
    if low < high:
        pindex = partition(array, low, high, visualize, speed)  # get partition index
        quicksort(array, low, pindex - 1, visualize, speed)     # sort left half
        quicksort(array, pindex + 1, high, visualize, speed)    # sort right half
    return array  # return sorted array for unit tests
