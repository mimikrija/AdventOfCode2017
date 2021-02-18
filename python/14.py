# Day 14: Disk Defragmentation

from santas_little_helpers import *
from knot_hash import dense_hash

my_input = 'stpzcrnm'

# part 1: count used coordinates
part_1 = sum(int(c) for row in range(128) for c in dense_hash(my_input + '-' + str(row), 'bin'))

print_solutions(part_1)
# Part 1 solution is: 8250
