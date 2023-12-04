file = open("./input/4.txt", "r").readlines()
total = 0


def cardPoints(card):
    card = card.strip("\n")[card.find(":") + 2 :].lstrip()
    scratchcard = [n.split(" ") for n in card.replace("  ", " ").split(" | ")]

    matches = len(list(set(scratchcard[0]) & set(scratchcard[1])))
    return 2 ** (matches - 1) if matches > 0 else 0


for i in range(0, len(file)):
    total += cardPoints(file[i])

print(total)
