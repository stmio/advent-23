import numpy as np
import itertools

ex_factor = 1000000

file = np.array(open("./input/11.txt", "r").readlines())
file = np.char.strip(file, "\n")
space = np.array([list(i) for i in file])

expanding_rows = [i for i in range(len(space)) if not np.any(np.isin(space[i, :], "#"))]
expanding_cols = [i for i in range(len(space)) if not np.any(np.isin(space[:, i], "#"))]

galaxies = list(zip(*np.where(np.isin(space, ["#"]))))

for galaxy in range(len(galaxies)):
    y, x = galaxies[galaxy]
    galaxies[galaxy] = (
        y + len([i for i in expanding_rows if i < y]) * (ex_factor - 1),
        x + len([i for i in expanding_cols if i < x]) * (ex_factor - 1),
    )

total = 0
for pair in itertools.combinations(galaxies, 2):
    g1, g2 = pair
    total += abs(g2[0] - g1[0])
    total += abs(g2[1] - g1[1])

print(total)
