from functools import lru_cache
from math import floor, log10, ceil

from aocd import get_data

data = get_data(day=3, year=2025)
example = r"""987654321111111
811111111111119
234234234234278
818181911112111"""


def parse_input(raw_input: str):
    banks = []
    for raw_bank in raw_input.split("\n"):
        banks.append([int(c) for c in raw_bank])
    return banks

def largest_joltage(bank: list[int], number_of_batteries: int, current_total: int = 0) -> int:
    if number_of_batteries > len(bank):
        raise ValueError("Bank too small")
    if number_of_batteries == 1:
        current_total += max(bank)
        return current_total
    next_value = max(bank[:1-number_of_batteries])
    next_battery = bank.index(next_value)
    current_total += next_value*10**(number_of_batteries-1)
    return largest_joltage(bank[next_battery+1:], number_of_batteries-1, current_total)

def part1(used_input: str):
    banks = parse_input(used_input)
    total = 0
    for bank in banks:
        total += largest_joltage(bank, 2, 0)
    return total

def part2(used_input: str):
    banks = parse_input(used_input)
    total = 0
    for bank in banks:
        total += largest_joltage(bank, 12, 0)
    return total

print(part1(data))

print(part2(data))