file = open("./input/2.txt", "r").readlines()
total = 0


def validateGame(data):
    data = data.strip("\n")[data.find(":") + 2 :].split("; ")

    for j in range(len(data)):
        cubes = data[j].split(", ")
        cubes = [cube.split(" ") for cube in cubes]

        if ([int(c[0]) for c in cubes if c[1] == "red"] or [0]).pop() > 12:
            return False
        if ([int(c[0]) for c in cubes if c[1] == "green"] or [0]).pop() > 13:
            return False
        if ([int(c[0]) for c in cubes if c[1] == "blue"] or [0]).pop() > 14:
            return False

    return True


for i in range(0, len(file)):
    gameId = i + 1
    if validateGame(file[i]):
        total += gameId

print(total)
