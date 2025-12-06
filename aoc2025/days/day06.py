import re


def part_1(input: str) -> int:
    lines = input.splitlines()
    numbers = []
    for i, line in enumerate(lines):
        numbers.append(_prepare_line(line))

    operators = numbers[-1]
    numbers = numbers[:-1]

    total = 0
    for i in range(len(operators)):
        operands = [n[i] for n in numbers]
        calculation = operators[i].join(operands)
        total += eval(calculation)

    return total


def part_2(input: str) -> int:
    # Transpose input
    lines = input.splitlines()
    rev = [line[::-1] for line in lines[:-1]]
    transposed = [("".join(list(e))).strip() for e in zip(*rev)]
    operators = _prepare_line(lines[-1])[::-1]  # reverted because starting from right

    # Prepare operations
    operands = [[]]
    current_calc = 0
    for line in transposed:
        if line == "":
            operands.append([])
            current_calc += 1
        else:
            operands[current_calc].append(line)

    # Perform operations
    total = 0
    for i in range(len(operators)):
        calculation = operators[i].join(operands[i])
        total += eval(calculation)

    return total


def _prepare_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\s+", ",", line)
    return line.split(",")

