# Day 24: Electromagnetic Moat

from santas_little_helpers import *


def bridge_strength(in_bridge):
    return sum(sum(comp) for comp in in_bridge)


components = sorted([tuple(sorted(map(int, line.split('/')))) for line in get_input('inputs/24')])

# i did this by looking at the input, there's only
# one which contains a zero (unlike the example input)
starting_component = components[0]
rest = components[1:]
