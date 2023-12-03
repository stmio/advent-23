import numpy as np

file = np.array(open("./input/3.txt", "r").readlines())
file = np.char.strip(file, "\n")
engine = np.array([list(i) for i in file])

# get indicies for symbols
symbols = list(zip(*np.where(~np.char.isnumeric(engine) & ~np.isin(engine, ["."]))))
parts = []

for i in range(len(engine)):
    validPart = False
    part = ""

    for j in range(len(engine[i])):
        item = engine[i][j]

        if item.isnumeric():
            part += item
            if (i - 1, j) in symbols or (i + 1, j) in symbols:
                validPart = True
        elif (i, j) in symbols:
            validPart = True
            if part != "":
                parts.append(int(part))
                part = ""
        elif item == ".":
            if (i - 1, j) in symbols or (i + 1, j) in symbols:
                validPart = True
                if part != "":
                    parts.append(int(part))
                    part = ""
            else:
                if validPart and part != "":
                    parts.append(int(part))
                validPart = False
                part = ""

    if validPart and part != "":
        parts.append(int(part))

print(int(sum(parts)))
