from collections import defaultdict
from functools import lru_cache
from math import floor, log10, ceil, prod

from aocd import get_data

data = get_data(day=7, year=2025)
example = r""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def parse_input(raw_input: str):
    return raw_input.split("\n")

def splitters(line):
    return {i for i,c in enumerate(line) if c == "^"}

def split_beams(active_splitters):
    beams = set()
    for splitter in active_splitters:
        beams |= {splitter-1, splitter+1}
    return beams

def part1(used_input: str):
    lines = parse_input(used_input)
    total = 0
    start_position = lines[0].find("S")
    beams = {start_position}
    for line in lines[1:]:
        active_splitters = beams & splitters(line)
        total += len(active_splitters)
        passing_beams = beams - active_splitters
        beams = passing_beams | split_beams(active_splitters)
    return total

def split_paths(active_splitters):
    paths = defaultdict(int)
    for i, incoming_paths in active_splitters.items():
        paths[i-1] += incoming_paths
        paths[i+1] += incoming_paths
    return paths

def part2(used_input: str):
    lines = parse_input(used_input)
    start_position = lines[0].find("S")
    paths = {start_position: 1}
    for line in lines[1:]:
        active_splitters = {i: incoming_paths for i, incoming_paths in paths.items() if i in splitters(line)}
        passing_paths = {i: incoming_paths for i, incoming_paths in paths.items() if i not in active_splitters}
        paths = split_paths(active_splitters)
        for i, incoming_paths in passing_paths.items():
            paths[i] += incoming_paths
    return sum(paths.values())

print(part1(data))

print(part2(data))