from time import sleep

"""Comb sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2 / 2^p) (p is number of increments)
            best:    O(n log n)
"""


# To find next gap from current
def get_next_gap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap


def comb_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with comb sort algorithm."""
    n = len(array)
    # Initialize gap
    gap = n
    # Initialize swapped as true to make sure that loop runs
    swapped = True
    # Keep running while gap is more than 1 and last iteration caused a swap
    while gap != 1 or swapped == 1:
        # Find next gap
        gap = get_next_gap(gap)
        # Initialize swapped as false so that we can check if swap happened or not
        swapped = False
        # Compare all elements with current gap
        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
    return array  # return sorted array for unit tests
