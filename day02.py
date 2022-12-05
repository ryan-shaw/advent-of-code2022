from aoc import timer, read_input

score_map = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def parse_data():
    return [(score_map[item[0]], score_map[item[1]]) for item in [row.split(' ') for row in read_input(2)]]

@timer
def part1():
    data = parse_data()
    def calc():
        for challenge, response in data:
            score = (((challenge - response) + 1) % 3) * 3 + response
            yield score
    return sum(list(calc()))
    
@timer
def part2():
    data = parse_data()
    def calc():
        for challenge, state in data:
            result = (state - 1) * 3
            response = ((challenge + state) % 3) + 1
            yield result + response
    
    return sum(list(calc()))


part1()
part2()
