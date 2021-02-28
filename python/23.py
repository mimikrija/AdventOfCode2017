# Day 23: Coprocessor Conflagration

from santas_little_helpers import *
from math import sqrt


def initialize_registers(instructions):
    registers = {}
    for instruction in instructions:
        potential_letter = instruction[1]
        try:
            int(potential_letter)
        except:
            registers[potential_letter] = 0
    return registers


def duo(instructions, registers, pos=0):
    count_mul = 0
    while pos < len(instructions):
        operation, *args = instructions[pos]

        if operation == 'set':
            try:
                registers[args[0]] = int(args[1])
            except:
                registers[args[0]] = registers[args[1]]

        if operation == 'sub':
            try:
                registers[args[0]] -= int(args[1])
            except:
                registers[args[0]] -= registers[args[1]]

        if operation == 'mul':
            try:
                registers[args[0]] *= int(args[1])
            except:
                registers[args[0]] *= registers[args[1]]
            count_mul += 1

        if operation == 'mod':
            try:
                registers[args[0]] %= int(args[1])
            except:
                registers[args[0]] %= registers[args[1]]

        if operation == 'jnz':
            try:
                compare = int(args[0])
            except:
                compare = registers[args[0]]
            if compare != 0:
                try:
                    pos += int(args[1]) - 1
                except:
                    pos += registers[args[1]] - 1

        pos += 1

    return count_mul


instructions = [line.split(' ') for line in get_input('inputs/23')]

registers_pt1 = initialize_registers(instructions)
part_1 = duo(instructions, registers_pt1)

# part 2 - see 23-pt2.py and translate-23.txt for translation of assembly comments
compound = lambda x: any(x % num == 0 for num in range(2, int(sqrt(x))))

b = 79 * 100 + 100000
c = b + 17000
part_2 = sum(compound(num) for num in range(b, c+1, 17))


print_solutions(part_1, part_2)
# Part 1 solution is: 5929
# Part 2 solution is: 907
