# Day 19: A Series of Tubes

from santas_little_helpers import *

def neighbors(in_coordinate):
    return {in_coordinate + complex(x, y) for (x, y) in {(-1, 0), (1, 0), (0, -1), (0, 1)}}


def move_in_the_right_direction(passed_so_far, ways_to_go, current_position):
    direction = passed_so_far[-1] - passed_so_far[-2]
    #print(current_position, ways_to_go)
    for candidate in ways_to_go:
        #print(direction, candidate - current_position)
        if candidate - current_position == direction:
            return candidate

def walk_the_line(start, in_coordinates, directions):
    passed = [start]
    to_be_processed = set(in_coordinates) - set(passed)
    current_direction = directions[start]
    current = start
    crossroads = set()
    while to_be_processed:
        possible_ways_to_go = neighbors(current) & (to_be_processed | crossroads)
        #print(current, possible_ways_to_go)
        #print(f'crossroads: {crossroads}')
        if len(possible_ways_to_go) == 1:
            current = possible_ways_to_go.pop()
        elif len(possible_ways_to_go) == 2:
            current = move_in_the_right_direction(passed, possible_ways_to_go, current)
        else:
            #print('mooove in the right direction')
            crossroads.add(current)
            current = move_in_the_right_direction(passed, possible_ways_to_go, current)

        to_be_processed -= {current}
        passed.append(current)
        
    return passed


# def get_letters(in_passed, directions):
#     letters = [directions[coordinate] for coordinate in in_passed if]
#     for coordinate in in_passed:


directions = {}
positions = set()
for vertical, line in enumerate(get_input('inputs/19')):
    for horizontal, c in enumerate(line):
        if c != ' ':
            coordinate = complex(horizontal, vertical)
            positions.add(coordinate)
            directions[coordinate] = c
            if vertical == 0:
                start = coordinate

passed = walk_the_line(start, positions, directions)
part_1 = ''.join(c for c in (directions[point] for point in passed) if c not in '|+-')
part_2 = len(passed)

print_solutions(part_1, part_2)
# Part 1 solution is: GEPYAWTMLK
# Part 2 solution is: 17628
