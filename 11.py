import math
import re
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations, pairwise
from math import floor, log10, ceil, prod
from platform import machine

from aocd import get_data

data = get_data(day=11, year=2025)
example = r"""aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

example2 = r"""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

def parse_input(raw_input: str):
    devices = {}
    for line in raw_input.split("\n"):
        key, raw_values = line.split(": ")
        values = tuple(raw_values.split(" "))
        devices[key] = values
    return devices

def count_paths(start, end, devices) -> int:
    @lru_cache(None)
    def _count_paths(s):
        if s == end:
            return 1
        if s not in devices:
            return 0
        return sum(_count_paths(device) for device in devices[s])

    return _count_paths(start)

def part1(used_input: str):
    devices = parse_input(used_input)
    return count_paths("you", "out", devices)


def part2(used_input: str):
    devices = parse_input(used_input)
    return (
            count_paths("svr", "dac", devices)*count_paths("dac", "fft", devices)*count_paths("fft", "out", devices)
            + count_paths("svr", "fft", devices)*count_paths("fft", "dac", devices)*count_paths("dac", "out", devices)
    )

print(part1(data))

print(part2(data))