import numpy as np
from scipy.signal import convolve2d


def part_1(input: str) -> int:
    floor = _read_input(input)

    # Convolve with kernel
    removed = _get_removed_rolls_locations(floor)

    return len(removed)


def part_2(input: str) -> int:
    floor = _read_input(input)

    num_removed = []
    while not num_removed or num_removed[-1] != 0:
        removed_rolls = _get_removed_rolls_locations(floor)
        num_removed.append(len(removed_rolls))
        for i, j in removed_rolls:
            floor[i, j] = 0

    return sum(num_removed)


def _get_removed_rolls_locations(floor: np.array) -> np.array:
    # Get every tile on the floor surrounded by fewer than 4 rolls
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    result = convolve2d(floor, kernel, mode="same") < 4
    # Mask with the floor to only get the ROLLS surrounded by fewer than 4 rolls
    removed_rolls = np.ma.masked_array(result, mask=np.logical_not(floor))
    # Return the removed rolls locations
    return np.argwhere(removed_rolls)


def _read_input(input: str):
    lines = input.splitlines()

    # Create array
    floor = np.zeros([len(lines), len(lines[0])], dtype=int)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "@":
                floor[i, j] = 1

    return floor
