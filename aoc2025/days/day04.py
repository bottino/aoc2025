import numpy as np
from scipy.signal import convolve2d


def part_1(input="example"):
    floor = _read_input(input)

    # Convolve with kernel
    removed = _get_removed_boxes(floor)

    print(len(removed))


def part_2(input="example"):
    floor = _read_input(input)

    removed_boxes = []
    while len(removed_boxes) == 0 or removed_boxes[-1] != 0:
        removed = _get_removed_boxes(floor)
        removed_boxes.append(len(removed))
        for i, j in removed:
            floor[i, j] = 0

    print(sum(removed_boxes))


def _get_removed_boxes(floor: np.array) -> np.array:
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    result = convolve2d(floor, kernel, mode="same") < 4
    result_masked = np.ma.masked_array(result, mask=np.logical_not(floor))
    return np.argwhere(result_masked)


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
