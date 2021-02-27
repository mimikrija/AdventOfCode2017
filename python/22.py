# Day 22: Sporifica Virus

from santas_little_helpers import *


def burst(in_infected, current_position, in_direction, counter):
    infected = set(in_infected)
    if current_position in in_infected:
        # infected; turn right
        direction = in_direction*(0+1j)
        infected.remove(current_position)
    else:
        # not infected; turn left and add to infected
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


def burst_two(infected, flagged, weakened, current_position, direction, counter):

    if current_position in infected:
        # infected; turn right and add to flagged
        direction *= 0+1j
        infected.remove(current_position)
        flagged.add(current_position)
    elif current_position in flagged:
        # flagged; reverse direction and clean
        direction = -direction
        flagged.remove(current_position)
    elif current_position in weakened:
        # weakened; keep direction the same and infect it
        infected.add(current_position)
        weakened.remove(current_position)
        counter += 1
    else:
        # not infected; turn left and add to weakened
        direction *= 0-1j
        weakened.add(current_position)

    current_position += direction

    return counter, current_position, direction


def run_bursts_2(num, in_infected, start, starting_direction):
    infected = set(in_infected)
    flagged = set()
    weakened = set()
    current_position = start
    direction = starting_direction
    counter = 0
    for _ in range(num):
        counter, current_position, direction = burst_two(infected, flagged, weakened, current_position, direction, counter)
    return counter


input_map = get_input('inputs/22')
# we start from the middle
middle_of_the_map = complex(len(input_map[0])//2, len(input_map)//2)
# we start facing up
starting_direction = 0-1j

# set of initially infected nodes
infected = {complex(horizontal, vertical) for vertical, line in enumerate(input_map) for horizontal, c in enumerate(line) if c == '#'}

infections_after_10000_bursts = run_bursts(10000, infected, middle_of_the_map, starting_direction)
party2_infections = run_bursts_2(10000000, infected, middle_of_the_map, starting_direction)

print_solutions(infections_after_10000_bursts, party2_infections)
# Part 1 solution is: 5246
# Part 2 solution is: 2512059
