# Day 13: Packet Scanners

from santas_little_helpers import *

def scanner_at_zero_position(time, size):
    return time % ((size-1)*2) == 0


depth_and_range = {layer: size for layer, size in (map(int, line.split(': ')) for line in get_input('inputs/13'))}

# part 1
severity = sum(time*size for time, size in depth_and_range.items() if scanner_at_zero_position(time, size))

# part 2: find initial delay which makes sure we don't get caught
delay = 0
while True:
    if not any(scanner_at_zero_position(time+delay, size) for time, size in depth_and_range.items()):
        break
    else:
        delay += 1

print_solutions(severity, delay)
# Part 1 solution is: 2384
# Part 2 solution is: 3921270
