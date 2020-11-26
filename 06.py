def is_unique(configuration):
    return len(set(configuration)) == len(configuration)

def list_to_string(memory):
    memory_string = ''
    for n in memory:
        memory_string += str(n)
    return memory_string

def do_the_shuffle(memory):
    chosen = max(memory) # the memory block that gets redistributed
    positions = [(memory.index(chosen)+ 1 + i) % size for i in range(size)]

    memory[memory.index(chosen)] = 0 # reset chosen memory slot

    i = 0
    for n in positions:
        memory[n] += chosen // size
        if i < chosen%size:
            memory[n] += 1
        i += 1
    return(memory)

with open('./inputs/06', 'r') as infile:
    memory = infile.readline().split()

for n in memory:
    memory[memory.index(n)] = int(n)

size = len(memory)

# part 1
instructions=[list_to_string(memory)]
solution_1 = 0

while is_unique(instructions):
    instructions.append(list_to_string(do_the_shuffle(memory)))
    solution_1 += 1

# part 2
memory_2 = memory.copy()
instructions_2 = []
solution_2 = 0

while memory not in instructions_2:
    instructions_2.append(do_the_shuffle(memory_2))
    solution_2 += 1


print("It takes ", solution_1, "cycles to reach the same memory configuration!")
# It takes  11137 cycles to reach the same memory configuration!

print("It takes ", solution_2, "more cycles to reach it again!")
# It takes  1037 more cycles to reach it again!
