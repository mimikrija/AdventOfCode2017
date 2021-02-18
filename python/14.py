# Day 14: Disk Defragmentation

from santas_little_helpers import *
from knot_hash import dense_hash
from itertools import product
from collections import deque


def adjacents(in_coordinate):
    return {in_coordinate + complex(x, y) for x, y in {(0, 1), (0, -1), (1, 0), (-1, 0)}}


def remove_group(in_coordinates):
    remaining_coordinates = set(in_coordinates)
    start = remaining_coordinates.pop() # pop a random coord to start the search from
    frontier = deque()
    frontier.append(start)
    while frontier:
        current_position = frontier.pop()
        for next_position in adjacents(current_position):
            if next_position in remaining_coordinates:
                frontier.appendleft(next_position)
                remaining_coordinates.remove(next_position)
    return remaining_coordinates


def count_groups(in_coordinates):
    count = 0
    remaining = set(in_coordinates)
    while remaining:
        remaining = remove_group(remaining)
        count += 1
    return count


my_input = 'stpzcrnm'

# part 1: count used coordinates
part_1 = sum(int(c) for row in range(128) for c in dense_hash(my_input + '-' + str(row), 'bin'))


# part_2 generate all coordinates
all_used = {complex(row, column) for row in range(128) for column, c in enumerate(dense_hash(my_input + '-' + str(row), 'bin')) if int(c)}

part_2 = count_groups(all_used)


print_solutions(part_1, part_2)
# Part 1 solution is: 8250
# Part 2 solution is: 1113
