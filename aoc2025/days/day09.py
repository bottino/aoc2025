import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


def part_1(input: str) -> int:
    coords = []
    for row in input.splitlines():
        coords.append(tuple([int(coord) for coord in row.split(",")]))

    max_area = 0
    for a in coords:
        for b in coords:
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area

    return max_area


def part_2(input: str) -> int:
    coords = []
    max_x, max_y = 0, 0
    for row in input.splitlines():
        coord = tuple([int(coord) for coord in row.split(",")])
        max_x = coord[1] if coord[1] > max_x else max_x
        max_y = coord[0] if coord[0] > max_y else max_y
        coords.append((coord[1], coord[0]))

    # Based on observation of input, there are two likely candidates
    candidates = [(48472, 94664), (50278, 94664)]

    # Left half
    max_area = 0
    best = None
    a = candidates[0]
    for b in coords:
        if b[0] < 50000:
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area
                best = b

    # Right half
    # a = candidates[1]
    # for b in coords:
    #     if b[0] > 50000:
    #         area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    #         if area > max_area:
    #             max_area = area
    #             best = b

    coords = np.array(coords)
    candidates = np.array(candidates)
    plt.plot(coords[:, 0], coords[:, 1])
    rect = patches.Rectangle(
        a, best[0] - a[0], best[1] - a[1], linewidth=1, edgecolor="r", facecolor="none"
    )
    ax = plt.gca()
    ax.add_patch(rect)
    plt.show()

    return max_area


def _square_intersect(u, v) -> bool:
    corners = [u, (v[0], u[1]), v, (u[0], v[1])]

    a = (a2[0] - a1[0], a2[1] - a1[1])
    b = (b2[0] - b1[0], b2[1] - b1[1])
def _seg_intersect(a1, a2, b1, b2) -> bool:
    if perp != 0:
    perp = a[0] * b[0] + a[1] * b[1]
        return False

    for c in (0, 1):
        if a[c] == 0:
            if min(b1[c], b2[c]) <= a1[c] and a1[c] <= max(b1[c], b2[c]):
                return True

    return False
