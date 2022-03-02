from time import sleep

"""Heap sort algorithm.
Complexity: worst:   O(n log n)
            average: O(n log n)
            best:    O(n log n)
"""


def heapify(array: list, n: int, i: int, visualize: callable, speed: float):
    """Heap-sorting given tree or subtree."""
    root = i
    left = 2 * i + 1    # left child index = 2 * i + 1
    right = 2 * i + 2   # right child index = 2 * i + 2
    if left < n and array[i] < array[left]:     # check if left child greater than parent
        root = left
    if right < n and array[root] < array[right]:    # check if right child greater than parent
        root = right
    if root != i:
        visualize(["#C6D57E" if k == i or k == root else "#A2CDCD" for k in range(len(array))], array)
        sleep(speed)
        array[i], array[root] = array[root], array[i]  # root-child swap
        visualize(["#C6D57E" if k == i or k == root else "#A2CDCD" for k in range(len(array))], array)
        sleep(speed)
        heapify(array, n, root, visualize, speed)   # re-heapify subtree if root has changed


def heapsort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with heap sort algorithm."""
    arr_len = len(array)
    for i in range(arr_len // 2 - 1, -1, -1):       # arr_len // 2 - 1 = last parent position
        heapify(array, arr_len, i, visualize, speed)
    for i in range(arr_len - 1, 0, -1):
        visualize(["#D57E7E" if k == i or k == 0 else "#A2CDCD" for k in range(len(array))], array)
        sleep(speed)
        array[i], array[0] = array[0], array[i]  # swap into final(i) position
        visualize(["#D57E7E" if k == i or k == 0 else "#A2CDCD" for k in range(len(array))], array)
        sleep(speed)
        heapify(array, i, 0, visualize, speed)
    return array  # return sorted array for unit tests
