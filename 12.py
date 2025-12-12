import math
import re
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations, pairwise
from math import floor, log10, ceil, prod
from platform import machine

from aocd import get_data

data = get_data(day=12, year=2025)
example = r"""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

def augment_shape(base_shape):
    def rotate(shape):
        return tuple("".join(line[i] for line in shape[::-1]) for i in range(len(shape[0])))
    def rotated(shape):
        return {shape, rotate(shape), rotate(rotate(shape)), rotate(rotate(rotate(shape)))}
    def flip(shape):
        return tuple(line[::-1] for line in shape)
    return rotated(base_shape) | rotated(flip(base_shape))

def parse_input(raw_input: str):
    blocks = raw_input.split("\n\n")

    presents = {}
    for raw_present in blocks [:-1]:
        raw_lines = raw_present.split("\n")
        index = int(raw_lines[0].strip(":"))
        base_shape = tuple(raw_lines[1:])
        presents[index] = augment_shape(base_shape)

    trees = []
    for line in blocks[-1].split("\n"):
        raw_size, raw_present_list = line.split(": ")
        size = tuple(int(s) for s in raw_size.split("x"))
        present_list = tuple(int(amount) for amount in raw_present_list.split(" "))
        trees.append((size, present_list))

    return presents, trees

def occupied_area(present):
    total = 0
    variant = next(iter(present))
    for line in variant:
        total += sum(1 if c == "#" else 0 for c in line)
    return total

def part1(used_input: str):
    presents, trees = parse_input(used_input)
    total = 0
    for size, present_list in trees:
        available_area = size[0]*size[1]
        needed_area = sum(amount*occupied_area(presents[i]) for i, amount in enumerate(present_list))
        if available_area < needed_area:
            continue
        x, y = size
        available_tiles = x//3 * y//3
        number_of_tiles = sum(present_list)
        if available_tiles < number_of_tiles:
            continue
        total += 1
    return total

print(part1(data))
