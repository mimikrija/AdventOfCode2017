# Day 13: Packet Scanners

from santas_little_helpers import *
from itertools import count

def scanner_at_zero_position(time, size):
    return time % ((size-1)*2) == 0


depth_and_range = {layer: size for layer, size in (map(int, line.split(': ')) for line in get_input('inputs/13'))}

# part 1
severity = sum(time*size for time, size in depth_and_range.items() if scanner_at_zero_position(time, size))

# part 2: find initial delay which makes sure we don't get caught
delay = next(offset for offset in count() # count() generates an endless range
            if not any(scanner_at_zero_position(time+offset, size)
            for time, size in depth_and_range.items()))


print_solutions(severity, delay)
# Part 1 solution is: 2384
# Part 2 solution is: 3921270
