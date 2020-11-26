infile = open('./inputs/05', 'r')

instructions = []
for line in infile:
    instructions.append(int(line))

#print(instructions)
index = 0
solution = 0
part = '2'

while index < len(instructions):
    next_index = instructions[index]
    if part == '2' and next_index >= 3:
        instructions[index] -= 1
    else:
        instructions[index] += 1
    index += next_index
    solution += 1

print("Part", part, ": it takes ", solution, "steps to exit!")
# Part 1: it takes  375042 steps to exit!
# Part 2: it takes  28707598 steps to exit!