from functools import lru_cache
from math import floor, log10, ceil

from aocd import get_data

data = get_data(day=4, year=2025)
example = r"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def parse_input(raw_input: str):
    return [[c for c in line] for line in raw_input.split("\n")]

def is_occupied(i,j,lines) -> bool:
    if 0 <= i < len(lines[0]) and 0 <= j < len(lines):
        return lines[j][i] == "@"
    return False

def neighbors(i,j,lines) -> int:
    return sum(
        1 if is_occupied(k,l,lines) else 0
        for k,l in [
            (i + 1, j + 1),
            (i + 1, j ),
            (i + 1, j - 1),
            (i , j + 1),
            (i , j - 1),
            (i - 1, j + 1),
            (i - 1, j ),
            (i - 1, j - 1),
        ]
    )


def part1(used_input: str):
    lines = parse_input(used_input)
    return sum(
        1 if lines[j][i] == "@" and neighbors(i,j,lines) < 4 else 0
        for i in range(len(lines[0]))
        for j in range(len(lines))
    )

def part2(used_input: str):
    lines = parse_input(used_input)
    total = 0
    previous_total = None
    while total != previous_total:
        previous_total = total
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                if lines[j][i] == "@" and neighbors(i,j,lines) < 4:
                    total += 1
                    lines[j][i] = "."
    return total

print(part1(data))

print(part2(data))