import numpy as np

file = np.array(open("./input/8.txt", "r").readlines())
file = np.char.strip(file, "\n")

pattern = file[0]
network = {
    node: tuple(lr.strip("()").split(", "))
    for node, lr in [i.split(" = ") for i in file[2:]]
}

currents = [n for n in network.keys() if n[2] == "A"]
targets = [n for n in network.keys() if n[2] == "Z"]


for i in range(len(currents)):
    counter = 0
    steps = 0

    while currents[i] not in targets:
        l, r = network[currents[i]]

        if pattern[counter] == "L":
            currents[i] = l
        elif pattern[counter] == "R":
            currents[i] = r

        counter += 1
        steps += 1

        if counter == len(pattern):
            counter = 0

    currents[i] = steps


print(np.lcm.reduce(np.array(currents).astype(np.int64)))
