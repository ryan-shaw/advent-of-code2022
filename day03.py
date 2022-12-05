from aoc import timer, read_input


def get_priority(char):
    return ord(char) - 96 if ord(char) > 95 else ord(char) - 38


def split_line(line):
    return set(line[:len(line)//2]), set(line[len(line)//2:])

# part1 
@timer
def part1(data):
    total = 0
    for line in data:
        c1, c2 = split_line(line)
        total += sum([get_priority(c) for c in set.intersection(c1, c2)])

    return total

@timer
def part2(data):
    total = 0
    for idx in range(0, len(data), 3):
        lines = []
        for line in data[idx:idx+3]:
            lines += [set([get_priority(c) for c in line])]
        value = list(set.intersection(*lines))[0]
        total += value
    return total

data = read_input(3)
part1(data)
part2(data)
