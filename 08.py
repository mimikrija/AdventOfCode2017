with open('./inputs/08') as f:
    inputs = f.readlines()

def get_variable_name(instruction):
    return instruction[0][:instruction[0].index(" ")]

# create program, a list of instructions + conditions
program = []
for line in inputs:
    instr = line.strip().replace('inc','+=')
    instr = instr.replace('dec','-=')
    program.append(instr.split(" if "))

# curly braces generate a set <3
args = { get_variable_name(instruction) for instruction in program }

initialization = [ var +'=0' for var in args ]

for init in initialization:
    exec(init)

all_results = []
for instruction in program:
    if eval(instruction[1]):
        exec(instruction[0])
    all_results.append(eval(get_variable_name(instruction)))

final_results = [eval(arg) for arg in args]

solution_1 = max(final_results)
solution_2 = max(all_results)

print(f'Part 1: maximum value after all evaluations is {solution_1}!')
print(f'Part 2: maximum value reached during evaluations is {solution_2}!')
