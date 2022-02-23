from time import sleep
from typing import List, Callable

"""Shell sort algorithm.
Complexity: worst:   O(n^2)
            average: depends on gap
            best:    O(n log n)
"""


def visualize_shell(array: List, color: str, i: int, j: int, visualize: Callable, speed: float) -> None:
    visualize([color if z == i or z == j else "#A2CDCD" for z in range(len(array))], array)
    sleep(speed)


def shell_sort(array: List, visualize: Callable, speed: float) -> List:
    """Sort given array with ShellSort algorithm."""
    gap = len(array) // 2  # first gap will have half of the array width
    while gap > 0:
        i = 0
        j = gap
        while j < len(array):
            visualize_shell(array, "#C6D57E", i, j, visualize, speed)
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                visualize_shell(array, "#D57E7E", i, j, visualize, speed / 5)
                visualize_shell(array, "#C6D57E", i, j, visualize, speed)
            i += 1
            j += 1

            k = i
            while k - gap > -1:
                visualize_shell(array, "#C6D57E", k, k - gap, visualize, speed * 0.3)
                if array[k - gap] > array[k]:
                    array[k - gap], array[k] = array[k], array[k - gap]
                    visualize_shell(array, "#D57E7E", k, k - gap, visualize, speed / 5)
                    visualize_shell(array, "#C6D57E", k, k - gap, visualize, speed * 0.3)
                k -= 1
        gap //= 2   # pick new gap
    return array  # return sorted array for unit tests
