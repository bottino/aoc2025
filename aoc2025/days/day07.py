Manifold = list[str]
Split = tuple[int, int]
BeamRow = set[int]


def part_1(input: str) -> int:
    print(input)
    manifold = input.splitlines()
    start_column = manifold[0].index("S")
    beams = {start_column}
    num_splits = 0
    for row in manifold[1:]:
        beams, num_splits = _process_row(beams, row, num_splits)
    return num_splits


def _process_row(beams, row, num_splits):
    for i, char in enumerate(row):
        if char == "^":
            if i in beams:
                num_splits += 1
                beams.remove(i)
                beams.add(i - 1)
                beams.add(i + 1)
    return beams, num_splits


def _trickle_down(
    row: int, column: int, manifold: Manifold, splits: set[Split]
) -> None:
    if row >= len(manifold) - 1:
        return

    # Go down
    row += 1
    if manifold[row][column] == "^":
        # Keep count of splits
        splits.add((row, column))
        _trickle_down(row, column - 1, manifold, splits)
        _trickle_down(row, column + 1, manifold, splits)
    else:
        _trickle_down(row, column, manifold, splits)
