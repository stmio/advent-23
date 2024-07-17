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
                for v in range(len(values[i]) - sequence.shape[0])
            ]
        )
        diff = np.pad(diff, (0, sequence.shape[1] - len(diff)), "constant")
        sequence = np.vstack([sequence, diff])

    for r in range(sequence.shape[0]):
        total += sequence[r][-(r + 1)]

print(total)
