"""Radix sort algorithm.

Radix sort algorithm can only sort numbers

Complexity: worst:   O(l * n) (l is key length)
"""

from time import sleep


def counting_sort(arr: list, exp1: int, visualize: callable, speed: float) -> None:
    arr_len = len(arr)
    output = [0] * arr_len  # future sorted array
    count = [0] * 10    # count array
    for i in range(arr_len):    # store number of occurrences, of sorted digit, in count array
        index = (arr[i] / exp1)
        visualize(["#C6D57E" if k == i else "#A2CDCD" for k in range(arr_len)], arr)
        sleep(speed)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(arr_len - 1, -1, -1):    # build output array
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
    for i in range(len(arr)):   # copy sorted array to start array
        arr[i] = output[i]
        visualize(["#D57E7E" if k == i else "#A2CDCD" for k in range(arr_len)], arr)
        sleep(speed)


def radix_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with radix sort algorithm."""
    try:
        max1 = max(array)   # find number with most digits
    except ValueError:  # except empty list
        return array
    exp = 1     # digit
    while max1 // exp > 0:
        counting_sort(array, exp, visualize, speed)
        exp *= 10   # switch digit, 1 -> 10, 10 -> 100 etc.
    return array  # return sorted array for unit tests
