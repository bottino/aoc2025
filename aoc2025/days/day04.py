import numpy as np
from scipy.signal import convolve2d


def part_1(input="example"):
    floor = _read_input(input)

    # Convolve with kernel
    removed = _get_removed_rolls_locations(floor)

    print(len(removed))


def part_2(input="example"):
    floor = _read_input(input)

    num_removed = []
    while not num_removed or num_removed[-1] != 0:
        removed_rolls = _get_removed_rolls_locations(floor)
        num_removed.append(len(removed_rolls))
        for i, j in removed_rolls:
            floor[i, j] = 0

    print(sum(num_removed))


def _get_removed_rolls_locations(floor: np.array) -> np.array:
    # Get every tile on the floor surrounded by fewer than 4 rolls
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    result = convolve2d(floor, kernel, mode="same") < 4
    # Mask with the floor to only get the ROLLS surrounded by fewer than 4 rolls
    removed_rolls = np.ma.masked_array(result, mask=np.logical_not(floor))
    # Return the removed rolls locations
    return np.argwhere(removed_rolls)


def _read_input(input="example"):
    filepath = f"./inputs/day04/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    # Create array
    floor = np.zeros([len(lines), len(lines[0])], dtype=int)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "@":
                floor[i, j] = 1

    return floor


if __name__ == "__main__":
    part_2("input")
