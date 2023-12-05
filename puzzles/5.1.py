file = open("./input/5.txt", "r").readlines()

seeds = {int(n): int(n) for n in file[0].strip("\n").strip("seeds: ").split(" ")}
mapped = []

for i in range(1, len(file)):
    if not file[i].isspace():
        if file[i][0].isnumeric():
            data = [int(x) for x in file[i].strip("\n").split(" ")]

            for seed in seeds:
                if seed in mapped:
                    if len(mapped) == len(seeds):
                        break
                    continue
                elif seeds[seed] >= data[1] and seeds[seed] <= data[1] + data[2]:
                    seeds[seed] = data[0] + (seeds[seed] - data[1])
                    mapped.append(seed)

        else:
            mapped = []

print(min(seeds.values()))
