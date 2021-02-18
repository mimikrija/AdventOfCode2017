# Day 16: Permutation Promenade

from santas_little_helpers import *


def spin(in_list, count):
    return in_list[-count:] + in_list[:-count]

def exchange(in_list, A, B):
    first, second = sorted((A, B))
    return in_list[:first] + [in_list[second]] + in_list[first+1:second] + [in_list[first]] + in_list[second+1:]

def partner(in_list, name_A, name_B):
    return exchange(in_list, in_list.index(ord(name_A)), in_list.index(ord(name_B)))

def dance(in_instructions, sequence):
    for args in in_instructions:
        try:
            arguments = list(map(int, args))
            if len(arguments) == 1:
                sequence = spin(sequence, *arguments)
            else:
                sequence = exchange(sequence, *arguments)
        except:
            sequence = partner(sequence, *args)
    return sequence


dance_instructions = (instruction[1:].split('/') for instruction in get_input('inputs/16',','))
sequence = list(range(ord('a'), ord('p')+1))


sequence = dance(dance_instructions, sequence)
part_1 = ''.join(chr(c) for c in sequence)

print_solutions(part_1)
# Part 1 solution is: kgdchlfniambejop
