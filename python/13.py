# Day 13: Packet Scanners

from santas_little_helpers import *

def scanner_at_zero_position(time, size):
    return time % ((size-1)*2) == 0


depth_and_range = {layer: size for layer, size in (map(int, line.split(': ')) for line in get_input('inputs/13'))}

# part 1
severity = sum(time*size for time, size in depth_and_range.items() if scanner_at_zero_position(time, size))


print_solutions(severity)
# Part 1 solution is: 2384
