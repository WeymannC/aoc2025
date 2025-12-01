from aocd import get_data

data = get_data(day=1, year=2025)
example = r"""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

used_input = data
starting_position = 50

def parse_input(raw_input: str) -> list[int]:
    steps = []
    for instruction in raw_input.split("\n"):
        if instruction[0] == "R":
            steps.append(int(instruction[1:]))
        else:
            steps.append(-int(instruction[1:]))
    return steps

position = starting_position
total = 0
for instruction in parse_input(used_input):
    position += instruction
    if position % 100 == 0:
        total += 1

print(total)