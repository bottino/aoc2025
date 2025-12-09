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
    timelines = [0] * len(manifold[0])
    timelines[start_column] = 1
    for row in manifold[1:]:
        timelines = _propagate_timelines(timelines, row)

    return sum(timelines)


def _process_row(beams: set[int], row: list[str], num_splits: int) -> [set[int], int]:
    for i, char in enumerate(row):
        if char == "^":
            if i in beams:
                num_splits += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)
    return beams, num_splits


def _propagate_timelines(beams: list[int], row: list[str]) -> dict[int, int]:
    for i, char in enumerate(row):
        if char == "^":
            num_timelines = beams[i]
            beams[i] = 0
            beams[i + 1] += num_timelines
            beams[i - 1] += num_timelines
    return beams
