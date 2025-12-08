from collections import defaultdict
from functools import lru_cache
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

@lru_cache(maxsize=None)
def square_distance(p, q):
    x,y,z = p
    r,s,t = q
    return (x-r)**2 + (y-s)**2 + (z-t)**2

def part1(used_input: str, number_of_links: int):
    pass

def part2(used_input: str):
    pass

print(part1(example, 10))

print(part2(example))