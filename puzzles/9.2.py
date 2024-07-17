import numpy as np

file = np.array(open("./input/9.txt", "r").readlines())
file = np.char.strip(file, "\n")
values = np.array([i.split(" ") for i in file]).astype(np.int64)

total = 0

for i in range(len(values)):
    sequence = np.array([values[i]])

    while np.any(sequence[-1] != np.zeros(sequence.shape[1])):
        diff = np.array(
            [
                sequence[-1][v + 1] - sequence[-1][v]
                for v in range(sequence.shape[0] - 1, len(values[i]) - 1)
            ]
        )
        diff = np.pad(diff, (sequence.shape[1] - len(diff), 0), "constant")
        sequence = np.vstack([sequence, diff])

    x = 0
    for r in range(sequence.shape[0] - 1, -1, -1):
        x = sequence[r][r] - x
    total += x

print(total)
