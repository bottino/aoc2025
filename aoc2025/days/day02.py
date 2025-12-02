def part_1(input="example"):
    filepath = f"./inputs/day02/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    ranges = []
    for line in lines:
        ranges.extend([l.split("-") for l in line.split(",") if l != ""])

    invalids = 0
    for r in ranges:
        for id in range(int(r[0]), int(r[1]) + 1):
            str_id = str(id)
            if (
                len(str_id) % 2 == 0
                and str_id[: len(str_id) // 2] == str_id[len(str_id) // 2 :]
            ):
                invalids += id

    print(invalids)


def part_2(input="example"):
    filepath = f"./inputs/day02/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    ranges = []
    for line in lines:
        ranges.extend([l.split("-") for l in line.split(",") if l != ""])

    invalids = set()
    for r in ranges:
        for id in range(int(r[0]), int(r[1]) + 1):
            str_id = str(id)
            if _is_invalid_id(str_id):
                invalids.add(id)

    print(sum(invalids))


def _is_invalid_id(id: str) -> bool:
    for n in range(2, len(id) + 1):
        if len(id) % n != 0:
            continue

        m = len(id) // n
        split_id = [id[i : i + m] for i in range(0, len(id), m)]

        # All elements are the same
        if len(set(split_id)) == 1:
            return True
    return False


if __name__ == "__main__":
    part_2("input")
