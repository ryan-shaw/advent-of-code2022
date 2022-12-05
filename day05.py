import math
from aoc import timer, read_raw_input

def parse_crates(crates : str) -> list:
    col_count = math.ceil(len(crates.split('\n')[0]) / 4)
    cols = [[] for _ in range(col_count)]
    lines = crates.split('\n')
    [[cols[x // 4].append(line[x+1]) for x in range(0, len(crates.split('\n')[0]), 4) if ord(line[x+1]) >= 65] for line in lines]
    return cols

def parse_moves(moves : str) -> list:
    for line in moves.split('\n'):
        _, count, _, col1, _, col2 = line.split(' ')
        yield int(count), int(col1), int(col2)

def parse_data(data : str) -> None:
    crates, moves = data.split('\n\n')
    return parse_crates(crates), parse_moves(moves)

def apply_move(crates : list, move: tuple, reverse):
    popped = [crates[move[1] - 1].pop(0) for _ in range(move[0])]
    if reverse:
        popped.reverse()
    crates[move[2] - 1] = popped + crates[move[2] - 1]

def do_moves(crates : list, moves : list, reverse=True) -> None:
    [apply_move(crates, move, reverse) for move in moves]
    return ''.join([x[0] for x in crates])

@timer
def part1(data):
    return do_moves(*parse_data(data))

@timer
def part2(data):
    return do_moves(*parse_data(data), reverse=False)

data = read_raw_input(5)
part1(data)
part2(data)
