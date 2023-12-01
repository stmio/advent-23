file = open("./input/1.txt", "r").readlines()

total = 0
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in file:
    first, last = None, None
    for i in range(len(line)):
        if line[i].isnumeric():
            if first == None:
                first = line[i]
            else:
                last = line[i]
        else:
            for word, n in numbers.items():
                if line[i : i + len(word)] == word:
                    if first == None:
                        first = n
                    else:
                        last = n

    if last == None:
        last = first

    total += int(first + last)

print(total)
