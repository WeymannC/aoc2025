from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from math import floor, log10, ceil, prod

from aocd import get_data

data = get_data(day=8, year=2025)
example = r"""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def parse_input(raw_input: str):
    points = []
    for line in raw_input.split("\n"):
        x,y,z = line.split(",")
        points.append((int(x), int(y), int(z)))
    return points

def square_distance(p, q):
    x,y,z = p
    r,s,t = q
    return (x-r)**2 + (y-s)**2 + (z-t)**2

def build_distances(points):
    return [(square_distance(p,q), p, q) for p, q in combinations(points, 2)]

def part1(used_input: str, number_of_links: int):
    points = parse_input(used_input)
    distances = build_distances(points)
    circuits = {point: {point} for point in points}

    selected_pairs = sorted(distances)[:number_of_links]
    for _, p, q in selected_pairs:
        for r in circuits[p].copy():
            circuits[r] |= circuits[q]
        for r in circuits[q].copy():
            circuits[r] |= circuits[p]

    visited = set()
    sizes = []
    for p, circuit in circuits.items():
        if p not in visited:
            sizes.append(len(circuit))
            visited |= circuit

    return prod(sorted(sizes, reverse=True)[:3])

def part2(used_input: str):
    points = parse_input(used_input)
    distances = build_distances(points)
    circuits = {point: {point} for point in points}

    selected_pairs = sorted(distances)
    for _, p, q in selected_pairs:
        for r in circuits[p].copy():
            circuits[r] |= circuits[q]
        for r in circuits[q].copy():
            circuits[r] |= circuits[p]
        if len(circuits[p]) == len(points):
            return p[0] * q[0]

print(part1(data, 1000))

print(part2(data))