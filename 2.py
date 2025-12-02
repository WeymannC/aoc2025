from math import floor, log10, ceil

from aocd import get_data

data = get_data(day=2, year=2025)
example = r"""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def parse_input(raw_input: str):
    pairs = []
    for raw_pair in raw_input.split(","):
        start, end = raw_pair.split("-")
        pairs.append((int(start), int(end)))
    return pairs

def number_of_digits(n: int) -> int:
    return ceil(log10(n))

def part1(used_input: str):
    pairs = parse_input(used_input)
    total = 0
    for start, end in pairs:
        for i in range(start, end+1):
            if number_of_digits(i) % 2 == 0:
                divisor = 10**(number_of_digits(i)/2) + 1
                if i % divisor == 0:
                    total += i
    return total


print(part1(data))