# Day 10: Knot Hash

from santas_little_helpers import *
from knot_hash import tie_the_knots, dense_hash, generate_lengths



lengths = [165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153]
size = 256

part_1_circle, _, _ = tie_the_knots(lengths)
part_1 = part_1_circle[0]*part_1_circle[1]


# part 2 new specifications

part_2 = dense_hash(lengths)


print_solutions(part_1, part_2)
# Part 1 solution is: 4114
# Part 2 solution is: 2f8c3d2100fdd57cec130d928b0fd2dd
