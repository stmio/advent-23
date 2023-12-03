import numpy as np

file = np.array(open("./input/3.txt", "r").readlines())
file = np.char.strip(file, "\n")
engine = np.array([list(i) for i in file])

# get indicies for **possible** gears
gears = list(zip(*np.where(np.isin(engine, ["*"]))))
ratios = dict.fromkeys(gears, np.array([]))

for i in range(len(engine)):
    # (-1, -1) denotes that a gear is not currently selected
    gear = (-1, -1)
    part = ""

    for j in range(len(engine[i])):
        item = engine[i][j]

        if item.isnumeric():
            part += item
            if (i - 1, j) in gears:
                gear = (i - 1, j)
            if (i + 1, j) in gears:
                gear = (i + 1, j)
        elif (i, j) in gears:
            gear = (i, j)
            if part != "":
                ratios[gear] = np.append(ratios[gear], int(part))
                part = ""
        elif item == ".":
            if (i - 1, j) in gears:
                gear = (i - 1, j)
                if part != "":
                    ratios[gear] = np.append(ratios[gear], int(part))
                    part = ""
            elif (i + 1, j) in gears:
                gear = (i + 1, j)
                if part != "":
                    ratios[gear] = np.append(ratios[gear], int(part))
                    part = ""
            else:
                if gear != (-1, -1) and part != "":
                    ratios[gear] = np.append(ratios[gear], int(part))
                gear = (-1, -1)
                part = ""

    if gear != (-1, -1) and part != "":
        ratios[gear] = np.append(ratios[gear], int(part))

valid_ratios = {key: np.prod(val) for key, val in ratios.items() if val.size == 2}
total_ratio = sum(valid_ratios.values())

print(int(total_ratio))
