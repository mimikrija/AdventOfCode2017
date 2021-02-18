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


def first_42_dances(in_instructions, in_sequence):
    # after running about 1000 dances and putting them into a set,
    # I realized that there are only 42 unique dance solutions which
    # start repeating - it is enough to generate first 43 - index 0
    # denotes the starting position before any dance is made
    sequence = list(in_sequence)
    dances = [sequence]
    for _ in range(43):
        sequence = dance(list(dance_instructions), sequence)
        dances.append(sequence)
    return dances


def convert_list_to_string(in_list):
    return ''.join(chr(c) for c in in_list)


dance_instructions = [instruction[1:].split('/') for instruction in get_input('inputs/16',',')]
start_sequence = list(range(ord('a'), ord('p')+1))


first_dance = convert_list_to_string(dance(dance_instructions, start_sequence))
# there is no need to dance a billion times because the dances start repeating after 42 times
billionth_dance = convert_list_to_string(first_42_dances(dance_instructions, start_sequence)[(1000*1000*1000)%42])

print_solutions(first_dance, billionth_dance)
# Part 1 solution is: kgdchlfniambejop
# Part 2 solution is: fjpmholcibdgeakn
