import argparse
from datetime import datetime
import os
from importlib import import_module


def main(day: int, part: int, is_example: bool) -> None:
    input = "example" if is_example else "input"
    day_module = import_module(f"aoc2025.days.day{day:02}")
    if part == 1:
        day_module.part_1(input)
    elif part == 2:
        day_module.part_2(input)
    else:
        day_module.part_1(input)
        day_module.part_2(input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="aoc2025", description="Solutions to Advent of Code 2025"
    )

    current_day = datetime.now().day
    aoc_day = os.getenv("AOC_DAY", current_day)
    aoc_part = os.getenv("AOC_PART", 0)

    parser.add_argument("-d", "--day", type=int, default=aoc_day)
    parser.add_argument("-p", "--part", type=int, default=aoc_part)
    parser.add_argument("-e", "--example", action="store_true")
    args = parser.parse_args()

    main(args.day, args.part, args.example)
