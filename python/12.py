# Day 12: Digital Plumber

from santas_little_helpers import *


def find_connections(in_tree, find_next, all_programs=set()):
    if not all_programs:
        all_programs = set(find_next)
    while find_next:
        find_next = {child for find_me in find_next for child in in_tree[find_me] if child not in all_programs}
        all_programs |= set(find_next)
        find_connections(in_tree, find_next, all_programs)
    return all_programs


def count_groups(in_tree):
    already_included = set()
    count = 0
    for program in in_tree:
        if program not in already_included:
            already_included |= find_connections(in_tree, [program])
            count += 1
    return count


#connections_2 = {one: rest.split(', ') for line in get_input('inputs/12') for one, rest in line.split(' <-> ')}
connections = {}
for line in get_input('inputs/12'):
    a, b = line.split(' <-> ')
    connections[a] = b.split(', ')

programs_in_0_group = len(find_connections(connections, ['0']))
total_groups = count_groups(connections)

print_solutions(programs_in_0_group, total_groups)
# Part 1 solution is: 378
# Part 2 solution is: 204
