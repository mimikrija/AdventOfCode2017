with open('./inputs/06', 'r') as infile:
    memory = infile.readline().split()

for n in memory:
    memory[memory.index(n)] = int(n)
