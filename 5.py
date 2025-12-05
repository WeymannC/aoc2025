from functools import lru_cache
from math import floor, log10, ceil

from aocd import get_data

data = get_data(day=5, year=2025)
example = r"""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def parse_input(raw_input: str):
    raw_ranges, raw_items = raw_input.split("\n\n")
    ranges = [(int(start), int(end)) for start, end in (r.split("-") for r in raw_ranges.split("\n"))]
    items = [int(i) for i in raw_items.split("\n")]
    return ranges, items

def is_in_range(i, r):
    start, end = r
    return start <= i <= end

def is_fresh(i, ranges):
    return any(is_in_range(i, r) for r in ranges)

def part1(used_input: str):
    ranges, items = parse_input(used_input)
    return sum(1 if is_fresh(i, ranges) else 0 for i in items)

class CombinedRanges:

    def __init__(self):
        self._subranges: list[tuple[int,int]] = []

    @property
    def size(self) -> int:
        return sum(self._size(r) for r in self._subranges)

    @staticmethod
    def _size(r) -> int:
        start, end = r
        return end-start+1

    def add(self,r):
        r_start, r_end = r
        if any(is_in_range(r_start, s) and is_in_range(r_end, s) for s in self._subranges):
            return
        subranges_to_consider = [s for s in self._subranges if any(is_in_range(ss, r) for ss in s)]
        if not subranges_to_consider:
            self._subranges.append(r)
            return
        new_start = min(r_start, min(s_start for s_start, _ in subranges_to_consider))
        new_end = max(r_end, max(s_end for _, s_end in subranges_to_consider))
        self._subranges = [s for s in self._subranges if s not in subranges_to_consider]
        self._subranges.append((new_start, new_end))


def part2(used_input: str):
    ranges, _ = parse_input(used_input)
    combined_ranges = CombinedRanges()
    for r in ranges:
        combined_ranges.add(r)
    return combined_ranges.size

print(part1(data))

print(part2(data))