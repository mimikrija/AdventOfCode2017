# Day 13: Packet Scanners

from santas_little_helpers import *

depth_and_range = {layer: size for layer, size in (map(int, line.split(': ')) for line in get_input('inputs/13'))}

