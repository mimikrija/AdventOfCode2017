# Day 11: Hex Ed

from santas_little_helpers import *


HEX_DIRECTIONS = {
     'n': (0, 1, -1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
     's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0)
}

def hex_grid_distance(in_hex):
    " Red Blob Manhattan distance of `in_hex` from (0, 0, 0) using cube coords"
    return sum(abs(coord) for coord in in_hex) // 2

def hex_add(in_hex_a, in_hex_b):
    return tuple(coordinate_a + coordinate_b for coordinate_a, coordinate_b in zip(in_hex_a, in_hex_b))

def visit_all(in_directions):
    start = (0, 0, 0)
    current = start
    all_coords = set()
    for direction in directions:
        current = hex_add(current, HEX_DIRECTIONS[direction])
        all_coords.add(current)

    return map(hex_grid_distance, (current, max(all_coords, key=hex_grid_distance)))


directions = get_input('inputs/11',',')

part_1, part_2 = visit_all(directions)

print_solutions(part_1, part_2)
# Part 1 solution is: 784
# Part 2 solution is: 1558
