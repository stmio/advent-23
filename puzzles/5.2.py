file = open("./input/5.txt", "r").readlines()


def findMinLocation(locations):
    for location in range(0, max(locations) + 1):
        seed = location
        swapped = False
        for i in range(len(file) - 1, -1, -1):
            if not file[i].isspace() and file[i][0].isnumeric():
                data = [int(x) for x in file[i].strip("\n").split(" ")]
                if data[0] <= seed < data[0] + data[2] and not swapped:
                    seed = seed - data[0] + data[1]
                    swapped = True
            else:
                swapped = False

        for r in seeds:
            if seed in r:
                return location


ranges = [int(n) for n in file[0].strip("\n").strip("seeds: ").split(" ")]
seeds = [range(ranges[i], ranges[i] + ranges[i + 1]) for i in range(0, len(ranges), 2)]
locations = []

for line in range(len(file) - 1, -1, -1):
    if not file[line][0].isnumeric():
        break
    data = [int(x) for x in file[line].strip("\n").split(" ")]
    locations.append(data[0] + data[2])

print(findMinLocation(locations))
