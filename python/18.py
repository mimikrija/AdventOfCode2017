# Day 18: Duet
from santas_little_helpers import *


def initialize_registers(instructions):
    registers = {}
    for instruction in instructions:
        potential_letter = instruction[1]
        try:
            int(potential_letter)
        except:
            registers[potential_letter] = 0
    return registers


def duo(instructions, registers, pos=0, is_part_2=False):

    while pos < len(instructions):
        operation, *args = instructions[pos]
        if operation == 'snd':
            if not is_part_2:
                sound = registers[args[0]]

        if operation == 'rcv':
            if not is_part_2:
                try:
                    compare = int(args[0])
                except:
                    compare = registers[args[0]]
                if compare != 0:
                    if sound != 0:
                        return sound


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
