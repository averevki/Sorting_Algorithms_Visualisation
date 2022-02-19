from time import sleep
from typing import List, Callable
# TODO reverse order

def bubble_sort(array: List, visualize: Callable, time_tick: float) -> None:
    """Sort given array with bubble sort algorithm. Complexity(worst and average): O(n^2)"""
    array_len = len(array)
    for _ in range(array_len - 1):
        swapped = False
        for j in range(array_len - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            visualize(['green' if i == j or i == j + 1 else 'red' for i in range(array_len)], array)
            sleep(time_tick)
        if not swapped:
            break

    visualize(['green' for _ in range(array_len)], array)
