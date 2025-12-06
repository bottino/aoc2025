import re


def part_1(input: str) -> int:
    lines = input.splitlines()
    numbers = []
    for i, line in enumerate(lines):
        line = line.strip()
        line = re.sub("\s+", ",", line)
        numbers.append(line.split(","))

    operators = numbers[-1]
    numbers = numbers[:-1]

    total = 0
    for i in range(len(operators)):
        operands = [n[i] for n in numbers]
        calculation = operators[i].join(operands)
        print(calculation)
        total += eval(calculation)

    return total

