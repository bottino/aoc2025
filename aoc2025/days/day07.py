Manifold = list[str]
Split = tuple[int, int]


def part_1(input: str) -> int:
    print(input)
    manifold = input.splitlines()
    start_row = 1
    start_column = manifold[0].index("S")
    splits = set()
    _trickle_down(start_row, start_column, manifold, splits)
    print(len(splits))
    return 0


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
