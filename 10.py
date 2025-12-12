import math
import re
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations, pairwise
from math import floor, log10, ceil, prod
from platform import machine

from aocd import get_data
from pulp import LpVariable, LpProblem, LpMinimize, lpSum, value
from sympy import Matrix

data = get_data(day=10, year=2025)
example = r"""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def parse_input(raw_input: str):
    machines = []
    for line in raw_input.split("\n"):
        match = re.match(r"\[(?P<lights>.*)\] (?P<buttons>.*) {(?P<joltages>.*)}", line)
        lights = tuple(c == "#" for c in match["lights"])
        buttons = tuple(tuple(int(b) for b in raw_button.strip("()").split(",")) for raw_button in match["buttons"].split(" "))
        joltages = tuple(int(j) for j in match["joltages"].strip("{}").split(","))
        machines.append((lights, buttons, joltages))
    return machines

def least_presses_lights(state, target, buttons) -> int:
    queue = deque()
    queue.extend((state, target, action, 0) for action in buttons)
    while queue:
        s, t, a, counter = queue.popleft()
        new_state = tuple( light != (i in a) for i, light in enumerate(s))
        if new_state == t:
            return counter+1
        queue.extend((new_state, target, action, counter + 1) for action in buttons)

def part1(used_input: str):
    machines = parse_input(used_input)
    return sum(least_presses_lights(tuple(False for _ in lights), lights, buttons) for lights, buttons, _ in machines)

def part2(used_input: str):
    machines = parse_input(used_input)
    total = 0
    for _, buttons, joltages in machines:
        variables = [LpVariable(str(button), 0, cat="Integer") for button in buttons]
        problem = LpProblem("problem", LpMinimize)
        problem += lpSum(variables)
        for i, joltage in enumerate(joltages):
            problem += lpSum(variable for variable, button in zip(variables, buttons) if i in button) == joltage
        problem.solve()
        total += sum(value(variable) for variable in variables)


    return total

# print(part1(data))

print(part2(data))