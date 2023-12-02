from numpy import prod

file = open("./input/2.txt", "r").readlines()
total = 0

for i in range(len(file)):
    gameId = i + 1
    data = file[i].strip("\n")[file[i].find(":") + 2 :].split("; ")
    game = {"red": 0, "green": 0, "blue": 0}

    for j in range(len(data)):
        cubes = data[j].split(", ")
        cubes = [cube.split(" ") for cube in cubes]

        round = {
            colour: ([int(c[0]) for c in cubes if c[1] == colour] or [0]).pop()
            for colour in list(game)
        }

        game = {colour: max(n, round[colour]) for colour, n in game.items()}

    power = prod([n for n in game.values()])
    total += power

print(total)
