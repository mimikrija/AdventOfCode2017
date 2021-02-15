# Day 12: Digital Plumber

from santas_little_helpers import *
from collections import Counter


#connections = {one: rest for line in get_input('inputs/12') for one, rest in line.split(' <-> ')}
connections = {}
for line in get_input('inputs/12'):
    a, b = line.split(' <-> ')
    connections[a] = b.split(', ')

def count_connections(in_tree, find_next, all_programs):
    while find_next:
        temp_list = []
        for find_me in find_next:
            for child in in_tree[find_me]:
                if child not in all_programs:
                    temp_list.append(child)

        find_next = set(temp_list)

        all_programs |= set(find_next)
        count_connections(in_tree, find_next, all_programs)

    return set(all_programs)


part_1 = len(count_connections(connections,['0'], set('0')))

print_solutions(part_1)
