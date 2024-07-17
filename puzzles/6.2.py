import numpy as np

file = open("./input/6.txt", "r").readlines()

race = ["".join(n.strip("\n").split()) for n in file]
race = np.array([n[n.find(":") + 1 :] for n in race]).astype(np.int64)

time, record = race[0], race[1]

distances = []

for t in range(0, time + 1):
    speed = t
    moving_time = time - t
    distance = moving_time * speed
    distances.append(distance)

winning_distances = len([d for d in distances if d > record])

print(winning_distances)
