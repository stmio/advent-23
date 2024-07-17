import numpy as np
import itertools

file = np.array(open("./input/11.txt", "r").readlines())
file = np.char.strip(file, "\n")
space = np.array([list(i) for i in file])

expanding_rows = [i for i in range(len(space)) if not np.any(np.isin(space[i, :], "#"))]
expanding_cols = [i for i in range(len(space)) if not np.any(np.isin(space[:, i], "#"))]
space = np.insert(space, expanding_rows, ".", axis=0)
space = np.insert(space, expanding_cols, ".", axis=1)

galaxies = list(zip(*np.where(np.isin(space, ["#"]))))

total = 0
for pair in itertools.combinations(galaxies, 2):
    g1, g2 = pair
    total += abs(g2[0] - g1[0])
    total += abs(g2[1] - g1[1])

print(total)
