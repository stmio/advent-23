file = open("./input/1.txt", "r").readlines()

total = 0

for line in file:
    line = line.strip("\n")

    str = ""

    for i in range(0, len(line), 1):
        if line[i].isdigit():
            str += line[i]
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            str += line[i]
            break

    total += int(str)

print(total)
