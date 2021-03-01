# Day 24: Electromagnetic Moat

from santas_little_helpers import *
from collections import deque



def bridge_strength(in_bridge):
    return sum(sum(comp) for comp in in_bridge)


def find_strongest_bridge(in_bridge, dangling, remaining_components):
    max_strength = 0
    incomplete_bridges = deque()
    incomplete_bridges.append([in_bridge, dangling])
    while incomplete_bridges:
        bridge, dangling = incomplete_bridges.popleft()
        for candidate in (comp for comp in remaining_components if dangling in comp):
            if candidate not in bridge:
                next_dangling = set(candidate) - {dangling}
                if len(next_dangling) != 0:
                    new_dangling = next_dangling.pop()
                else:
                    new_dangling = dangling
                incomplete_bridges.append([bridge + [candidate], new_dangling])

        max_strength = max(max_strength, bridge_strength(bridge))

    return max_strength



components = sorted([tuple(sorted(map(int, line.split('/')))) for line in get_input('inputs/24')])

# i did this by looking at the input, there's only
# one which contains a zero (unlike the example input)
starting_num_to_match = components[0][1]
# I checked, there are no duplicates in the input so this is ok:
rest = set(components[1:])

part_1 = find_strongest_bridge([components[0]], starting_num_to_match, rest)

print_solutions(part_1)
# Part 1 solution is: 1695
