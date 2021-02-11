# Day 2: Corruption Checksum

from santas_little_helpers import *
from itertools import combinations

def evenly_divisible_pair(in_numbers):
    for pair in combinations(in_numbers, 2):
        big, small = sorted(pair, reverse=True)
        if big % small == 0:
            return big // small

rows = [sorted(map(int,row.split())) for row in get_input('inputs/02')]

part_1 = sum(row[-1] - row[0] for row in rows)
part_2 = sum(evenly_divisible_pair(row) for row in rows)

print_solutions(part_1, part_2)
