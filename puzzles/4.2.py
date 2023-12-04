from functools import lru_cache

file = open("./input/4.txt", "r").readlines()
total = 0


# Returns number of cards won from (and including) original card i
@lru_cache
def cardWinnings(i):
    card = 0
    data = file[i].strip("\n")[file[i].find(":") + 2 :].lstrip()
    scratchcard = [n.split(" ") for n in data.replace("  ", " ").split(" | ")]

    matches = len(list(set(scratchcard[0]) & set(scratchcard[1])))
    for x in range(1, matches + 1):
        card += cardWinnings(i + x)

    return card + 1


for i in range(0, len(file)):
    total += cardWinnings(i)

print(total)
