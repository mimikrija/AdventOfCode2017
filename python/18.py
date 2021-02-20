# Day 18: Duet
from santas_little_helpers import *
from collections import deque


def initialize_registers(instructions):
    registers = {}
    for instruction in instructions:
        potential_letter = instruction[1]
        try:
            int(potential_letter)
        except:
            registers[potential_letter] = 0
    return registers


def duo(instructions, registers, pos=0, is_part_2=False, in_data=deque([])):
    out_data = deque()
    while pos < len(instructions):
        operation, *args = instructions[pos]
        if operation == 'snd':
            if not is_part_2:
                sound = registers[args[0]]
            else:
                try:
                    out_data.appendleft(int(args[0]))
                except:
                    out_data.appendleft(registers[args[0]])

        if operation == 'rcv':
            if not is_part_2:
                try:
                    compare = int(args[0])
                except:
                    compare = registers[args[0]]
                if compare != 0:
                    if sound != 0:
                        return sound
            else:
                if in_data:
                    registers[args[0]] = in_data.pop()
                else:
                    return registers, pos, out_data


        if operation == 'set':
            try:
                registers[args[0]] = int(args[1])
            except:
                registers[args[0]] = registers[args[1]]

        if operation == 'add':
            try:
                registers[args[0]] += int(args[1])
            except:
                registers[args[0]] += registers[args[1]]

        if operation == 'mul':
            try:
                registers[args[0]] *= int(args[1])
            except:
                registers[args[0]] *= registers[args[1]]

        if operation == 'mod':
            try:
                registers[args[0]] %= int(args[1])
            except:
                registers[args[0]] %= registers[args[1]]

        if operation == 'jgz':
            try:
                compare = int(args[0])
            except:
                compare = registers[args[0]]
            if compare > 0:
                try:
                    pos += int(args[1]) - 1
                except:
                    pos += registers[args[1]] - 1

        pos += 1


instructions = [line.split(' ') for line in get_input('inputs/18')]

registers_pt1 = initialize_registers(instructions)
part_1 = duo(instructions, registers_pt1)

print_solutions(part_1)
# Part 1 solution is: 3188

# part_2:
program_0 = initialize_registers(instructions)
program_0['p'] = 0
program_0_output = deque()
pos_0 = 0
program_1 = initialize_registers(instructions)
program_1['p'] = 1
program_1_output = deque()
pos_1 = 0
part_2 = 0
deadlock = False
while not deadlock:
    program_0, pos_0, program_0_output = duo(instructions, program_0, pos_0, True, program_1_output)
    #print(program_0, pos_0, program_0_output)
    program_1, pos_1, program_1_output = duo(instructions, program_1, pos_1, True, program_0_output)
    #print(program_1, pos_1, program_1_output)
    part_2 += len(program_1_output)
    if not program_0_output and not program_1_output:
        print(f'program 1 sent data {part_2} times')
        break
