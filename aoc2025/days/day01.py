def part_1(input="example"):
    filepath = f"./inputs/day01/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    pos = 50
    zeroes = 0
    for l in lines:
        dir = l[0]
        rot = int(l[1:])

        if dir == "L":
            pos = (pos - rot) % 100
        elif dir == "R":
            pos = (pos + rot) % 100
        else:
            raise ValueError(f"Incorrect value {dir}")

        if pos == 0:
            zeroes += 1

    print(zeroes)


def part_2(input="example"):
    filepath = f"./inputs/day01/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    pos = 50
    zeroes = 0

    # We use integer division:
    for l in lines:
        dir = l[0]
        rot = int(l[1:])

        if dir == "L":
            turns = abs((pos - rot) // 100)
            if pos == 0:  # handle edge case when starting at zero and going left
                turns -= 1
            pos = (pos - rot) % 100
            if pos == 0:  # handle edge case when arriving on 0 from left
                turns += 1
        elif dir == "R":
            turns = abs((pos + rot) // 100)
            pos = (pos + rot) % 100
        else:
            raise ValueError(f"Incorrect value {dir}")

        zeroes += turns

        print(f"{l}, {zeroes}, {turns}, {pos}")

    print(zeroes)


if __name__ == "__main__":
    part_2("input")
