# Day 25: The Halting Problem

from santas_little_helpers import *

states = {
    'A': ((1, 1, 'B'), (0, -1, 'C')),
    'B': ((1, -1, 'A'), (1, 1, 'D')),
    'C': ((1, 1, 'A'), (0, -1, 'E')),
    'D': ((1, 1, 'A'), (0, 1, 'B')),
    'E': ((1, -1, 'F'), (1, -1, 'C')),
    'F': ((1, 1, 'D'), (1, 1, 'A'))
}


def turing(tape, steps, initial_state):
    state = initial_state
    index = 0
    for _ in range(steps):
        current_value = tape.get(index, 0)
        next_value, index_increment, state = states[state][current_value]
        tape[index] = next_value
        index += index_increment


tape = {0: 0}
turing(tape, 12919244, 'A')
checksum = sum(tape.values())
print_solutions(checksum)
# Part 1 solution is: 4287
