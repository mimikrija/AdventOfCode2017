def is_unique(configuration):
    return len(set(configuration)) == len(configuration)

def list_to_string(memory):
    memory_string = ''
    for n in memory:
        memory_string += str(n)
    return memory_string
        

with open('./inputs/06', 'r') as infile:
    memory = infile.readline().split()

for n in memory:
    memory[memory.index(n)] = int(n)

instructions=[list_to_string(memory)]

solution_1 = 0 # number of cycles


while is_unique(instructions):
    chosen = max(memory)

    basic_add = [ chosen // 16 for _ in range (16)]
    remainder_add = [ 1 for _ in range (chosen % 16)]

    positions = [(memory.index(chosen)+1 + i) % 16 for i in range(16)]


    solution_1 += 1
    i = 0
    memory[memory.index(chosen)] = 0

    for n in positions:
        memory[n] += basic_add[i]
        if i < len(remainder_add):
            memory[n] += remainder_add[i]
        i+= 1
    instructions.append(list_to_string(memory))

print("It takes ", solution_1, "cycles to reach the same memory configuration!")
# It takes  11137 cycles to reach the same memory configuration!