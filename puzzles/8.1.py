import numpy as np

current = "AAA"
target = "ZZZ"

file = np.array(open("./input/8.txt", "r").readlines())
file = np.char.strip(file, "\n")

pattern = file[0]
network = {
    node: tuple(lr.strip("()").split(", "))
    for node, lr in [i.split(" = ") for i in file[2:]]
}

counter = 0
steps = 0

while current != target:
    l, r = network[current]

    if pattern[counter] == "L":
        current = l
    elif pattern[counter] == "R":
        current = r

    counter += 1
    steps += 1

    if counter == len(pattern):
        counter = 0

print(steps)
