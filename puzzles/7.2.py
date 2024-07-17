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

file = np.array(open("./input/7.txt", "r").readlines())
file = np.char.strip(file, "\n")
hands = [(i.split(" ")[0], i.split(" ")[1]) for i in file]


for hand in hands:
    count = dict(zip(*np.unique(list(hand[0]), return_counts=True)))
    jokers = count.get("J", 0)
    count.pop("J", None)
    n = list(count.values())

    if len(n) == 1 or len(n) == 0:
        types["5k"].append(hand)
    elif max(n) + jokers == 4:
        types["4k"].append(hand)
    elif (len(n) == 2 and 3 in n and 2 in n) or (n.count(2) == 2 and jokers == 1):
        types["fh"].append(hand)
    elif 3 - jokers in n:
        types["3k"].append(hand)
    elif (2 in n and n.count(2) == 2) or (jokers > 0 and 2 in n):
        types["2p"].append(hand)
    elif 2 - jokers in n:
        types["1p"].append(hand)
    else:
        types["hc"].append(hand)


rank = []
order = {c: i for i, c in enumerate("AKQT98765432J")}

for t in types.values():
    t.sort(key=lambda word: [order.get(c) for c in word[0]])
    for hand in t:
        rank.append(hand)

winnings = 0
for i in range(len(rank)):
    winnings += int(rank[i][1]) * (len(rank) - i)

print(winnings)
