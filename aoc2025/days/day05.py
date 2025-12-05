import sys


def part_1(input="example"):
    ranges, ids = _read_input(input)

    total_fresh = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                total_fresh += 1
                break

    print(total_fresh)


def part_2(input="example"):
    ranges, _ = _read_input(input)

    start_len = sys.maxsize
    while len(ranges) < start_len:
        start_len = len(ranges)
        ranges = _compact_ranges(ranges)

    total_ids = sum([r[1] + 1 - r[0] for r in ranges])
    print(total_ids)


def _compact_ranges(ranges):
    final_ranges = [ranges[0]]
    for r in ranges[1:]:
        is_disjoint_from_all_exising = True
        for i, f in enumerate(final_ranges):
            if not _is_disjoint(r, f):
                final_ranges[i] = (min(r[0], f[0]), max(r[1], f[1]))
                is_disjoint_from_all_exising = False
                break

        if is_disjoint_from_all_exising:
            final_ranges.append(r)

    return final_ranges


def _is_disjoint(a, b) -> bool:
    if b[1] < a[0]:  # disjoint ranges
        return True
    if b[0] > a[1]:  # disjoint ranges
        return True
    return False


def _read_input(input="example"):
    filepath = f"./inputs/day05/{input}.txt"
    with open(filepath, "r") as f:
        text = f.read()

    ranges_str, ids_str = text.split("\n\n")
    ids = [int(i) for i in ids_str.splitlines()]
    ranges = [tuple(map(int, r.split("-"))) for r in ranges_str.splitlines()]
    return ranges, ids
