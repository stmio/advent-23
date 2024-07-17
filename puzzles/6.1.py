import numpy as np

file = open("./input/6.txt", "r").readlines()

races = [" ".join(n.strip("\n").split()) for n in file]
races = np.array([n[n.find(": ") + 2 :].split(" ") for n in races]).astype(int)

margin = []

for i in range(races.shape[1]):
    time, record = races[0][i], races[1][i]

    distances = []
    for t in range(0, time + 1):
        speed = t
        moving_time = time - t
        distance = moving_time * speed
        distances.append(distance)

    winning_distances = len([d for d in distances if d > record])
    margin.append(winning_distances)

print(np.prod(margin))
