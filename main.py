import argparse
import os
from datetime import datetime
from importlib import import_module
from typing import Optional


def main(day: Optional[int], part: Optional[int], is_example: bool) -> None:
    day_module = import_module(f"aoc2025.days.day{day:02}")
    input = _read_input(day, is_example)
    example_str = " (example)" if is_example else ""
    if part == 1 or part is None:
        sol = day_module.part_1(input)
        print(f"Day {day:02} - Part 1{example_str}: {sol}")
    if part == 2 or part is None:
        sol = day_module.part_2(input)
        print(f"Day {day:02} - Part 2{example_str}: {sol}")


def _read_input(day: int, is_example: bool) -> str:
    filename = "example" if is_example else "input"
    filepath = f"./inputs/day{day:02}/{filename}.txt"
    with open(filepath, "r") as f:
        input = f.read()
    return input


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="aoc2025", description="Solutions to Advent of Code 2025"
    )

    current_day = datetime.now().day
    aoc_day = os.getenv("AOC_DAY", current_day)
    aoc_part = os.getenv("AOC_PART", None)

    parser.add_argument("-d", "--day", type=int, default=aoc_day)
    parser.add_argument("-p", "--part", type=int, default=aoc_part)
    parser.add_argument("-e", "--example", action="store_true")
    args = parser.parse_args()

    main(args.day, args.part, args.example)
