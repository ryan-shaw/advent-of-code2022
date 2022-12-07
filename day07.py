from aoc import timer, read_input
from collections import defaultdict

def tree(): return defaultdict(tree)

directory_tree = tree()
path = []

def recursive_access(tree, cwd):
    if len(cwd) == 0: return tree
    new_dir = tree[cwd.pop(0)]
    return recursive_access(new_dir, cwd)


def parse_line(line : str):
    if line.startswith("$"):
        cmd = [c.strip() for c in line.split(" ")[1:]]
        if len(cmd) == 2:
            if cmd[1] == "/":
                path.clear()
            elif cmd[1] == "..":
                path.pop()
            else:
                path.append(cmd[1])
            
    else:
        if not line.startswith("dir"):
            dir = recursive_access(directory_tree, path.copy())
            dir[line.split(' ')[1]] = int(line.split(' ')[0])    

def directory_size(tree, results={}):
    size = 0
    for key, value in tree.items():
        if isinstance(value, int):
            size += value
        else:
            dir = recursive_access(tree, [key])
            dir_size = directory_size(dir, results)
            while key in results:
                key += "1" # don't care what the name is just that it's not overwriting existing
            results[key] = dir_size[0]
            size += dir_size[0]
    return size, results


@timer
def part1():
    total = sum([value for value in directory_size(directory_tree)[1].values() if value <= 100000])
    return total
    

@timer
def part2():
    total, sizes = directory_size(directory_tree)
    free = 70000000 - total
    required = 30000000 - free 
    return [v for v in sorted(sizes.values()) if v >= required][0]    

data = read_input(7)
[parse_line(line) for line in data]
part1()
part2()
