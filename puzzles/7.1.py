import numpy as np

types = {
    "5k": [],
    "4k": [],
    "fh": [],
    "3k": [],
    "2p": [],
    "1p": [],
    "hc": [],
}

order = {c: i for i, c in enumerate("AKQJT98765432")}

file = np.array(open("./input/7.txt", "r").readlines())
file = np.char.strip(file, "\n")
hands = [(i.split(" ")[0], i.split(" ")[1]) for i in file]


for hand in hands:
    n = sorted(dict(zip(*np.unique(list(hand[0]), return_counts=True))).values())
    if max(n) == 5:
        types["5k"].append(hand)
    elif max(n) == 4:
        types["4k"].append(hand)
    elif max(n) == 3 and 2 in n:
        types["fh"].append(hand)
    elif max(n) == 3:
        types["3k"].append(hand)
    elif n.count(2) == 2:
        types["2p"].append(hand)
    elif max(n) == 2:
        types["1p"].append(hand)
    else:
        types["hc"].append(hand)


rank = []


for t in types.values():
    t.sort(key=lambda word: [order.get(c) for c in word[0]])
    for hand in t:
        rank.append(hand)

winnings = 0
for i in range(len(rank)):
    winnings += int(rank[i][1]) * (len(rank) - i)

print(winnings)
