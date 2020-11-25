def has_unique(words):
    temp = []
    for word in words:
        if word not in temp:
            temp.append(word)
    return len(temp) == len(words)

solution_1 = 0

for line in open('inputs/04','r'):
    if has_unique(line.split()):
        solution_1 += 1

print("There are ", solution_1, "unique pass phrases!")
# There are  451 unique pass phrases!
