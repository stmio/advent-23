import numpy as np
import matplotlib.path as path

file = np.array(open("./input/10.txt", "r").readlines())
file = np.char.strip(file, "\n")
ground = np.array([list(i) for i in file])

pipes = list(zip(*np.where(~np.isin(ground, ["."]))))
pipes = {(y, x): ground[y][x] for (y, x) in pipes}
start = [key for key, val in pipes.items() if val == "S"].pop()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for dir in dirs:
    y, x = start
    dy, dx = dir
    location = (y + dy, x + dx)
    loop = []

    while location in list(pipes) and pipes[location] != "S":
        if pipes[location] == "|":
            if dy == 1:
                dy, dx = (1, 0)
            elif dy == -1:
                dy, dx = (-1, 0)
        elif pipes[location] == "-":
            if dx == 1:
                dy, dx = (0, 1)
            elif dx == -1:
                dy, dx = (0, -1)
        elif pipes[location] == "L":
            if dy == 1:
                dy, dx = (0, 1)
            elif dx == -1:
                dy, dx = (-1, 0)
        elif pipes[location] == "J":
            if dy == 1:
                dy, dx = (0, -1)
            elif dx == 1:
                dy, dx = (-1, 0)
        elif pipes[location] == "7":
            if dy == -1:
                dy, dx = (0, -1)
            elif dx == 1:
                dy, dx = (1, 0)
        elif pipes[location] == "F":
            if dy == -1:
                dy, dx = (0, 1)
            elif dx == -1:
                dy, dx = (1, 0)

        location = (y + dy, x + dx)
        y, x = y + dy, x + dx
        loop.append(location)

    if location in list(pipes) and pipes[location] == "S":
        break

# ensures "S" tile is at start of array
loop.reverse()

not_loop = list(set(np.ndindex(*ground.shape)) - set(loop))
polygon = path.Path(np.array(loop))
tiles = np.sum(polygon.contains_points(not_loop))

print(tiles)
