def part_1(input: str) -> int:
    manifold = input.splitlines()[::2]  # half the lines are empty
    start_column = manifold[0].index("S")
    beams = {start_column}
    num_splits = 0
    for row in manifold[1:]:
        for i, char in enumerate(row):
            if char == "^" and i in beams:
                num_splits += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)

    return num_splits


def part_2(input: str) -> int:
    manifold = input.splitlines()[::2]  # half the lines are empty
    start_column = manifold[0].index("S")
    timelines = [0] * len(manifold[0])
    timelines[start_column] = 1
    for row in manifold[1:]:
        for i, char in enumerate(row):
            if char == "^":
                num_timelines = timelines[i]
                timelines[i] = 0
                timelines[i - 1] += num_timelines
                timelines[i + 1] += num_timelines

    return sum(timelines)
