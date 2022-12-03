from aoc import timer, read_raw_input


# part1 
@timer
def part1():
    data = read_raw_input(1)
    data = max([sum([int(cal) for cal in elf]) for elf in [elf.strip().split('\n') for elf in data.split('\n\n')]])
    return data

# part2
@timer
def part2():
    data = read_raw_input(1)
    data = sorted([sum([int(cal) for cal in elf]) for elf in [elf.strip().split('\n') for elf in data.split('\n\n')]])
    return sum(data[-3:])

part1()
part2()
