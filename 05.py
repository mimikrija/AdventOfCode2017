infile = open('./inputs/05', 'r')

instructions = []
for line in infile:
    instructions.append(int(line))

#print(instructions)
index = 0
solution_1 = 0

while index < len(instructions):
    next_index = instructions[index]
    instructions[index] += 1
    index += next_index
    solution_1 += 1

print("Part 1: it takes ", solution_1, "steps to exit!")
# Part 1: it takes  375042 steps to exit!