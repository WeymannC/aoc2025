from collections import defaultdict
from functools import lru_cache
from itertools import combinations, pairwise
from math import floor, log10, ceil, prod

from aocd import get_data

data = get_data(day=9, year=2025)
example = r"""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def parse_input(raw_input: str):
    points = []
    for line in raw_input.split("\n"):
        x,y = line.split(",")
        points.append((int(x), int(y)))
    return points

def rectangle_area(p, q):
    x,y = p
    r,s = q
    return (abs(x-r)+1)*(abs(y-s)+1)

def build_areas(points):
    return [(rectangle_area(p,q), p, q) for p, q in combinations(points, 2)]

def part1(used_input: str):
    points = parse_input(used_input)
    areas = build_areas(points)
    return max(area for area, _, _ in areas)

def build_edges(points):
    return list(pairwise(points)) + [(points[-1], points[0])]

def edge_in_area(p, q, edge):
    x, y = p
    r, s = q
    if any((min(x,r) < u < max(x,r)) and (min(y,s) < v < max(y,s)) for u, v in edge):
        return True
    ((a,b), (c,d)) = edge
    if b == d:
        if (min(a,c) <= min(x,r) and max(a,c) >= max(x,r)) and min(y,s) < b < max(y,s):
            return True
    if a == c:
        if (min(b,d) <= min(y,s) and max(b,d) >= max(y,s)) and min(x,r) < a < max(x,r):
            return True
    return False

def part2(used_input: str):
    points = parse_input(used_input)
    areas = build_areas(points)
    edges = build_edges(points)
    valid_areas = []
    for area, p, q in areas:
        if any(edge_in_area(p,q,edge) for edge in edges):
            continue
        valid_areas.append((area, p, q))
    return max(area for area, _, _ in valid_areas)

print(part1(data))

print(part2(data))