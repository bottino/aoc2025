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
    pass

