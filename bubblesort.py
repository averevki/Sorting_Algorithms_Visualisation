"""Bubble sort algorithm.
Complexity: worst:   O(n^2)
            average: O(n^2)
            best:    O(n)
"""

from time import sleep
import logging
from logging import config


def bubble_sort(array: list, visualize: callable, speed: float) -> list:
    """Sort given array with bubble sort algorithm."""
    logging.config.fileConfig("logging.conf")  # Use logger config
    logger = logging.getLogger(__name__)  # Create logger

    array_len = len(array)
    logger.info("Bubble sort start...")
    for _ in range(array_len - 1):
        swapped = False
        for j in range(array_len - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                logger.debug("Bubble sort swap.")
            visualize(["#C6D57E" if i == j or i == j + 1 else "#A2CDCD" for i in range(array_len)], array)
            sleep(speed)
        if not swapped:
            break
    logger.debug("Bubble sort end.")
    return array    # return sorted array for unit tests
