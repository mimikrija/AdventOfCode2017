from santas_little_helpers import *

def burst(in_infected, current_position, in_direction, counter):
    infected = set(in_infected)
    if current_position in in_infected:
        # infected; turn right
        direction = in_direction*(0+1j)
        infected.remove(current_position)
    else:
        # not indected; turn left and add to infected
        direction = in_direction * (0-1j)
        infected.add(current_position)
        counter += 1

    return infected, current_position + direction, direction, counter


def run_bursts(num, in_infected, start, starting_direction):
    infected = set(in_infected)
    current_position = start
    direction = starting_direction
    counter = 0
    for _ in range(num):
        infected, current_position, direction, counter = burst(infected, current_position, direction, counter)
    return counter


input_map = get_input('inputs/22')
# we start from the middle
middle_of_the_map = complex(len(input_map[0])//2, len(input_map)//2)
# we start facing up
starting_direction = 0-1j

# set of initially infected nodes
infected = {complex(horizontal, vertical) for vertical, line in enumerate(input_map) for horizontal, c in enumerate(line) if c == '#'}

infections_after_10000_bursts = run_bursts(10000, infected, middle_of_the_map, starting_direction)

print_solutions(infections_after_10000_bursts)
