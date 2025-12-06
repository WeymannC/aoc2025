from functools import lru_cache
from math import floor, log10, ceil, prod

from aocd import get_data

data = get_data(day=6, year=2025)
example = r"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def parse_input(raw_input: str):
    lines = []
    for number_line in raw_input.split("\n")[:-1]:
        lines.append(number_line.split())
    problems = []
    for i in range(len(lines[0])):
        problems.append([int(l[i]) for l in lines])
    operators = raw_input.split("\n")[-1].split()
    return problems, operators

def part1(used_input: str):
    problems, operators = parse_input(used_input)
    total = 0
    for i, operator in enumerate(operators):
        if operator == "+":
            total+=sum(problems[i])
        else:
            total+=prod(problems[i])
    return total

def parse_input_2(raw_input: str):
    raw_lines = raw_input.split("\n")
    problems, operators = [], []
    current_problem = []
    for i in range(len(raw_lines[0])-1, -1, -1):
        if (operator:=raw_lines[-1][i]) in ["+", "*"]:
            operators.append(operator)
            current_problem.append(int("".join(rl[i] for rl in raw_lines[:-1])))
            problems.append(current_problem)
            current_problem = []
            continue
        if not (number:="".join(rl[i] for rl in raw_lines)).strip():
            continue
        current_problem.append(int(number))
    return problems, operators

def part2(used_input: str):
    problems, operators = parse_input_2(used_input)
    total = 0
    for i, operator in enumerate(operators):
        if operator == "+":
            total += sum(problems[i])
        else:
            total += prod(problems[i])
    return total

print(part1(data))

print(part2(data))