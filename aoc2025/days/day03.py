def part_1(input="example"):
    filepath = f"./inputs/day03/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    total_joltage = 0
    for line in lines:
        first_digit = 0
        second_digit = 0
        for i, c in enumerate(line):
            num = int(c)
            if num > first_digit and i < len(line) - 1:
                first_digit = num
                second_digit = 0
                continue
            if num > second_digit:
                second_digit = num

        joltage = 10 * first_digit + second_digit
        total_joltage += joltage

    print(total_joltage)


def part_2(input="example"):
    filepath = f"./inputs/day03/{input}.txt"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    total_joltage = 0
    num_batteries = 12
    for line in lines:
        digits = [0] * num_batteries
        for i, c in enumerate(line):
            num = int(c)
            for j, n in enumerate(digits):
                if num > n and i < len(line) - (num_batteries - j - 1):
                    digits[j] = num
                    digits[j + 1 :] = [0] * len(digits[j + 1 :])
                    break

        joltage = sum([10**i * n for i, n in enumerate(digits[::-1])])
        total_joltage += joltage

    print(total_joltage)


if __name__ == "__main__":
    part_2("input")
