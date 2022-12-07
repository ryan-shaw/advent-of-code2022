from aoc import timer, read_input
from collections import Counter

def get_part(data, marker_count):
    return [c[0] + marker_count for c in enumerate(data) if len(Counter(data[c[0]:marker_count+c[0]]).keys()) == marker_count][0]

@timer
def part1(data):
    return get_part(data, 4)

@timer
def part2(data):
    return get_part(data, 14)

data = read_input(6)[0]
part1(data)
part2(data)
