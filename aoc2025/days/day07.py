def part_1(input: str) -> int:
    manifold = input.splitlines()[::2]  # half the lines are empty
    start_column = manifold[0].index("S")
    beams = {start_column}
    num_splits = 0
    for row in manifold[1:]:
        beams, num_splits = _process_row(beams, row, num_splits)
    return num_splits


def part_2(input: str) -> int:
    manifold = input.splitlines()[::2]  # half the lines are empty
    start_column = manifold[0].index("S")
    beams = {start_column: 1}
    for row in manifold[1:]:
        beams = _process_row_part_2(beams, row)

    num_timelines = 0
    for _, v in beams.items():
        num_timelines += v
    return num_timelines


def _process_row(beams: set[int], row: list[str], num_splits: int) -> [set[int], int]:
    for i, char in enumerate(row):
        if char == "^":
            if i in beams:
                num_splits += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)
    return beams, num_splits


def _process_row_part_2(beams: dict[int, int], row: list[str]) -> dict[int, int]:
    for i, char in enumerate(row):
        if char == "^":
            if i in beams:
                num_timelines = beams.pop(i)
                for neighbor in (i - 1, i + 1):
                    if neighbor in beams:
                        beams[neighbor] += num_timelines
                    else:
                        beams[neighbor] = num_timelines
    return beams
