def part_1(input="example"):
    ranges, ids = _read_input(input)

    total_fresh = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                total_fresh += 1
                break

    print(total_fresh)


def _read_input(input="example"):
    filepath = f"./inputs/day05/{input}.txt"
    with open(filepath, "r") as f:
        text = f.read()

    ranges_str, ids_str = text.split("\n\n")
    ids = [int(i) for i in ids_str.splitlines()]
    ranges = [tuple(map(int, r.split("-"))) for r in ranges_str.splitlines()]
    return ranges, ids


if __name__ == "__main__":
    part_1("input")
