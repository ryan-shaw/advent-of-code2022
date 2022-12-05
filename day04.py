from aoc import timer, read_input

def parse_data(data):
    for row in data:
        yield [[int(i) for i in item.split('-')] for item in row.split(',')]

def contains(p1, p2):
    return p1[0] <= p2[0] and p1[1] >= p2[1]

def overlaps(p1, p2):
    return p2[0] <= p1[1] and p2[1] >= p1[0]

@timer
def part1(data):
    return len([row for row in parse_data(data) if contains(*row) or contains(*reversed(row))])

@timer
def part2(data):
    return len([row for row in parse_data(data) if overlaps(*row) or overlaps(*reversed(row))])

data = read_input(4)
part1(data)
part2(data)
