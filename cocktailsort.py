"""Cocktail shaker sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""

from time import sleep


def visualize_shaker(array: list, pos: int, headed: str, visualize: callable, speed: float) -> None:
    """Redraw visualization"""
    colors: list = []
    left = right = "#C6D57E"    # green
    match headed:
        case "l":
            left = "#D57E7E"    # red
        case "r":
            right = "#D57E7E"   # red
    for k in range(len(array)):
        if k == pos:
            colors.append(left)
        elif k == pos + 1:
            colors.append(right)
        else:
            colors.append("#A2CDCD")    # blue
    visualize(colors, array)
    sleep(speed)


def check_swap(array: list, i: int, swapped: bool, headed: str, visualize: callable, speed: float) -> bool:
    """Sort 2 elements"""
    if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = True
    visualize_shaker(array, i, headed, visualize, speed)    # visualize
    return swapped


def cocktail_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with cocktail shaker sort algorithm."""
    swapped = True
    start = 0
    end = len(array) - 1
    while swapped is True:
        swapped = False
        for i in range(start, end):
            swapped = check_swap(array, i, swapped, "r", visualize, speed)
        if swapped is False:    # check if array is sorted
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            swapped = check_swap(array, i, swapped, "l", visualize, speed)
        start = start + 1
    return array  # return sorted array for unit tests
