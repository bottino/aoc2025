import numpy as np
import matplotlib.pyplot as plt


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

    coords = np.array(coords)

    floor = np.zeros((max_x + 1, max_y + 1), dtype=np.uint8)
    for c in coords:
        floor[c[0], c[1]] = 1

    # plt.plot(coords[:, 0], coords[:, 1])
    # plt.show()

    # fill the rows with green tiles
    for i in range(floor.shape[0]):
        inside = False
        for j in range(floor.shape[1]):
            if floor[i][j] == 1:
                inside = not inside
            else:
                if inside:
                    floor[i][j] = 2

    # fill the columns with green tiles
    for j in range(floor.shape[1]):
        inside = False
        for i in range(floor.shape[0]):
            if floor[i][j] == 1:

            else:
                if inside:
                    floor[i][j] = 2

    SEED = (4, 4) if floor.shape[0] < 10000 else (40000, 40000)
    _flood_fill(SEED, floor)

    plt.imshow(floor)
    plt.show()


    
    if floor[*coord] > 0:
        return
    floor[*coord] = 2
    for dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        _flood_fill((coord[0] + dir[0], coord[1] + dir[1]), floor)
