def part_1(input: str) -> int:
    ranges, ids = _read_input(input)

    total_fresh = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                total_fresh += 1
                break

    return total_fresh


def part_2(input: str) -> int:
    ranges, _ = _read_input(input)

    tagged = []
    for r in ranges:
        tagged.append((r[0], "begin"))
        tagged.append((r[1], "end"))

    # It's important that beginnings get sorted _before_ ends that have the same edge
    # It's handled here naturally because 'begin' < 'end' in alphabetical order
    tagged = sorted(tagged)

    compacted_ranges = []
    current_range_start = 0
    num_open_ranges = 0
    for edge in tagged:
        if edge[1] == "begin":
            if num_open_ranges == 0:
                current_range_start = edge[0]
            num_open_ranges += 1
        else:
            num_open_ranges -= 1
            if num_open_ranges == 0:
                compacted_ranges.append((current_range_start, edge[0]))

    total_ids = sum([r[1] + 1 - r[0] for r in compacted_ranges])
    return total_ids


def _read_input(input: str):
    ranges_str, ids_str = input.split("\n\n")
    ids = [int(i) for i in ids_str.splitlines()]
    ranges = [tuple(map(int, r.split("-"))) for r in ranges_str.splitlines()]
    return ranges, ids
