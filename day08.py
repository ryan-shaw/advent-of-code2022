import math
from aoc import timer, read_input

def load_grid():
    grid = []
    data = read_input(8)
    for row in data:
        grid.append([int(chr) for chr in row])
    return grid

@timer
def part1(grid):
    visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree = grid[row][col]
            if col == len(grid[row]) - 1 or col == 0 or row == len(grid) - 1 or row == 0:
                visible += 1
                continue

            if tree > max(grid[row][col+1:]):
                visible += 1
                continue

            if tree > max(grid[row][:col]):
                visible += 1
                continue

            if tree > max([grid[x][col] for x in range(len(grid)) if x < row]):
                visible += 1
                continue

            if tree > max([grid[x][col] for x in range(len(grid)) if x > row]):
                visible += 1
                continue

    return visible

def get_visible_count(trees, tree):
    visible = 0
    for check_tree in trees:
        visible += 1
        if check_tree >= tree:
            break
    return visible

 
@timer
def part2(grid):
    max_visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree = grid[row][col]
            right = grid[row][col+1:]
            left = grid[row][:col]
            top = [grid[x][col] for x in range(len(grid)) if x < row]
            down = [grid[x][col] for x in range(len(grid)) if x > row]
            left.reverse()
            top.reverse()

            if not any(top and left and right and down):
                continue

            visible = math.prod([get_visible_count(direction, tree) for direction in [top, left, right, down]])
            max_visible = max(max_visible, visible)

    return max_visible

grid = load_grid()
part1(grid)
part2(grid)

